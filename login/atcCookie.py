#!/usr/bin/ python3
# -*- coding: utf-8 -*-
import json
from time import sleep

import requests
from bs4 import BeautifulSoup


class ATCLogin(object):

    def __init__(self, account, password, jiraUrl):
        self.account = account
        self.password = password
        self.jiraUrl = jiraUrl

        self.login_data = {
            "os_username": self.account,
            "os_password": self.password,
            "os_destination": '/browse/ATLANTIS-1',
            "user_role": '',
            'atl_token': '',
            'login': 'Log In'
        }

        self.session = requests.session()
        self.session.headers = {
            'accept-encoding': 'gzip, deflate, br, zstd',
            'Referer': self.jiraUrl,
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }

    '''
        1.校验是否已经登陆
        2.没登陆去登陆
        3.登陆直接去jira单拿到desc内容
    '''
    def login(self):
        if self.check_login():
            print('已经有cookie了')
            return True

        print('没有cookie，需要重新登陆')

        login_api = 'https://atc.bmwgroup.net/jira/login.jsp'
        headers = self.session.headers
        self.session.post(login_api, data=self.login_data, headers=headers)
        sleep(1)

        if self.check_login():
            print('登录成功')
            return True
        print('登录失败')
        return False

    def check_login(self):
        resp = self.session.get(self.jiraUrl, allow_redirects=False)
        if resp.status_code == 200:
            print(self.session.cookies)
            return True
        return False

    def getDescCtx(self):
        resp = self.session.get(self.jiraUrl)
        soup = BeautifulSoup(resp.text, 'html.parser')
        # 查找所有class为user-content-block的div元素
        blocks = soup.find_all('div', class_='user-content-block')

        # 遍历匹配的div元素，写入文件
        with open('desc.txt', 'w') as f:
            for block in blocks:
                text_lines = block.get_text(separator='\n', strip=True).split('\n')
                for line in text_lines:
                    f.write(line + '\n')

if __name__ == '__main__':
    account = input("请输入你的账号：")
    password = input("请输入你的密码：")
    jiraURL = input("输入你想进入的jira链接：")
    atc = ATCLogin(account, password, jiraURL)


    res = atc.login()
    if res:
        atc.getDescCtx()

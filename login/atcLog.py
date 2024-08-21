from getpass import getpass
from time import sleep
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AtcLogin(object):
    def __init__(self,account,password,jiraurl):
        self.account = account
        self.password = password
        self.jiraurl = jiraurl
        options = webdriver.ChromeOptions()
        # 设置为开发者模式，避免被识别
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])
        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 5, 0.2)
        self.url = 'https://atc.bmwgroup.net/jira/login.jsp?native_login='


    def login(self):
        self.browser.get(self.url)

        username = self.wait.until(EC.element_to_be_clickable((By.ID, 'login-form-username')))
        password = self.wait.until(EC.element_to_be_clickable((By.ID, 'login-form-password')))
        sleep(1)
        username.send_keys(self.account)
        sleep(1)
        password.send_keys(self.password)

        subBtn = self.wait.until(EC.element_to_be_clickable((By.ID, 'login-form-submit')))
        subBtn.click()

        try:
            self.browser.get(self.jiraurl)
            desText = self.wait.until(EC.element_to_be_clickable((By.ID, 'description-val')))
            print(desText.text)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    ACCOUNT = input('请输入您的账号:')
    PASSWORD = getpass('请输入您的密码:')
    JIRAURL = getpass('请输入您要访问的jira链接:')
    atc = AtcLogin(ACCOUNT, PASSWORD,JIRAURL)  # 输入账号和密码
    atc.login()

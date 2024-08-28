import requests
import time


def download_one(url):
    resp = requests.get(url, headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    })
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    for site in sites:
        download_one(site)


def main():
    sites = [
        'https://m.douban.com/movie/',
        'https://movie.douban.com/subject/36847744/',
        'https://movie.douban.com/',
        'https://movie.douban.com/subject/35712796/?tag=%E7%83%AD%E9%97%A8&from=gaia'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print(f'Download {len(sites)} sites in {end_time - start_time} seconds')


if __name__ == '__main__':
    main()
import requests
import time
import concurrent.futures


def download_one(url):
    resp = requests.get(url, headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    })
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one,site)
            to_do.append(future)

        for future in concurrent.futures.as_completed(to_do):
            future.result()


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
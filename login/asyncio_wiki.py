import time
import asyncio
import aiohttp


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.content)

async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        'https://m.douban.com/movie/',
        'https://movie.douban.com/subject/36847744/',
        'https://movie.douban.com/',
        'https://movie.douban.com/subject/35712796/?tag=%E7%83%AD%E9%97%A8&from=gaia'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print(f'Download {len(sites)} sites in {end_time - start_time} seconds')


if __name__ == '__main__':
    main()
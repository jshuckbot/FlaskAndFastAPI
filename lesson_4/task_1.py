import sys
import asyncio
import aiohttp
import requests
import threading
from time import perf_counter
from multiprocessing import Process

urls = [
    'https://gurman-bel.ru/assets/uploads/2015/10/markirovka_1.jpg',
    'https://klike.net/uploads/posts/2022-08/1661836199_c-4.jpg',
]


def download_image_sync(url: str):
    """Синхронно скачивает изображения"""
    start_time = perf_counter()
    response = requests.get(url)

    filename = url.split('/')[-1]
    filename = 'downloads/' + filename
    with open(filename, "bw") as f:
        f.write(response.content)
    print(f"Downloaded {url} in {perf_counter() - start_time:.2f} seconds")


async def download_image_async(url: str):
    """Асинхронно скачивает изображение"""
    start_time = perf_counter()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img = await response.content.read()
            filename = url.split('/')[-1]
            filename = 'downloads/' + filename
            with open(filename, "bw", ) as f:
                f.write(img)
    print(f"Downloaded {url} in {perf_counter() - start_time:.2f} seconds")


def download_threading(urls: list):
    """Скачивает в потоках картинки по заданным urls"""
    print('Threads')

    threads = []
    start_time = perf_counter()

    for url in urls:
        thread = threading.Thread(target=download_image_sync, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Downloaded time all urls using threads -> {perf_counter() - start_time:.2f} seconds")


def download_process(urls: list):
    """Скачивает в процессах картинки по заданным urls"""
    print('Processes')

    processes = []
    start_time = perf_counter()

    for url in urls:
        thread = Process(target=download_image_sync, args=(url,))
        processes.append(thread)
        thread.start()

    for process in processes:
        process.join()

    print(f"Downloaded time all urls using processes -> {perf_counter() - start_time:.2f} seconds")


async def download_asyncio(urls: list):
    """Скачивает асинхронно картинки по заданным urls"""
    print('Async')
    start_time = perf_counter()
    await asyncio.gather(*[await asyncio.to_thread(download_image_async, url) for url in urls])
    print(f"Downloaded time using asyncio: {perf_counter() - start_time:.2f} seconds")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        urls = sys.argv[1:]

    download_threading(urls)
    download_process(urls)
    asyncio.run(download_asyncio(urls))

import argparse
import asyncio
import multiprocessing
import aiohttp
import requests
import threading
import time

urls_list = ['https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg',
               'https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-48.jpg',
               'http://chudo-prirody.com/uploads/posts/2021-08/1628917339_87-p-foto-malenkikh-rizhikh-kotyat-98.jpg',
               'https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663579262_51-mykaleidoscope-ru-p-veselie-koshechki-krasivo-54.jpg',
               'https://www.ejin.ru/wp-content/uploads/2017/09/9-1022.jpg',
               'https://s1.1zoom.ru/b5050/667/Cats_Kittens_Grass_Bokeh_590075_3840x2400.jpg',
               'https://www.sunny-cat.ru/datas/users/1-elefant017.jpg',
               'https://w-dog.ru/wallpapers/0/14/503116390422985/porodistyj-kotenok-na-beloj-prostyne.jpg',
               'https://rare-gallery.com/uploads/posts/881890-Cats-Grass-Kittens-Bokeh.jpg',
               'https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-47.jpg']

extensions = ["png", "jpg", "bmp"]

def get_filename(url: str) -> str | None:
    filename = None
    url_parts = url.split(".")
    for part in range(len(url_parts)):
        for ext in extensions:
            if url_parts[part].startswith(ext):
                name = url_parts[part - 1].split("/")[1]
                print(name)
                filename = name + "." + ext
    if filename is None:
        print(f"This URL {url} dont contain picture")
    return filename


def download_pict(url: str):
    start_time = time.time()
    response = requests.get(url)
    filename = get_filename(url)
    if filename:
        with open('task_hw_files/' + filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
            print(f"{url} download in {time.time() - start_time:.4f} seconds")


async def a_download_pict(url: str):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = get_filename(url)
            if filename:
                with open(filename, "wb") as file:
                    file.write(content)
                print(f"{url} download in {time.time()- start_time: 4f} seconds")


async def async_download():
    start_time = time.time()
    tasks = [asyncio.create_task(a_download_pict(url)) for url in urls_list]
    await asyncio.gather(*tasks)
    print(f"Download async finished in {time.time() - start_time:.4f} seconds")


def multiproc_download():
    processes = []
    start_time = time.time()
    for url in urls_list:
        process = multiprocessing.Process(target=download_pict, args=([url]))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print(f"Download multiprocessing finished in {time.time() - start_time:.4f} seconds")


def threads_download():
    threads = []
    start_time = time.time()
    for url in urls_list:
        thread = threading.Thread(target=download_pict, args=[url])
        threads.append(thread)
        thread.start()
    for tread in threads:
        thread.join()
    print(f"Download threading finishing in {time.time() - start_time:.4f} seconds")


def parse():
    parser = argparse.ArgumentParser(
        prog="parser module", description="program for download pictures"
    )
    parser.add_argument("-u", "--url", help="url of picture", type=str, default=urls_list)
    arguments = parser.parse_args()
    urls = arguments.url
    return urls


if __name__ == "__main__":
    parse()
    multiproc_download()
    print("_____")
    threads_download()
    print("_____")
    asyncio.run(async_download())





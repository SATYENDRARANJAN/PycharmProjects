import asyncio
import time

import aiohttp
import aiofiles

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        html = await response.text()
        return html

async def write_to_file(file,text,i):
    async with aiofiles.open(file,'w') as f:
        print(str (i) + "--in1")
        await f.write(text)
        print(str (i) + "--in2")

#
# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         response = await session.get(url)



async def demo(url,i):
    task=[]
    file = f'{url.split("//")[-1]}.txt'
    print(str(i) + "--start")
    print(str(i) + "-- STARTING TO DOWNLOAD ")

    html = await fetch(url)
    print(str(i) + "-- ENDING TO DOWNLOAD ")

    print(str(i) + "--end")
    print(str(i) + "-- STARTING TO WRITE ")
    await write_to_file(file,html,i)
    print(str(i) + "-- ENDING TO WRITE ")


async def main1(urls):
    tasks =[]
    i=0
    for url in urls:

        print("start ")
        tasks.append( demo(url,i))
        i = i + 1
    start  = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    print(end - start )






# asyncio.run(main(('https://google.com','https://facebook.com','https://python.org')))

async def main2():


    await main1(('https://google.com','https://facebook.com','https://python.org'))


async def main():
    await main2()



asyncio.run(main2())
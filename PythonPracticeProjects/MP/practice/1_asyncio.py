import asyncio
import time

def sync_f():

    print("one1",end="")
    time.sleep(4)
    print("two",end =" ")

async def async_f():

    print('one',end=' ')
    await asyncio.sleep(4)
    print('two',end=' ')



async def main():
    # await async_f() - NO OUTPUT
    tasks = [async_f() for _ in range(2)]
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
end = time.time()
print(end-start)

start = time.time()
for _ in range(4):
    sync_f()
end = time.time()
print(end-start)
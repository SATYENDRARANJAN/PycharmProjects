
import aiohttp, asyncio, async_timeout
import time


async def get_url(session, url, corou_id=-1, timeout=10):
    start = time.time()
    res = ""
    # SECTION-UNDER-TEST
    with async_timeout.timeout(timeout):  # TIMEOUT-PROTECTED
        async with session.get(url) as response:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                res += str(chunk)
            await response.release()
    end = time.time()
    runtime = end - start

    print(
        "Now finished get_url(launch_id:<{2: >2d}>) E2E execution took {0: >9d} [us](Safety timeout was set {1: >2d} [s])".format(
            runtime, timeout, corou_id))
    return runtime, len(res)


async def async_payload_wrapper(async_loop, number_of_tests=10, url="http://example.com"):

    url = "https://api.religarehealthinsurance.com/relinterfacerestful/religare/restful/getPolicyStatus/"
    async with aiohttp.ClientSession(loop=async_loop) as session:
        corou_to_execute = [get_url(session, url, launchID) for launchID in
                                              range(min(number_of_tests, 1000))]
        await asyncio.gather(*corou_to_execute)
if __name__ == '__main__':

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(async_payload_wrapper(event_loop, 25))
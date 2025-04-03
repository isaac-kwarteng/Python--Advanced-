import asyncio
import aiohttp


async def producer(queue: asyncio.Queue, urls: list[str]) -> None:
    if urls:
        print("Queuing urls...")   
        for url in urls:
            await queue.put(url)

        await queue.put(None)  # Signal the consumer to stop
        print("All urls queued.")
    else:
        print("Please include the urls")


async def consumer(
    queue: asyncio.Queue, session: aiohttp.ClientSession, worker_id: int
) -> None:
    """Worker that fetches URLs from the queue"""
    while True:
        url = await queue.get()
        if url is None:
            break
        else:
            try:
                async with session.get(url) as response:
                    content = await response.text()
                    print(f"Worker - {worker_id} finished: {url[:30]}... ")
            except Exception as e:
                print(f"{e} \n Worker - {worker_id} failed to fetch: {url}")

            queue.task_done()


async def main():
    queue = asyncio.Queue()
    urls = ["wwww.w3schools.com", "www.google.com"]

    async with aiohttp.ClientSession() as session:
        producing_tasks = asyncio.create_task(producer(queue, urls))
        consuming_tasks = [
            asyncio.create_task(consumer(queue, session, i)) for i in range(len(urls))
        ]
        await producing_tasks
        await queue.join()

        for _ in range(len(consuming_tasks)):
            await queue.put(None)

        await asyncio.gather(*consuming_tasks)


if __name__=="__main__":
    asyncio.run(main())
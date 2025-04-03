import asyncio

# async def main():
#     print("tim")
#     task = asyncio.create_task(foo("text"))
#     await asyncio.sleep(0.5)
#     print("finished")
#     await asyncio.gather(task)


# async def foo(text):
#     print(text)
#     await asyncio.sleep(10)


# asyncio.run(main())


# async def api_call(endpoint, delay) -> str:
#     try:
#         print(f"Fetching {endpoint}")
#         await asyncio.sleep(delay)
#         print(f"Done with {endpoint}")
#         return f"Response from {endpoint}"
#     except Exception as e:
#         return f"Error from {endpoint}"


# async def main():
#     await asyncio.gather(
#         api_call("google.com", 1),
#         api_call("facebook.com", 5),
#         api_call("twitter.com", 3),
#     )


# if __name__ == "__main__":
#     asyncio.run(main())


# # Handling errors in async code
# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(2)
#     print("Task 1 done")

# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(2)
#     print("Task 2 done")


# async def task_with_error():
#     print("Starting risky task...")
#     await asyncio.sleep(1)
#     raise ValueError("Something went wrong!")


# async def main():
#     try:
#         await asyncio.gather(task1(), task_with_error(), task2())
#     except Exception as e:
#         print(f"Error caught: {e}")


# asyncio.run(main())


# Semaphores
# They are used to limit the number of coroutines that can access a resource at a time.
sem = asyncio.Semaphore(3)  # Allow only 3 concurrent tasks


async def limited_task(name):
    async with sem:
        print(f"Starting {name}")
        await asyncio.sleep(2)
        print(f"Finished {name}")


async def main():
    tasks = [limited_task(f"Task {i}") for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())

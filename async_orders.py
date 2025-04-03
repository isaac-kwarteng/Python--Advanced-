import asyncio


async def serve_orders(orders: list[str]):
    for order in orders:
        print(f"Making {order}")
        await asyncio.sleep(1.5)
        yield (f"{order} is ready")


async def main():
    orders = ["pizza", "sushi", "salad"]
    async for order in serve_orders(orders):
        print(f"{order} is served")


if __name__ == "__main__":
    asyncio.run(main())

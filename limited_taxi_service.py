import asyncio


async def take_taxi(passenger: str, sem: asyncio.Semaphore) -> None:
    async with sem:
        print("Taking taxi")

        # Simulating boarding taxi
        await asyncio.sleep(3)
        print(f"{passenger} has arrived at his destination")


async def main() -> None:
    number_of_taxis: int = 3
    semaphore = asyncio.Semaphore(number_of_taxis)
    passengers = [take_taxi(f"Passenger {i+1}", semaphore) for i in range(6)]

    await asyncio.gather(*passengers)


if __name__ == "__main__":
    asyncio.run(main())

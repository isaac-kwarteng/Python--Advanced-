import asyncio


async def cook_rice() -> None:
    """Simulates cooking rice"""
    print("Cooking rice")
    await asyncio.sleep(5)
    print("The rice is ready")


async def boil_water() -> None:
    """Simulates boiling water"""
    print("Boiling water")
    await asyncio.sleep(3)
    print("Boiling complete")


async def chop_vegetables() -> None:
    """Simulates chopping vegetables"""
    print("Chopping vegetables")
    await asyncio.sleep(1)
    print("Chopping complete")


async def main() -> None:
    """Main function to run the cooking tasks concurrently"""
    await asyncio.gather(cook_rice(), boil_water(), chop_vegetables())


if __name__ == "__main__":
    asyncio.run(main())

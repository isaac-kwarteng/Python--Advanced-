import asyncio


balance: int = 100


async def withdraw(amount: int, lock: asyncio.Lock) -> None:
    async with lock:
        global balance
        print("Transaction is in progess...")
        await asyncio.sleep(3)
        if balance >= amount:
            balance -= amount
            print(f"Balance is now {balance}")
        else:
            print("Balance is not enough")


async def main() -> None:
    lock = asyncio.Lock()
    await asyncio.gather(withdraw(5, lock), withdraw(48, lock))


if __name__ == "__main__":
    asyncio.run(main())

from dataclasses import dataclass


@dataclass
class BankAccount:
    account_number: int
    holder_name: str
    balance: int

    def __post_init__(self):
        if self.balance < 0:
            print("Balance must must be negative")


if __name__=="__main__":
    new_account: BankAccount = BankAccount(654654654, "Isaac", 500)
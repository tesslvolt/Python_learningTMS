
class BankAccount:
    bank_name = "PythonBank"
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_info(self, owner, balance):
        print(f"Счет: {self.owner}, баланс: {self.balance}")

        def _secret_message():
class ATM:

    def __init__(self):
        self.banknotes = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for index, count in enumerate(banknotesCount):
            self.banknotes[index] += count

    def withdraw(self, amount: int) -> List[int]:

        nominals = [20, 50, 100, 200, 500]

        answer = [0]*5
        for i in range(len(nominals) - 1, -1, -1):
            if amount == 0:
                break
            if amount >= nominals[i]:
                count = min(self.banknotes[i], amount // nominals[i])
                answer[i] = count
                amount -= count*nominals[i]

        if amount == 0:
            for i, ans in enumerate(answer):
                self.banknotes[i] -= ans

        return answer if amount == 0 else [-1]

    # Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
import random
import time
import threading as tr


class Bank:
    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = tr.Lock()

    def deposit(self):
        amount = round(random.uniform(50, 500), 2)
        time.sleep(0.001)
        if self.balance >= 500 and self.lock.locked():
            time.sleep(0.001)
            self.lock.release()
            time.sleep(0.001)
            self.balance += amount
            time.sleep(0.05)
            print(f'Баланс: {self.balance}')
            time.sleep(0.001)
        else:
            # self.lock.acquire()
            time.sleep(0.001)
            self.balance += amount
            time.sleep(0.001)
            print(f'Баланс: {self.balance}')
            time.sleep(0.001)

        print(f"Пополнение: {amount}. Баланс: {self.balance}")

    def take(self):
        amount = round(random.uniform(50, 500), 2)
        time.sleep(0.001)
        print(f"Запрос на {amount}")
        time.sleep(0.001)
        if amount <= self.balance:
            time.sleep(0.001)
            self.balance -= amount
            time.sleep(0.001)
            print(f"Снятие: {amount}.Баланс: {self.balance}")
            time.sleep(0.001)
        else:
            time.sleep(0.001)
            print("Запрос отклонен, недостаточно средств")
            time.sleep(0.001)
            self.lock.acquire()
            time.sleep(0.001)

bk = Bank(0, tr.Lock())



# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank

th1 = tr.Thread(target=Bank.deposit, args=(bk,))

th2 = tr.Thread(target=Bank.take, args=(bk,))



th1.start()

th2.start()

th1.join()

th2.join()



print(f'Итоговый баланс: {bk.balance}')
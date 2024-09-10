import math

class Computation:

    def __init__(self):
        ...

    @staticmethod
    def factorial(n):
        return math.factorial(n)

    @staticmethod
    def summa(*args):
        return sum(args)

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_is_prime(self, n):
        for j in range(2, n+1):
            if self.is_prime(j):
                print(j, end=" ")
        return ""

    def table_mult(self, n):
        for number in range(1, 11):
            print(f"{number} * {n} = {number * n}")
        return ""

    def all_tables_mult(self):
        n = 1
        while n <= 10:
            for j in range(1, 11):
                print(f"{j} * {n} = {j * n}")
            n += 1
            print()
        return ""




class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.prime_numbers = []

    def get_prime_numbers(self):
        for number in range(2, self.n + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)
                yield number






# num = PrimeNumbers(11)
# num.__call__()
# print(list(num.__call__()))

prime_number_iterator = PrimeNumbers(n=11)
for number in prime_number_iterator:
    print(number)



def nprimos(a):
    def primo(b):
        for i in range(2, b):
            if b % i == 0:
                return False
        return True
    print(primo(a))
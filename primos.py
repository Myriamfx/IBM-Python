def nprimos(a)
    b=21
    def primo(b):
        for i in range(2,b):
            if b%i==0:
                return False
        return True
    print(primo(b))o
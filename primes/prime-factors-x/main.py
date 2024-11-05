def find_primes(x):
    primes = []

    r = x

    d = 2

    while r > 1 :
        if r % d == 0 :
            primes.append(d)

            r //= d

            d = 2
        else :
            d+=1

    return primes

def main() :
    while True :

        while True :
            x = int(input("Give x (>=0, integer) :"))

            if x >= 0 :
                break

        print(find_primes(x))

if __name__ == "__main__" :
    main()

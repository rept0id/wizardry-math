import math

def is_prime(x) :
    if x < 0:
        raise ValueError("Negative value provided")

    if x == 1:
        return False

    for d in range (2, (int(math.sqrt(x)) + 1)) :
        if x % d == 0 :
            return False

    return True

def main() :
    while True :

        while True :
            x = int(input("Give x (>=0, integer) :"))

            if x >= 0 :
                break

        print(is_prime(x))

if __name__ == "__main__" :
    main()

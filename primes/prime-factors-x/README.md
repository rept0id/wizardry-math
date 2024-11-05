# prime-factors-x

The prime factors of a given number are the numbers whose multiplication results in the original number.

For example, the prime factors of 100 are [2, 2, 5, 5], since 2 * 2 * 5 * 5 = 100.

There are various methods to find prime factors, including deterministic and probabilistic approaches.

## Approaches

### Deterministic

Deterministic approaches will try **series** of numbers until we get the desired behaviour.

In our case, of prime factors, the desired behaviour is simply division with a n number (where n>1) to not have a remainder.
That mean we have found one of our prime numbers. Then we repeat the same for the result until we reach 1.
N has to be >1 because dividing with 1 always gives no remainder no matter if the number is prime or not.

Usually, the n numbers we should try shouldn't be bigger than the square root (sqrt) of the given number x (sqrt(x)).
This is because of a very simple paradox :
```
If sqrt(x) had a factor greater than sqrt(x),
it would also need a corresponding factor smaller than sqrt(x),
as the product of two factors larger than sqrt(n), would exceed n).
```

To warp up, in a deterministic approach :
- We need to check **all** numbers (thus "determinism") from 2 up to sqrt(x) to see if any of them divide x without a remainder.
- If a number n divides x with no remainder, we add it to the "prime factors" list.
- We then repeat this process for the result, checking all numbers from 2 up to sqrt(result).
- This process continues until we reach 1.

A good example can be the number 51.

For 51 :

| **Calculation**                                                  | **Prime Factors of 51** |
|------------------------------------------------------------------|--------------------------|
| (51/2 = 25.5) (remainder : true)   | []                          |                          |
| (51/***3*** = **17**), (remainder : *false*)  | [3]              |                          |
| -***3*** is added to the list of prime factors.-                 |                          |
| -Now we continue with the result, **17**, to find it's factors.- |                          |
|                                                                  |                          |
| (17/2 = 8.5) (remainder : true)                                  | [3]                      |
| (17/3 = 5.66) (remainder : true)                                 | [3]                      |
| ...                                                              |                          |
| (17/16 = 1.06), (remainder : true)                               | [3]                      |
| (17/***17*** = **1**\), (remainder : *false*)                    | [3, 17]                  |
| -***17*** is added to the list of prime factors.-                |                          |
| -Since the result is now **1**, we stop here.-                   |                          |

**Final Prime Factors of 51:** [3, 17]

### Propabilistic

Probabilistic approaches will try random numbers or numbers related to x (e.g., if x = 15, a good guess is 5).

There are methods developed which can be really fast and have very small error range :

- AKS primality test
- Elliptic curve primality proving
- Baillie–PSW primality test
- Miller–Rabin primality test
- Solovay–Strassen primality test

From them, `Miller–Rabin` has the simplest algorithm, in a software engineering approach.

Also, there is the `Fermat primality test` which is a solid methiod of finding if a number is prime.

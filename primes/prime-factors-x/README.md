# prime-factors-x

The prime factors of a given number are the numbers whose product results in the original number.

For example, the prime factors of 100 are [2, 2, 5, 5], since 2 * 2 * 5 * 5 = 100.

There are various methods for finding prime factors, including both deterministic and probabilistic approaches.

## Approaches

### Deterministic
Deterministic approaches involve testing a **series** of numbers until we achieve the desired outcome.

In our case, the desired outcome is division by a number n (where n > 1) such that there is no remainder. This means we have found one of the prime factors. We then repeat the process with the result until we reach 1. n must be greater than 1, because dividing by 1 always results in no remainder, regardless of whether the number is prime or not.

Typically, the numbers we test should not be greater than the square root of the given number x (sqrt(x)). This is because of a simple paradox:

```
If sqrt(x) had a factor greater than sqrt(x),
it would also need a corresponding factor smaller than sqrt(x),
as the product of two factors larger than sqrt(n), would exceed n).
```

To wrap up, in a deterministic approach:
- We need to check **all** numbers (hence "determinism") from 2 up to the square root of x to see if any of them divide x without a remainder.
- If a number n divides x with no remainder, we add it to the "prime factors" list.
- We then repeat this process for the result, checking all numbers from 2 up to the square root of the result.
- This process continues until we reach 1.

A good example is the number 51.

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

Probabilistic approaches involve trying random numbers or numbers related to x (e.g., if x = 15, a good guess is 5).

There are methods that have been developed which can be very fast and have a very small error range:

- AKS primality test
- Elliptic curve primality proving
- Baillie–PSW primality test
- Miller–Rabin primality test
- Solovay–Strassen primality test

From them, the `Miller–Rabin` test has the simplest algorithm from a software engineering perspective.

There is also the `Fermat primality test`, which is a solid method for determining if a number is prime.

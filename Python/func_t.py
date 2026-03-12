# function to add two numbers.
def add(a, b):
    return a + b


print(add(4, 4))


# function to subtract two numbers.
def sub(a, b):
    return a - b


print(sub(4, 4))


# function to multiply two numbers.
def mul(a, b):
    return a * b


print(mul(8, 8))


# function to divide two numbers.
def div(a, b):
    return a / b


print(div(100, 20))


# function to find the square of a number.
def sequence(n):
    return (n * n)


print(sequence(2))


# function to check whether a number is even or odd.
def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check(5))


# function to find the largest of two numbers.
def largest(a, b):
    if a > b:
        return a
    else:
        return b


print(largest(10, 20))


# function to count vowels in a string.
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count


print(count_vowels("Hello"))


# function to reverse a string.
def reverse(text):
    return text[::-1]


print(reverse("NIKILE EINES DHONI"))


# function to find factorial of a number.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(factorial(6))


# function to find sum of list elements.
def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total


print(sum_list([1, 2, 3]))


# function to find maximum number in a list.
def max_list(lst):
    return max(lst)


print(max_list([5, 10, 3]))


# function to check whether a number is prime.
def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"


print(is_prime(7))


# function to count characters in a string.
def count_char(text):
    return len(text)


print(count_char("Athiban"))


# function to return multiplication table of a number.
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


table(8)




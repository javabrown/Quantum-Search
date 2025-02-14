def factorial_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def de_factorial(fact):
    n = 0
    while fact > 1:
        n += 1
        fact /= n
    if fact == 1:
        return n
    else:
        return "Invalid factorial number"

if __name__== "__main__":
    num_str = input("Enter Number to perform factorial: ")
    num = int(num_str)
  
    fact = factorial_for_loop(num)
    print(f"Factorial of {num} : {fact}")

    defact = de_factorial(fact)

    print(defact)
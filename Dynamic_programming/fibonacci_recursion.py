def fib(n):
    if n < 0:
        return "error"
    if n == 0:
        return 0
    if n == 1:
        return 1

    sum= fib(n-1) + fib(n-2)
    return sum


def main():
    n = int(input("Enter the value of n: "))
    result= fib(n)
    print(result)
    

if __name__ == "__main__":
    main()

#fibonachi series
def recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return recursion(n - 2) + recursion(n - 1)


for i in range(6):
    print(recursion(i))

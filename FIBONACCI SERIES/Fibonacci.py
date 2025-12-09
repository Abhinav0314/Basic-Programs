def fib_loop1(n):
    first, second = 0, 1
    for i in range(n):
        third = first + second
        print(third)
        first = second
        second = third
def fib_loop2(n):
    ans = [0,1]
    for i in range(2,n+1):
        ans.append(ans[i-1] + ans[i-2])
    return ans
def fib_recursive(n):
    if n <= 0:
        return '-1'
    elif n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)
print
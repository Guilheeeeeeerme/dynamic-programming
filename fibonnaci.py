
# Fibonacci pure and using Dynamic Programming
import time

mem = [0,1]

def fib(n: int):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_dyn(n: int):

    if n < 2:
        return n
    else:
        while len(mem) <= n:
            mem.append(0)

        if mem[n - 1] == 0:
            mem[n - 1] = fib_dyn(n - 1)

        if mem[n - 2] == 0:
            mem[n - 2] = fib_dyn(n - 2)

        mem[n] = mem[n - 1] + mem[n - 2]

        return mem[n]

fib_dyn_points = [];
fib_points = [];

for fibTest in range(50):

    start_time = time.time()
    # cleaning memory to force 
    # DP to run from scratch
    mem = [0,1]

    fib_dyn(fibTest)
    elapsed_time = time.time() - start_time
    fib_dyn_points.append([fibTest, elapsed_time])

    start_time = time.time()
    fib(fibTest)
    elapsed_time = time.time() - start_time
    fib_points.append([fibTest, elapsed_time])

    print(fib_dyn_points)
    print(fib_points)


import random
import time

C = 15                     # Capacity
mem = {}

Weight = [3, 4, 2, 6, 7, 3, 5]    # List of weights
Value = [7, 9, 5, 12, 14, 6, 12]     # List of values

# Weight = [6, 8, 1, 9, 7]    # List of weights
# Value = [9, 4, 2, 8, 6]     # List of values


def Knapsack(n, capacity):

    if(n == -1 or capacity == 0):
        return 0

    no = Knapsack(n - 1, capacity)

    if(Weight[n] > capacity):
        result = no
    else:
        yes = Value[n] + Knapsack(n - 1, capacity - Weight[n])
        result = max(no, yes)

    return result


def Knapsack_dynamic(n, capacity):
    global mem

    if(n == -1 or capacity == 0):
        return 0
    
    if(n in mem and capacity in mem[n]):
        return mem[n][capacity]

    no = Knapsack_dynamic(n - 1, capacity)

    if(Weight[n] > capacity):
        result = no
    else:
        yes = Value[n] + Knapsack_dynamic(n - 1, capacity - Weight[n])
        result = max(no, yes)

    if(n not in mem):
        mem[n] = {}

    mem[n][capacity] = result

    return result


ks_dyn_points = [];
ks_points = [];

for ksTest in range(1000):

    Weight = []    # List of weights
    Value = []     # List of values

    for i in range (ksTest):
        Weight.append(random.randrange(1,101,1))
        Value.append(random.randrange(1,101,1))

    C = 100                     # Capacity

    mem = {}

    start_time = time.time()
    Knapsack_dynamic((ksTest - 1), C)
    elapsed_time = time.time() - start_time
    ks_dyn_points.append([ksTest, elapsed_time])

    start_time = time.time()
    Knapsack((ksTest - 1), C)
    elapsed_time = time.time() - start_time
    ks_points.append([ksTest, elapsed_time])

    print('-----',ksTest,'-----')
    print(ks_dyn_points)
    print(ks_points)

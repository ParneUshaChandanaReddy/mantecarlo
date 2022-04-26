
#    montecarlo.py - Using the MonteCarlo method in problem solving.
#    Copyright (C) 2011 Sakis Kasampalis <faif at dtek period gr> 

#  reference :  https://github.com/faif/montecarlo/blob/master/montecarlo.py#L1

import random, math, datetime
# pi problem parameters
N_POINTS = 2000                 # increase it to get a better pi approximation

# factory problem parameters
P_LEN = 38                      # total items/production
F_LEN = 9                       # maximum number of faulty chips/production
P_FAULTS = 7                   # faulty orders indicating a bad production
N_PRODUCTIONS = 200             # increase it to see how the probability of getting
                                # bad productions increases as the number of total 
                                # productions increases


# @param n the total number of random points to use

def calculate_pi(n):
    assert(n > 0)
    good = 0                    # indicates a good case
    for _ in range(n):
        x = random.random()     # [0.0 - 1.0)
        y = random.random()
        num1 = math.pow(x - 0.5, 2) # (x - 1/2) ^ 2
        num2 = math.pow(y - 0.5, 2)
      
        if num1 + num2 <= math.pow(0.5, 2):
            good += 1
    
    return 4 * (good / float(n))


# Calculates the probability of finding f orders of faulty

def ele_chips(f, t, c, n):
    assert(f > 0 and t > 0 and c > 0 and n > 0)
    bad = 0                    # indicates a bad case
    for _ in range(n):
        r = list()
        # generate a random production with c faulty chips
        while not count_production_faults(r, c):
            r = gen_rnd_production(t)
        # check if the production is faulty
        if f == faulty_orders(r):
            bad += 1
    return bad / float(n)


# Generates a random production.

def gen_rnd_production(n):
    return rnd_boollist(n)


# Counts the faulty chips found in a production.

def count_production_faults(r, c):
    return count_true_vals(r) == c


# Counts the number of True items found in a boolean 

def count_true_vals(c):
    i = 0
    for it in c:
        if it:
            i += 1
    return i


# Organizes the given container as pairs.

def pairs(c):
    for i in range(1, len(c)):
        yield c[i-1], c[i]
    yield c[-1], c[0]


# Counts the faulty orders 

def faulty_orders(c):
    i = 0
    for x1, x2 in pairs(c):
        # faulty order when the first item is True
        # and the second False
        if x1 and not x2:
            i += 1
    return i


# Generates a random boolean list.

def rnd_boollist(list_len):
    c = list()
    [c.append(random.choice([True, False])) for _ in range(list_len)]
    return c

# pi approximation
pi = calculate_pi(N_POINTS)
print('pi approximation using', N_POINTS, 'points:', pi)

# factory production problem
fe = ele_chips(P_FAULTS, P_LEN, F_LEN, N_PRODUCTIONS)
print('probability of getting', P_FAULTS, 'faulty orders in', N_PRODUCTIONS, 'productions:', fe)


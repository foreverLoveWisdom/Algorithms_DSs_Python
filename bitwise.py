# import uuid
import timeit

# Method 1:
# With
# O(n) runtime, n is the total no of bits.
# O(1) space complexity
num_bits = 0
# for i in bin(7):
#     if i == "1":
#         num_bits += 1
# print("Number of 1 bits: %s" %(num_bits))

# def parity(x):
#     print("\n x is: %s" %(x))
#     result = 0
#     while x:
#         result ^= 1
#         x &= x - 1
#     print("\nResult is: %s" %(result))

print(timeit.timeit('''
def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1

parity(111111111111111111111111111111111111111111111111111111111111111)'''
))

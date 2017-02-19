#Computing Statistics
import numpy as np
from statistics import mean


nums = []
while True:
    try:
        a = int(input("Enter a number.  A non number to quit."))
    except ValueError:
        break
    else:
        nums.append(a)

print(nums)
print(str(np.std(nums)) + " std. deviation")
print(str(mean(nums)) + " average")
#print(str(np.mean(nums) + " mean"))
print(str(min(nums)) + " minimum")
print(str(max(nums)) + " maximum")
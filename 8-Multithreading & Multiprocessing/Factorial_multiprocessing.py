import multiprocessing
import time
import sys
import math

sys.set_int_max_str_digits(100000)

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Dactorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,7000,8000]
    start_time=time.time()
    with multiprocessing.Pool() as Pool:
        results=Pool.map(compute_factorial,numbers)
        
    end_time=time.time()
    print(results)
    print(end_time-start_time)

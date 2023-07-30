import multiprocessing
import time
def task(num):
print(f"Task {num} started at {time.time()}")
time.sleep(2)
print(f"Task {num} finished at {time.time()}")
def square(x):
return x * x
if _name_ == '_main_':
start_time = time.time()
pool = multiprocessing.Pool()
pool = multiprocessing.Pool(processes=4)
inputs = [0,1,2,3,5]
outputs = pool.map(square, inputs)
print("Input: {}".format(inputs))
print("Output: {}".format(outputs))
end_time = time.time()
print(f"All tasks completed in {end_time - start_time} seconds")
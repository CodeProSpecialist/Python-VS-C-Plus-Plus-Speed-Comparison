import time

start = time.time()

for i in range(1, 1000000001):
    print(i)

end = time.time()
duration = end - start

print("Total time taken:", duration, "seconds")

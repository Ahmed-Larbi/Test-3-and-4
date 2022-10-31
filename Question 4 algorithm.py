import time
def findFactors(x):
   start = time.perf_counter()
   list =[]
   for i in range(1, x + 1):
       if x % i == 0:
           list.append(i)
   finish = time.perf_counter()
   print(f'test case took: { finish-start} seconds')
   return list

num = int(input('Enter the Product Number: ex. 127'))

listOfFactors = findFactors(num)
print("The factors are:")
print(listOfFactors[len(listOfFactors)-2], listOfFactors[len(listOfFactors)-3])
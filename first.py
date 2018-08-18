import random # Used to Generate Random Number

random_arr=[] # Creating an Empty Array
for x in range(1000000):  
  random_arr.append(random.randint(1,100)) # Appending Random Number Generate in range of (1,100) to the Array


count_arr=[0] * 100
for i in range(len(random_arr)):
  
  count_arr[random_arr[i] -1 ]=count_arr[random_arr[i] -1 ]+1

print (count_arr)

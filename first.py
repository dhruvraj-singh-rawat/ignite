import random # Used to Generate Random Number


# Creating an Random Array of Size 1M cointaing Elements between < 1 To 100 >
random_arr=[] 
for x in range(1000000):  
  random_arr.append(random.randint(1,100)) # Appending Random Number Generate in range of (1,100) to the Array


####
#   Main Algorithm : An array of Size 100 is initialized and as the random number comes the Count of that Index is Incremented

count_arr=[0] * 100
for i in range(len(random_arr)):
  
  count_arr[random_arr[i] -1 ]=count_arr[random_arr[i] -1 ]+1
####

# Printing the Solution
for i in range(100):
  print("Total Number of ", i+1, " are :",count_arr[i])


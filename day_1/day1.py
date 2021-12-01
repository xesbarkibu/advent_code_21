import numpy as np

input = open("day_1/input", "r")

input_list=[]
for line in input:
    input_list.append(int(line.rstrip()))
input.close()


arr = np.array(input_list)

# part 1
count = 0
for index, number in  enumerate(arr):
    if (arr[index:index+2].max()!=number): 
        count += 1
print (count)
   
# part 2
count = 0
for index, number in enumerate(arr):
    if ((arr[index:index+3].sum() - arr[index+1:index+4].sum())<0):
        count += 1 
print(count)


# part 1 one liner
print(len([x for i,x in enumerate(arr) if  x - arr[(i+1)%len(arr)]<0]))

# part 2 one liner
print(len([index for index in range(len(arr)) if((arr[index:index+3].sum() - arr[index+1:index+4].sum())<0) ]))



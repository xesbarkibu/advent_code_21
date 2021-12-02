forward = 'forward'
down = 'down'
up= 'up'

input = open("day_2/input", "r")
input_list=[]
for line in input:
    line_value = line.split(" ")
    input_list.append((line_value[0], int(line_value[1].rstrip())))
input.close()


# part 1
forward_amount=0
depth_amount = 0
for line in input_list:
    movement = line[0]
    amount = line[1]
    if movement==forward:
        forward_amount+=amount
    if movement==up:
        depth_amount-=amount
    if movement==down:
        depth_amount+=amount

print(forward_amount * depth_amount)


#part 2
aim = 0
depth_amount = 0
forward_amount = 0
for line in input_list:
    movement = line[0]
    amount = line[1]
    if movement==up:
        aim -= amount
    if movement==down:
        aim += amount
    if movement==forward:
        forward_amount += amount
        depth_amount += amount*aim
       
print(forward_amount*depth_amount)


# part 1 in one line:
print(sum([fwd[1] for fwd in input_list if fwd[0]==forward])*sum([depth[1] if depth[0]==down else -depth[1] for depth in input_list if depth[0]!=forward]))


# part 2 in one line:
print(sum([x[1] * sum(list(map(lambda x: -x[1] if x[0]==up else x[1] if x[0]==down else 0, input_list[:i]))) for i,x in enumerate(input_list)if x[0]==forward])*sum([fwd[1] for fwd in input_list if fwd[0]==forward]))



import collections


input = open("day_3/input", "r")

original_list=[]
for line in input:
    line_value = line.rstrip()
    original_list.append(line_value)
input.close()

def rotate_array(list_to_rotate):
    return [''.join(reversed(a)) for a in zip(*list_to_rotate)]


# part 1
rotated_array = rotate_array(original_list)
gamma = [collections.Counter(most_common).most_common()[0][0] for most_common in rotated_array ]
epsilon =  [collections.Counter(less_common).most_common()[-1][0] for less_common in rotated_array ]
print(int(''.join(gamma), 2)  *  int(''.join(epsilon), 2))


#part 2
o2='o2'
co2='co2'

def get_life_support(index, list, gas):
    rotated_array = rotate_array(list)
    counter = [collections.Counter(counted).most_common() for counted in rotated_array][index]
    if(len(counter)>1):
        more_common = [more_common_value[0] if counter[0][1]!=counter[1][1] else '1' for more_common_value in counter][0]
        less_common = [less_common_value[0] if counter[0][1]!=counter[1][1] else '0' for less_common_value in counter][-1]    
    else:
        more_common = less_common = counter[0][0]

    filtered_list = [filtered for filtered in list if filtered[index]== (more_common if gas ==o2 else less_common)]


    if(len(filtered_list)==1):
        return filtered_list
    else:
        return get_life_support(index+1, filtered_list, gas)


print(int(''.join(get_life_support(0, original_list,o2)), 2)  *  int(''.join(get_life_support(0, original_list,co2)), 2))


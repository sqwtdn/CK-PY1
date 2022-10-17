list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ind = 0
max_num = list_numbers[max_ind]

for ind in range(19):
    if list_numbers[max_ind] < list_numbers[ind]:
        max_ind = ind

list_numbers[max_ind], list_numbers[-1] = list_numbers[-1], list_numbers[max_ind]

print(list_numbers)
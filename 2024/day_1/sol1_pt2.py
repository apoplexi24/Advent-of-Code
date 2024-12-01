import pandas as pd

with open('input.txt', 'r') as txt_file:
    file_text = txt_file.readlines()

val1list = []
val2list = []
for element in file_text:
    line_val = element.split('   ')
    val1 = int(line_val[0])
    val2 = int(line_val[1].replace('/n', ''))
    val1list.append(val1)
    val2list.append(val2)

final = {}
result = 0

for val in val2list:
    if val in final.keys():
        final[val] += 1
    else:
        final[val] = 1

for val in val1list:
    if val in final.keys():
        result += val * final[val]

print(result)
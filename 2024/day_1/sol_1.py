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
    

val1list = sorted(val1list)
val2list = sorted(val2list)
df = pd.DataFrame(columns=['col1', 'col2'])

df['col1'] = tuple(val1list)
df['col2'] = tuple(val2list)

df['col3'] = abs(df['col1'] - df['col2'])

final = sum(df['col3'])

print(final)
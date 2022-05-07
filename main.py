import time
import pandas as pd
from tabulate import tabulate


data = [['Alex', 10], ['Bob', 12], ['Clarke', 13, 'Sofia'], ['George', 28]]

dic = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
name = 'Mario'
age = 8
city = 'Razlog'
headers = ['row', 'name', 'age', 'city']
new_member = [name, age, city]
data.append(new_member)

data[0].append('Plovdiv')

for i in data:
    if 'Bob' in i:
        i.append('Ruse')

df = pd.DataFrame.from_dict(dic)
# df = pd.DataFrame(data)
# print(df)

print(tabulate(df, headers=headers, tablefmt="simple", missingval="N/A"))

time.sleep(5)

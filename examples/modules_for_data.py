import pandas as pd
import csv

lst = []
with open('kku.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        lst.append(row)

df = pd.DataFrame(lst)
print(df)
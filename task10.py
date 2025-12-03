import pandas as pd

df = pd.read_csv('grades.csv')
df['Average'] = df.iloc[:, 1:].mean(axis=1)  
for index, row in df.iterrows():
    print(f"{row['Name']}'s average grade is {row['Average']:.2f}")
    
# Import package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read 2 Excel files
excelFile1 = pd.read_excel('file1.xlsx')
excelFile2 = pd.read_excel('file2.xlsx')

# Merge the 2 files 
merged_file = pd.concat([excelFile1, excelFile2], ignore_index=True)

# Write the merged file to a new Excel file
newFile = merged_file.to_excel('merged_file.xlsx', index=False)

# Read the new file
df = pd.read_excel('merged_file.xlsx')
print(df.head()) # preview first few rows
print()
print(df.info()) # view info about data
print()
print(df.drop_duplicates()) # drop duplicate data
print()

# Statistical analysis with rounding the number by 2 decimal place & export to Excel file
print(round(df.describe(),2))
print(df.describe().to_excel('analyzed_file.xlsx'))

# Plot the data on a graph
viz = sns.countplot(data=df, x='Age')
plt.title('Client by Age')
plt.show()
plt.clf()
plt.close()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns1
import seaborn as sns2

df = pd.read_csv('healthcare_dataset.csv')

bgt_by_gender = df.groupby(['Blood Group Type', 'Gender']).size().reset_index(name='BGCount')
mc_by_gender = df.groupby(['Medical Condition', 'Gender']).size().reset_index(name='MCCount')
average_cost_by_condition = df.groupby('Medical Condition')['Billing Amount'].mean().reset_index(name='AVGBill')

print(average_cost_by_condition)

plt.figure(num='Blood Group & Medical Condition', figsize=(18, 8))
sns1.barplot(x='Blood Group Type', y='BGCount', hue='Gender', data=bgt_by_gender,
             palette={'Male': 'blue', 'Female': 'pink'})
sns2.barplot(x='Medical Condition', y='MCCount', hue='Gender', data=mc_by_gender,
             palette={'Male': 'red', 'Female': 'orange'})

plt.title('Blood Group & Medical Condition Count by Gender')
plt.xlabel('Blood Group & Medical Condition')
plt.ylabel('Patients Count')
plt.show()

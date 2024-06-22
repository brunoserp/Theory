# https://hotmart.com/pt-BR/club/clube-de-assinaturas-da-universidade-dos-dados/products/2668372/content/R4jkmo8Wea?hashComment=x7WbpmAEe2
# https://pynative.com/python-matplotlib-exercise/

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os

df = pd.read_csv(r"C:\Users\bserpellone\Desktop\Python\Teoria\datasets\company_sales_data.csv")

'''
Colunas: ['month_number' 'facecream' 'facewash' 'toothpaste' 'bathingsoap' 'shampoo' 'moisturizer' 'total_units' 'total_profit']
'''

# Ex 3: Read all product sales data and show it  using a multiline plot
'''
plt.figure(figsize=[9,5])
for produto in df.iloc[:,1:-2].columns.values:
    plt.plot(df['month_number'],df[str(produto)],label=str(produto),marker='o',linewidth=2)
plt.legend(loc='upper left')
plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.xticks([mes for mes in range(len(df['month_number'])+1)])
plt.show()
'''

# Ex 4: Read toothpaste sales data of each month and show it using a scatter plot
'''plt.scatter(df['month_number'],df['toothpaste'],label='Tooth paste sales data')
plt.ylabel('Number of units sold')
plt.xlabel('Month number')
plt.xticks([mes for mes in range(len(df['month_number'])+1)])
plt.grid(color='gray',linestyle='--',alpha=0.8)
plt.show()'''

# Ex 5: Read face cream and facewash product sales data and show it using the bar chart
'''plt.bar(x=df['month_number']-0.2, height=df['facecream'], width=0.4, label="Face cream sales data")
plt.bar(x=df['month_number']+0.2, height=df['facewash'], width=0.4, label="Face wash sales data")
plt.title('Facewash and facecream sales data')
plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.legend()
plt.grid(linestyle='--')
plt.xticks([mes for mes in range(len(df['month_number'])+1)])
plt.show()'''

# Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
'''plt.bar(x=df['month_number'],height=df['bathingsoap'])
plt.title('bathingsoap sales data')
plt.xticks([mes for mes in range(len(df['month_number'])+1)])
plt.xlabel("Month number")
plt.ylabel("Sales units in number")
plt.grid(linestyle='--')
plt.show()'''

# Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
'''plt.hist(x=df['total_profit'])
plt.title('Profit data')
plt.ylabel('Actual profit in dollar')
plt.xlabel('profit range in dollar')
plt.legend(['Profit data'],loc='upper left')
plt.show()'''
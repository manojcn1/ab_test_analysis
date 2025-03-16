#!/usr/bin/env python
# coding: utf-8

# In[114]:


import pandas as pd
import os
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind

os.chdir("/Users/manoj/OneDrive/Documents/Manoj/Resume/Projects/AB Testing")
df = pd.read_csv("ab_testing_dataset.csv")


# In[20]:


df.head()


# In[21]:


df.info()


# In[22]:


df.describe()


# In[23]:


#Checking for null values
df.isna().sum()


# In[28]:


#Replacing the null values with 0
df.fillna(0,inplace=True)


# In[29]:


df.isna().sum()


# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[39]:


# Distribution of Impressions, Clicks, Conversions
sns.histplot(df['Clicks'], bins = 20, kde = True)
plt.title("Distribution of Clicks")
plt.show()


# In[40]:


sns.histplot(df['Impressions'], bins = 20, kde = True)
plt.title("Distribution of Impressions")
plt.show()


# In[41]:


sns.histplot(df['Revenue'], bins = 20, kde = True)
plt.title("Distribution of Revenue")
plt.show()


# In[58]:


# Distribution of Impressions, Clicks, Conversions
sns.histplot(df['Conversions'], bins = 20, kde = True)
plt.title("Distribution of Conversions")
plt.show()


# In[53]:


df.groupby('Group')[["Impressions","Clicks","Conversions","Revenue"]].mean()


# In[69]:


df['CTR'] = df['Clicks']/df['Impressions']


# In[55]:


df['Conv Rate'] = df['Conversions']/df['Clicks']


# In[56]:


df.head()


# In[57]:


df.groupby('Group')[["CTR","Conv Rate"]].mean()


# In[61]:


df['Conv Rate'].fillna(0, inplace=True)


# In[62]:


df.groupby('Group')[["CTR","Conv Rate"]].mean()


# In[63]:


df.isna().sum()


# In[131]:


#After trying a couple of solutions, changing Conv Rate to 0 when clicks are 0 worked with the NaN issue for CR
df['Conv Rate'] = np.where(df['Clicks']>0, df['Conversions']/df['Clicks'],0)


# In[70]:


df.groupby('Group')[["CTR","Conv Rate"]].mean()


# In[73]:


#Revenue per use
sns.boxplot(x=df['Group'], y=df['Revenue'])
plt.title("Revenue Distribution of A vs B")
plt.show()


# In[74]:


df.groupby('Group')['Revenue'].mean()


# In[77]:


df['Timestamp'] = pd.to_datetime(df['Timestamp'])


# In[80]:


df.set_index('Timestamp', inplace=True)


# In[94]:


df['Conversions'].resample('D').mean().plot(title="Daily Conversions Over Time")
plt.show()


# In[102]:


df.groupby('Group')[['Conversions','Revenue', 'CTR', 'Conv Rate']].mean()


# In[107]:


#Hypothesis Testing: This is the most important part of the project
conversion_table = pd.crosstab(df['Group'], df['Conversions'])
conversion_table


# In[110]:


#Run chi-2 test for conversions
chi2, p, dof, expected = chi2_contingency(conversion_table)
print(f"The value of p is {p}")


# In[113]:


###The value of p is <<<0.05. So the test is statistically significant. Let's conduct t-test for revenue


# In[123]:


t_stat, p_value = ttest_ind(df[df['Group'] == 'A']['Revenue'], df[df['Group']=='B',['Revenue'], nan_policy='omit')


# In[118]:


t_stat, p_value = ttest_ind(df[df['Group'] == 'A']['Revenue'], df[df['Group'] == 'B']['Revenue'], nan_policy='omit')


# In[124]:


print(f"p value is {p}")


# In[134]:


# Compute Lift in Conversion Rate
cr_A = df[df['Group'] == 'A']['Conv Rate'].mean()
cr_B = df[df['Group'] == 'B']['Conv Rate'].mean()
lift = ((cr_B - cr_A) / cr_A) * 100

print(f"Conversion Rate Lift: {lift:.2f}%")


# In[135]:


sns.barplot(x=df['Group'], y=df['Conv Rate'])
plt.title("Conversion Rate Comparison (A vs B)")
plt.show()


# In[136]:


sns.boxplot(x=df['Group'], y=df['Revenue'])
plt.title("Revenue Distribution of A vs B")
plt.show()


# In[ ]:





# -*- coding: utf-8 -*-
"""p3Analyze.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x2G5L6rZQVZLt6zfry56wtC2ZvKQpcyX
"""

#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")

data=pd.read_csv("data.csv")

data.head()

data.dtypes

#product names
data["product_name"].value_counts()

#details of products
plt.figure(figsize=(20,8))
sns.set_style("darkgrid")
sns.set_palette("Set2")
plt.xticks(rotation=90,fontsize=12)
plt.yticks(fontsize=12)
sns.countplot("product_name",data=data,label="Product Details")
plt.xlabel("Product Name",fontsize=12)
plt.legend()
plt.show()

data["product_category"].value_counts()

# product category
plt.figure(figsize=(10,4))
sns.set_style("darkgrid")
sns.set_palette("Set2")
plt.xticks(rotation=90,fontsize=12)
plt.yticks(fontsize=12)
sns.countplot("product_category",data=data,label="Category")
plt.xlabel("Product Category",fontsize=12)
plt.legend()
plt.show()

#payment types
plt.pie(list(ankit_data["payment_type"].value_counts()),labels=list(data["payment_type"].value_counts().keys()),autopct="%.1f%%",shadow=True,radius=2)
plt.pie([1],colors=["w"],radius=1)
plt.show()

#countries wrt product type
plt.figure(figsize=(20,8))
sns.set_style("darkgrid")
sns.set_palette("Set2")
plt.xticks(rotation=90,fontsize=12)
plt.yticks(fontsize=12)
sns.countplot("country",data=data,hue="product_category")
plt.show()

# cities wrt to product type
plt.figure(figsize=(20,8))
sns.set_style("darkgrid")
sns.set_palette("Set2")
plt.xticks(rotation=90,fontsize=12)
plt.yticks(fontsize=12)
sns.countplot("city",data=data,hue="product_category")
plt.show()

#failure reasons
plt.figure(figsize=(18,7))
sns.set_style("whitegrid")
sns.set_palette("Set2")
#plt.xticks(rotation=90)
#sns.countplot("failure_reason",data=data)
sns.countplot("failure_reason",data=data,order=data["failure_reason"].value_counts().index[:7])
print(plt.show())

#-------------payment_type----------------------
plt.figure(figsize=(15,7))
sns.set_style("whitegrid")
sns.set_palette("Set2")
sns.countplot("payment_type",data=data)
plt.show()
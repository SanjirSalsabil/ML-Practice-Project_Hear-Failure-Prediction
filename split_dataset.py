#import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import dataset

dataset= pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(dataset)
#print(dataset.info())
#print(dataset.describe())

#import train_test library
from sklearn.model_selection import train_test_split
train, test= train_test_split(dataset, test_size=0.2, random_state=42, shuffle=True)
# what is random_state ,shuffle 


# train.drop(train.columns[0], axis=1, inplace= True)
# train.info()

# test.drop(test.columns[0], axis=1, inplace= True)
# test.info()

print("==============train data ===================")
print(train.head())
print("===============test data =======================")
print(test.head())
train.to_csv("heart_train.csv")
test.to_csv("heart_test.csv")


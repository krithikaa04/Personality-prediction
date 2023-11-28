import pickle

import numpy as np
import pandas as pd
from sklearn import linear_model

# Loading Dataset Globally
data = pd.read_csv("dataset.csv")
array = data.values


df = pd.DataFrame(array)

maindf = df[[0, 1, 2, 3, 4]]
mainarray = maindf.values

temp = df[5]
train_y = temp.values

for i in range(len(train_y)):
    train_y[i] = str(train_y[i])

mul_lr = linear_model.LogisticRegression(
    multi_class="multinomial", solver="newton-cg", max_iter=1000
)

# Fit the model
multi_log_reg = mul_lr.fit(mainarray, train_y)

# Save the model to a pickle file
with open('multiNomialLogisticRegression.pkl', 'wb') as file:
    pickle.dump(mul_lr, file)
import json
import numpy as np
import os
import pickle
import joblib

model_path = "./outputs/clf.pkl"

model = joblib.load(model_path)

data = ["mele" , 4]

x = np.array([1 if data[0] == "female" else 0 , data[1] ])
x = x.reshape(1, -1)

y_hat = model.predict_proba(x)

print(y_hat)
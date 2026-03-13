import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
#load dataset

data = pd.read_csv("network_dataset.csv")
# simple feature
X = data[["len"]]
y = [0]*len(data)      # dummy label (normal traffic)
# train model
model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, "network_model.pkl")
print("Model trained and saved successfully")


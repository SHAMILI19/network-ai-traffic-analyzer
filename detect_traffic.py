import pandas as pd
import joblib
model = joblib.load("network_model.pkl")
data = pd.read_csv("network_dataset.csv")
X = data[["len"]]
predictions = model.predict(X)
print("Traffic Analysis Result:")
print(predictions[:20])


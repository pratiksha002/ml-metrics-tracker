from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import pickle

def train_model():
    data = {
        "feature": [1, 2, 3, 4, 5, 6],
        "target": [10, 20, 30, 40, 50, 60]
    }


    df = pd.DataFrame(data)

    x = df[["feature"]]
    y = df["target"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    with open("model/model_v1.pkl", "wb") as f:
        pickle.dump(model, f)

    return y_test.tolist(), y_pred.tolist()
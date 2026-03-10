import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn import metrics
from xgboost import XGBRegressor


# =========================
# Load Dataset
# =========================

calories = pd.read_csv("dataset/calories.csv")
exercise = pd.read_csv("dataset/exercise.csv")

data = pd.concat([exercise, calories["Calories"]], axis=1)


# =========================
# Data Preprocessing
# =========================

data.replace({"Gender": {"male": 0, "female": 1}}, inplace=True)

X = data.drop(columns=["User_ID", "Calories"], axis=1)
Y = data["Calories"]


# =========================
# Train Test Split
# =========================

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=2
)


# =========================
# Model Training
# =========================

model = XGBRegressor()

model.fit(X_train, Y_train)


# =========================
# Evaluation
# =========================

predictions = model.predict(X_test)

mae = metrics.mean_absolute_error(Y_test, predictions)

print("Mean Absolute Error:", mae)


# =========================
# Save Model
# =========================

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
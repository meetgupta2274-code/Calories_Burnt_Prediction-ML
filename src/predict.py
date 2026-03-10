import numpy as np
import pickle


model = pickle.load(open("models/model.pkl", "rb"))

# Example input
# Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp

input_data = [0, 25, 180, 75, 30, 120, 40]

input_array = np.asarray(input_data).reshape(1, -1)

prediction = model.predict(input_array)

print("Predicted Calories Burnt:", prediction[0])
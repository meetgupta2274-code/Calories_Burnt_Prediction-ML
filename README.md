# 🔥 Calories Burnt Prediction using Machine Learning

This project builds a **Machine Learning model that predicts the number of calories burned during physical exercise** based on physiological and workout-related parameters.

The model is trained using an **exercise and calorie dataset** and deployed as an **interactive web application using Streamlit**.

Users can input exercise details such as **age, weight, duration, heart rate, and body temperature** to estimate the calories burned.

---

# 📊 Dataset

The dataset used in this project contains information related to **exercise activities and calorie consumption**.

### Dataset Details

* **Dataset Files:**

  * `exercise.csv`
  * `calories.csv`

* **Features Used**

| Feature          | Description                      |
| ---------------- | -------------------------------- |
| Gender           | Male / Female                    |
| Age              | Age of the person                |
| Height           | Height in cm                     |
| Weight           | Weight in kg                     |
| Duration         | Exercise duration in minutes     |
| Heart Rate       | Heart rate during exercise       |
| Body Temperature | Body temperature during exercise |

### Target Variable

| Column   | Description                     |
| -------- | ------------------------------- |
| Calories | Calories burned during exercise |

The datasets are merged to create the final dataset used for training.

---

# 🧠 Machine Learning Model

The regression model used in this project is:

**XGBoost Regressor**

XGBoost is a powerful **gradient boosting algorithm** widely used in machine learning competitions and real-world ML systems.

### Model Evaluation

The performance of the model is evaluated using:

**Mean Absolute Error (MAE)**

This metric measures the average absolute difference between predicted and actual calorie values.

---

# ⚙️ Technologies Used

The project is implemented using the following technologies:

* Python
* NumPy
* Pandas
* Scikit-Learn
* XGBoost
* Matplotlib
* Seaborn
* Streamlit

---

# 📁 Project Structure

```
calories-burnt-prediction-ml
│
├── dataset
│   ├── calories.csv
│   └── exercise.csv
│
├── models
│   └── model.pkl
│
├── src
│   ├── train_model.py
│   ├── predict.py
│   └── app.py
│
├── notebook
│   └── Calories_Burnt_Prediction_ML.ipynb
│
├── screenshots
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/meetgupta2274-code/Calories_Burnt_Prediction-ML.git

cd calories-burnt-prediction-ml
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv myenv
```

Activate the environment

Windows:

```
myenv\Scripts\activate
```

Mac/Linux:

```
source myenv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Train the Model

```
python src/train_model.py
```

This will generate the trained model file:

```
models/model.pkl
```

---

### 5️⃣ Run the Web Application

```
streamlit run src/app.py
```

The application will start at:

```
http://localhost:8501
```

---

# 🖥️ Web Application

The **Streamlit web application** allows users to input exercise details and receive an instant prediction of calories burned.

Users can enter:

* Gender
* Age
* Height
* Weight
* Exercise Duration
* Heart Rate
* Body Temperature

The system then predicts the **estimated calories burned during the workout**.

---

# 📈 Future Improvements

Possible improvements for this project include:

* Hyperparameter tuning for improved accuracy
* Adding advanced regression models
* Deploying the application online
* Adding data visualization dashboards
* Integrating real-time fitness tracking data

---

# 👨‍💻 Author

**Meet Gupta**

B.Tech Artificial Intelligence & Machine Learning
Honors in Data Science

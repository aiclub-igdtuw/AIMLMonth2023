 # 📊 Body Fat Prediction using Machine Learning

A machine learning project focused on analyzing body composition data and predicting body fat percentage using **Exploratory Data Analysis (EDA), Feature Engineering, and Linear Regression**.

The project explores relationships between body measurements such as age, weight, height, abdomen, chest, hip, and other circumference measurements to understand and estimate body fat percentage.

## 📌 Project Overview

Body fat percentage is an important measure of body composition. This project uses a dataset containing body measurements to explore patterns and develop regression models for estimating body fat percentage.

The project is divided into two major tasks:

1. **Exploratory Data Analysis (EDA):** Investigating the dataset, identifying missing values, analyzing distributions, detecting outliers, and understanding correlations between body measurements.
2. **Machine Learning (Regression):** Performing feature engineering, splitting the dataset, training Linear Regression models, evaluating prediction errors, and comparing actual and predicted values.

## ✨ Features

- **Data Exploration:** Analyzes body composition and measurement data.
- **Data Cleaning:** Checks for missing values and duplicate records.
- **Data Visualization:** Uses histograms, box plots, and scatter plots.
- **Correlation Analysis:** Identifies relationships between body measurements and body fat percentage.
- **Feature Engineering:** Calculates BMI and explores an additional Navy-based body fat estimate.
- **Regression Modeling:** Implements Linear Regression.
- **Model Evaluation:** Uses Mean Absolute Error (MAE) to evaluate predictions.
- **Prediction Visualization:** Compares actual and predicted values using scatter plots.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning and model evaluation |
| Jupyter Notebook | Development environment |
| Google Colab | Cloud-based notebook execution |

## 📂 Dataset Description

The project uses a body fat dataset containing **252 records and 15 original attributes**.

The dataset includes body composition information and various physical measurements.

### Dataset Features

| Feature | Description |
|---|---|
| Density | Body density |
| BodyFat | Body fat percentage |
| Age | Age of the individual |
| Weight | Body weight |
| Height | Height of the individual |
| Neck | Neck circumference |
| Chest | Chest circumference |
| Abdomen | Abdomen circumference |
| Hip | Hip circumference |
| Thigh | Thigh circumference |
| Knee | Knee circumference |
| Ankle | Ankle circumference |
| Biceps | Biceps circumference |
| Forearm | Forearm circumference |
| Wrist | Wrist circumference |

## 🔍 Task 1 – Exploratory Data Analysis (EDA)

The first part of the project focuses on understanding the dataset and identifying important patterns.

### 1. Data Quality Analysis
- Checked for missing values.
- Identified duplicate records.
- Observed that the dataset contained no missing values or duplicate instances.

### 2. Distribution Analysis
- Visualized body fat percentage using histograms.
- Used box plots to examine body measurements.
- Investigated outliers and extreme values.

### 3. Correlation Analysis
- Calculated correlations between body fat percentage and physical measurements.
- Identified abdomen, chest, hip, weight, and other measurements as potentially significant predictors.
- Observed a strong positive relationship between body fat percentage and abdomen circumference.

### 4. Feature Scaling
- Applied StandardScaler to numerical features.
- Explored standardization to bring measurements with different scales onto a comparable scale.

### 5. Relationship Visualization
- Created scatter plots to examine the relationship between body fat percentage and individual body measurements.
- Observed positive relationships between body fat percentage, weight, and abdomen circumference.

## 🤖 Task 2 – Machine Learning and Regression

The second part focuses on developing regression models to estimate body fat percentage.

### 1. Data Preprocessing
- Loaded the dataset using Pandas.
- Separated input features and target variables.
- Prepared the data for regression modeling.

### 2. Feature Engineering

Two additional features or estimates were explored:

- **BMI (Body Mass Index):** Calculated using weight and height.
- **NavyFat:** An additional body fat estimate calculated using a Navy-based formula involving body measurements.

### 3. Train-Test Split

The dataset was divided into training and testing sets using an 80:20 split.

| Dataset | Records |
|---|---:|
| Training | 201 |
| Testing | 51 |
| Total | 252 |

The split uses `random_state=42` for reproducibility.

### 4. Model Selection and Training

**Linear Regression** was selected for predicting body fat percentage.

Two regression experiments were conducted:

- Model 1: Predicting the actual `BodyFat` target.
- Model 2: Predicting the engineered `NavyFat` target.

### 5. Model Evaluation

Mean Absolute Error (MAE) was used to measure the difference between actual and predicted values.

The reported results are:

| Regression Experiment | MAE |
|---|---:|
| Linear Regression – BodyFat | 3.33 |
| Linear Regression – NavyFat | 0.35 |

**Note:** The NavyFat result is reproduced from the notebook's implementation and should not be interpreted as a validated body fat prediction result. The formula's height-unit handling needs correction and validation before this result can be meaningfully compared.

### 6. Prediction Visualization

Scatter plots were generated to compare actual and predicted values against different body measurements, including:

- Abdomen
- Biceps
- Neck
- Hip

These visualizations help examine how closely the regression model follows the observed values.

## 📁 Project Structure

```text
Body-Fat-Prediction/
│
├── Untitled0.ipynb       # EDA and ML implementation
├── bodyfat.csv           # Dataset
└── README.md             # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ek-kudi/body-fat-prediction.git

cd body-fat-prediction
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 3. Add the Dataset

Place `bodyfat.csv` in the project directory.

### 4. Run the Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open `Untitled0.ipynb` and execute the cells sequentially.

Alternatively, upload the notebook and dataset to Google Colab.

## 🔮 Future Improvements

- Experiment with additional regression algorithms such as Random Forest, Decision Tree, and Gradient Boosting.
- Perform hyperparameter tuning to improve model performance.
- Add R² score, RMSE, and other regression evaluation metrics.
- Improve feature selection and investigate multicollinearity.
- Validate and correct the Navy-based body fat estimation formula.
- Implement a user-friendly interface for entering body measurements and generating predictions.
- Deploy the model as a simple web application.

## ⚠️ Disclaimer

This project is developed for educational and learning purposes. The predictions are experimental estimates based on the available dataset and should not be considered medical assessments or substitutes for professional health evaluations.

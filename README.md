# Final-Project-Stroke
A Final Project for Purwadhika Data Scientist Course

This Repository is about exploring and predicting Stroke Probability. The dataset used in this project can be found here
https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

The dataset consist of 10 input variables based on personal data and 1 output variable.

The input variables are:

1) gender: "Male", "Female" or "Other"
2) age: age of the patient
3) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
4) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
5) ever_married: "No" or "Yes"
6) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
7) Residence_type: "Rural" or "Urban"
8) avg_glucose_level: average glucose level in blood
9) bmi: body mass index
10) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
*Note: "Unknown" in smoking_status means that the information is unavailable for this patient

The steps that I took for this predictions were:

Exploratory data analysis
Preprocessing. Which mainly about handling missing values
Model selections. The models used are Logistic Regression, DecisionTreeClassifier, and KNNeighbors
Deployment with flask.
The best model evaluation is Logistic Regression.
Robust Scaling nor Polynomial does any improvement to the model

I did Hyperparameter tunning, with result as the following:

{'C': 0.1, 'solver': Newton-cg}

The tunning results improved the model to Recall Score of 0.88

![Screenshot](2021-04-13_020630.png)
![Screenshot](2021-04-13_020858.png)
![Screenshot](2021-04-13_020940.png)
![Screenshot](2021-04-13_021010.png)
![Screenshot](2021-04-13_021040.png)
![Screenshot](2021-04-13_021110.png)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
#feature engineering
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from imblearn.pipeline import Pipeline
from category_encoders import BinaryEncoder
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, RobustScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler, NearMiss
#evaluation
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedKFold
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score, accuracy_score, classification_report, plot_precision_recall_curve, plot_roc_curve
#saving models
import pickle

df = pd.read_csv(r'C:\Users\Shinjiriki\Purwadhika Code Jupyter\Project\Stroke\Dashboard Trial\stroke_data.csv') #Pathing baru jalan kalau begini

df.drop(df.loc[df['gender']=='Other'].index, inplace=True)
x = df.drop(['stroke','id'], axis = 1)
y = df['stroke']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, stratify = y, random_state = 2021)

logreg = LogisticRegression(solver = 'liblinear', random_state=2021)

one_hot = OneHotEncoder(drop = 'first')
binary = BinaryEncoder()
imputer_mean = SimpleImputer(strategy = 'mean')
impute = Pipeline([
    ('Simple Imputer',SimpleImputer(strategy = 'mean'))
])
transformer_mean = ColumnTransformer([
    ('One Hot', one_hot, ['gender','ever_married','Residence_type']),
    ('Binary', binary, ['work_type','smoking_status']),
    ('Simple Imputer', impute, ['bmi','avg_glucose_level'])
], remainder = 'passthrough')

randomover = RandomOverSampler(random_state = 2021)
estimator = Pipeline([
    ('preprocess', transformer_mean),
    ('balancing', randomover),
    ('model', logreg)
])

hyperparam_space =[{
    'model__solver':['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'], 
    'model__C' : [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
]

skfold = StratifiedKFold(n_splits = 5)
grid_search = GridSearchCV(estimator, param_grid = hyperparam_space, cv = skfold, scoring = 'recall', n_jobs = -1)

grid_search.fit(x_train, y_train)

grid_search.best_estimator_.fit(x, y)
file_name = 'Model Final.sav'
pickle.dump(grid_search.best_estimator_, open(file_name,'wb'))
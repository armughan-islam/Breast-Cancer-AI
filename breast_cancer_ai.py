import pandas as pd
import matplotlib.pyplot as plt

from google.colab import files
files.upload()
df = pd.read_csv('breast_cancer_data.csv')

df.head()

df.drop(columns=['id','Unnamed: 32'],axis=1,inplace=True)

df.head()

df['diagnosis']=df['diagnosis'].map({'M':1, 'B':0})

df.columns

mean_features = list(df.columns[1:11])
se_features = list(df.columns[11:21])
worst_features = list(df.columns[21:31])

mean_features.append('diagnosis')
se_features.append('diagnosis')
worst_features.append('diagnosis')

mean_features

df[mean_features].corr()

prediction_vars = ['radius_mean','perimeter_mean','area_mean','compactness_mean','concavity_mean','concave points_mean',
                   'radius_se','perimeter_se','area_se',
                   'radius_worst','perimeter_worst','area_worst','compactness_worst','concavity_worst','concave points_worst']

# Training the model

from sklearn.model_selection import train_test_split

X = df[prediction_vars]
y = df['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=1)

from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

model = RandomForestClassifier()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

predictions

y_test.values

from sklearn.metrics import confusion_matrix, accuracy_score
confusion_matrix(y_test,predictions)

accuracy_score(y_test,predictions)

# Grid Search

from sklearn.model_selection import GridSearchCV
parameters = {'max_depth': (1,2,3,4),'n_estimators': (10,50,100,500)}
grid = GridSearchCV(model,parameters)
grid.fit(X_train,y_train)
grid.best_params_

predictions = grid.predict(X_test)

confusion_matrix(y_test,predictions)

accuracy_score(y_test,predictions)


from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import pandas as pd

#Load the dataset
diabetes = datasets.load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)  
y = pd.Series(diabetes.target)

#Split dataset in training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Run a linear regression model
model = linear_model.LinearRegression()

#Train the model
model.fit(X_train, y_train)

#Make predictions
y_pred = model.predict(X_test)

# Print predictions
print("Predictions:", y_pred)


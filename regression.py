from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Load the dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

#Split dataset in training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes_X, diabetes_y, test_size=0.2, random_state=42)

#Run a linear regression model
model = LinearRegression()

#Train the model
model.fit(X_train, y_train)

#Make predictions
y_pred = model.predict(X_test)

# Print predictions
print(y_pred)


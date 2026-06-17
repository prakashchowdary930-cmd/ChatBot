import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target


# Convert dataset to DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = y

print("First 5 Rows of Dataset:\n")
print(df.head())


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Apply feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Create and train KNN model
model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)


# Make predictions
predictions = model.predict(X_test)


# Model evaluation
print("\nAccuracy Score:")
print(accuracy_score(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# Take user input
print("\nEnter Flower Measurements")

sepal_length = float(input("Sepal Length: "))
sepal_width = float(input("Sepal Width: "))
petal_length = float(input("Petal Length: "))
petal_width = float(input("Petal Width: "))


# Create new flower data
new_flower = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]


# Apply scaling
new_flower_scaled = scaler.transform(new_flower)


# Predict flower species
prediction = model.predict(new_flower_scaled)

flower_name = iris.target_names[prediction[0]]


# Display result
print("\nPredicted Flower Species:")
print(flower_name)

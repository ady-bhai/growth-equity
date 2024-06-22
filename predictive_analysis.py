import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('company_data.csv')

# Prepare the data
X = df[['Revenue', 'Employee Count']]
y = df['Valuation']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Visualize the results
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Valuations")
plt.ylabel("Predicted Valuations")
plt.title("Actual vs Predicted Valuations")
plt.show()

# Print model coefficients
print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")

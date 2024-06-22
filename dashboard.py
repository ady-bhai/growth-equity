import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('company_data.csv')

# Sidebar for user input
st.sidebar.header("User Input Parameters")

def user_input_features():
    revenue = st.sidebar.number_input("Revenue", min_value=0, max_value=1000000, value=500000)
    employee_count = st.sidebar.number_input("Employee Count", min_value=0, max_value=10000, value=1000)
    data = {'Revenue': revenue,
            'Employee Count': employee_count}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display the data
st.write("## Company Data")
st.write(df)

# Prepare the data
X = df[['Revenue', 'Employee Count']]
y = df['Valuation']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict based on user input
prediction = model.predict(input_df)

# Display the prediction
st.write("## Prediction")
st.write(f"Predicted Valuation: ${prediction[0]:.2f}")

# Visualization
st.write("## Actual vs Predicted Valuations")

# Make predictions
y_pred = model.predict(X_test)

# Plot the results
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.set_xlabel("Actual Valuations")
ax.set_ylabel("Predicted Valuations")
ax.set_title("Actual vs Predicted Valuations")
st.pyplot(fig)

# Run Streamlit app
if __name__ == "__main__":
    st.title("Growth Equity Analysis Dashboard")
    st.sidebar.header("Settings")

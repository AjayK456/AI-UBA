# alert_generator.py

import pandas as pd

# Step 1: Load the predicted results
predictions = pd.read_csv("predicted_results.csv")

# Step 2: Preview the data
print("Data Preview:")
print(predictions.head())

# Step 3: Set the alert condition
# Correct column name is 'predicted_malicious', not 'prediction'
alerts = predictions[predictions['predicted_malicious'] == True]

# Step 4: Display the alerts
print(" Suspicious Activities Detected:")
print(alerts)

# Step 5: Save the alerts separately
alerts.to_csv("alerts.csv", index=False)
print(" Alerts saved to 'alerts.csv'.")

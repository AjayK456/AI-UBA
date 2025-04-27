import pandas as pd
import joblib
from feature_engineering import preprocess_data

# Load the raw CSV
new_data = pd.read_csv("new_user_data_test.csv")

# Preprocess the data to generate new features
processed_data = preprocess_data(new_data)

# Load your trained model
model = joblib.load("uba_model.pkl")

# Extract only the features used in training
X_new = processed_data[['login_duration_minutes', 'is_using_vpn', 'suspicion_score']]

# Make predictions
predictions = model.predict(X_new)

# Add predictions to the DataFrame and print
processed_data['predicted_label'] = predictions
print(processed_data[['user_id', 'login_time', 'predicted_label']])

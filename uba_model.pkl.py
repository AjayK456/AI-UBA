import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from feature_engineering import preprocess_data

# Load and preprocess the dataset
df = pd.read_csv("enhanced_data_with_vpn.csv")
df = preprocess_data(df)  # Don't overwrite this!

# Define input features and target
features = ['login_duration_minutes', 'is_using_vpn', 'suspicion_score']
X = df[features]
y = df['is_malicious']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(clf, 'uba_model.pkl')
print(" Model trained and saved as uba_model.pkl")


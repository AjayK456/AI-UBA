import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Step 1: Load the dataset
df = pd.read_csv("enhanced_data_with_vpn.csv")

# Step 2: Convert time columns to datetime
df['login_time'] = pd.to_datetime(df['login_time'])
df['logout_time'] = pd.to_datetime(df['logout_time'])

# Step 3: Feature Engineering
df['hour_of_day'] = df['login_time'].dt.hour
df['file_count'] = df['files_accessed'].apply(lambda x: len(eval(x)) if isinstance(x, str) else 0)

# Step 4: Define features (X) and label (y)
X = df[['hour_of_day', 'login_duration_minutes', 'file_count', 'is_using_vpn', 'suspicion_score']]
y = df['is_malicious']

# Step 5: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
print("\n Model Evaluation Report:\n")
print(classification_report(y_test, y_pred))

# Step 8: Visualize Suspicion Score Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['suspicion_score'], kde=True, color='orange')
plt.title('Suspicion Score Distribution')
plt.xlabel('Suspicion Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

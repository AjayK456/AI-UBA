import pandas as pd
import os

# ✅ Hard-coded correct path with raw string to avoid escape issues
input_file = r"C:\Users\kulan\Desktop\Ajay\Projects\AI - UBA\predicted_results.csv"

output_file = r"C:\Users\kulan\Desktop\Ajay\Projects\AI - UBA\malicious_alerts.csv"

# ✅ Read the predicted results
df = pd.read_csv(input_file)

# ✅ Filter the malicious entries
malicious_df = df[df['predicted_malicious'] == True]

# ✅ Save to CSV
malicious_df.to_csv(output_file, index=False)
print(f" ALERT: Malicious entries saved to:\n{output_file}")

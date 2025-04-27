import pandas as pd

# Load new raw user data
df = pd.read_csv("enhanced_data_with_vpn.csv")

# Convert login and logout time to datetime
df['login_time'] = pd.to_datetime(df['login_time'])
df['logout_time'] = pd.to_datetime(df['logout_time'])

# Calculate session duration
df['login_duration_minutes'] = (df['logout_time'] - df['login_time']).dt.total_seconds() / 60

# Simple VPN detection (fake rule for demo)
vpn_ips = ['10.0.0.1', '172.16.0.9']
df['is_using_vpn'] = df['ip_address'].isin(vpn_ips)

# Suspicion scoring (custom rule-based logic)
df['suspicion_score'] = 0
df.loc[df['login_duration_minutes'] > 180, 'suspicion_score'] += 4
df.loc[df['is_using_vpn'], 'suspicion_score'] += 3
df.loc[df['location'] == 'Delhi', 'suspicion_score'] += 2
df.loc[df['device_id'] == 'DEVICE_C', 'suspicion_score'] += 2
df['suspicion_score'] = df['suspicion_score'].clip(upper=10)

# Save updated file for prediction
df.to_csv("enhanced_new_user_data.csv", index=False)
print(" enhanced_new_user_data.csv created with required features.")

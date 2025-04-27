import pandas as pd
from datetime import datetime, timedelta
import random

def simulate_user_logins(num_entries=100):
    users = ['U001', 'U002', 'U003']
    normal_locations = ['New York', 'London', 'Delhi']
    foreign_locations = ['Russia', 'Brazil']
    devices = ['DEVICE_A', 'DEVICE_B', 'DEVICE_C']
    unknown_device = 'UNKNOWN_DEVICE'
    ips = ['192.168.1.5', '10.0.0.1', '172.16.0.9', '222.45.67.89']
    files = ['report.docx', 'finance.xlsx', 'client_data.csv', 'salary_info.pdf', 'presentation.pptx',
             'confidential_notes.docx', 'source_code.py', 'contracts.pdf']

    data = []
    for _ in range(num_entries):
        is_malicious = random.random() < 0.1  # 10% chance

        user = random.choice(users)

        # VPN status
        is_using_vpn = random.random() < (0.7 if is_malicious else 0.1)  # 70% chance if malicious

        if is_malicious:
            login_hour = random.randint(0, 5)
            accessed_files = random.sample(files, random.randint(5, 8))
            location = random.choice(foreign_locations)
            device = unknown_device
            login_time = datetime(2025, 4, 1, login_hour, random.randint(0, 59))
            logout_time = login_time + timedelta(minutes=random.randint(5, 15))  # Short session
        else:
            login_hour = random.randint(8, 19)
            accessed_files = random.sample(files[:5], random.randint(1, 3))
            location = random.choice(normal_locations)
            device = random.choice(devices)
            login_time = datetime(2025, 4, 1, login_hour, random.randint(0, 59))
            logout_time = login_time + timedelta(hours=random.randint(1, 5))

        # Compute duration
        login_duration = (logout_time - login_time).total_seconds() / 60

        # Suspicion scoring
        suspicion_score = 0
        if login_hour < 6 or login_hour > 22:
            suspicion_score += 2
        if location in foreign_locations:
            suspicion_score += 2
        if is_using_vpn:
            suspicion_score += 3
        if login_duration < 10:
            suspicion_score += 1
        if len(accessed_files) > 5:
            suspicion_score += 2
        if device == unknown_device:
            suspicion_score += 2

        entry = {
            "user_id": user,
            "login_time": login_time.strftime('%Y-%m-%d %H:%M:%S'),
            "logout_time": logout_time.strftime('%Y-%m-%d %H:%M:%S'),
            "ip_address": random.choice(ips),
            "files_accessed": accessed_files,
            "location": location,
            "device_id": device,
            "is_using_vpn": is_using_vpn,
            "login_duration_minutes": round(login_duration, 2),
            "suspicion_score": suspicion_score,
            "is_malicious": is_malicious
        }

        data.append(entry)

    df = pd.DataFrame(data)
    df.to_csv('enhanced_data_with_vpn.csv', index=False)
    print(" enhanced_data_with_vpn.csv created with VPN + suspicion scoring!")

simulate_user_logins()
import pandas as pd

df = pd.read_csv("enhanced_data_with_vpn.csv")

print(df.head())            # View top 5 rows
print(df.columns)           # See column names
print(df.dtypes)            # Check data types
print(df['suspicion_score'].describe())  # See score distribution

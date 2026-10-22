# Lab 003 - Python Security Log Analyzer

import csv

from pathlib import Path

print("=== Security Log Analyzer ===")

with open(Path(__file__).parent / "security_logs.csv", "r") as file:
    reader = csv.DictReader(file)
    login_attempts = []

    failed_users = {}

    for row in reader:
        login_attempts.append(row["status"])

        if row["status"] == "FAILED":
            username = row["username"]
            failed_users[username] = failed_users.get(username, 0) + 1

failed_logins = login_attempts.count ("FAILED")
alert_threshold = 5

print("Total Login Attempts :", len(login_attempts))
print("Failed Login Attempts :", failed_logins)
print("Failed Logins by User:", failed_users)

alert_found = False

for username, count in failed_users.items():
    if count >= alert_threshold:
        print(f"ALERT: {username} has {count} failed login attempts!")
        alert_found = True

if not alert_found:
    print("No suspicious activity detected.")

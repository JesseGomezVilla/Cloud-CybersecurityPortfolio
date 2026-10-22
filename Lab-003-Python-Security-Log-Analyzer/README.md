# Lab 003 — Python Security Log Analyzer

## Objective
Develop a Python-based security log analyzer that identifies repeated failed login attempts and generates alerts for potentially suspicious account activity.

## Tools Used
- Python 3.13
- Python IDLE
- CSV files
- Windows 11

## Lab Overview
Created a Python script to analyze simulated authentication logs stored in a CSV file.

The program reads login records, counts failed authentication attempts, tracks failures by username, and generates alerts when an account reaches a configurable threshold.

## Methodology
1. Created a CSV file containing simulated login events with timestamps, usernames, and authentication statuses.
2. Used Python's `csv` module to read the records.
3. Implemented lists and dictionaries to organize authentication data.
4. Used loops and conditional statements to count failed logins by account.
5. Configured an alert threshold of five failed attempts per account.
6. Tested the program using multiple simulated authentication scenarios.

## Test Results
- Total login attempts analyzed: 13
- Failed login attempts: 11
- Admin account: 6 failed attempts — Alert triggered
- Guest account: 5 failed attempts — Alert triggered

Additional testing confirmed that accounts below the configured threshold did not generate alerts.

## Screenshot
![Python Security Log Analyzer Results](security_analyzer_results.png)

## Skills Demonstrated
- Python scripting fundamentals
- CSV file parsing
- Authentication log analysis
- Security event monitoring
- Threshold-based alert generation
- Troubleshooting and debugging

## Key Takeaways
This lab provided hands-on experience with Python automation and basic security monitoring concepts. It demonstrated how authentication records can be analyzed to identify accounts that may require further investigation.

**Note:** All login records are simulated. Threshold alerts indicate potentially suspicious activity, not confirmed security incidents.

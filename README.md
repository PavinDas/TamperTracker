
# TamperTracker

<img src="https://socialify.git.ci/PavinDas/TamperTracker/image?description=1&font=KoHo&language=1&name=1&owner=1&pattern=Solid&theme=Dark" alt="Socket" width="640" height="320" />


A Python-based file integrity monitoring system that detects unauthorized modifications to files in a specified folder. When a change is detected, it automatically creates an incident ticket in Jira for tracking and resolution.


## Features

- **File Integrity Monitoring:** Uses SHA-256 hashing to track file changes.

- **Automatic Alerts:** Detects unauthorized modifications in real-time.

- **Jira Integration:** Creates incident tickets when tampering is detected.

- **Customizable Interval:** Runs at user-defined intervals for continuous monitoring.

-  **Easy Setup:** Simply specify a folder to monitor and provide Jira credentials.
## Installation

**Prerequisites**

Ensure you have the following installed:
- Python 3.x
- requests (for Jira API integration)

Install dependencies using:

```bash
pip install requests
```
**Setup & Configuration**

- Clone the repository
```bash
git clone https://github.com/your-username/TamperTracker.git
cd TamperTracker
```
- Store Jira API Key
    - Creates a file ```api-key.txt``` in the project directory
    - Paste you **Jira API token** inside the file.

- Run the script
```bash
python3 tamper_tracker.py
```
- Provide user inputs
    - Enter the **directory path** to monitor.
    - Enter the **monitoring interval** in seconds.

## How It Works
- **Inital Scan:**  Computes SHA-256 hashes for all files in the specified folder and stores them.

- **Periodic Check:** Compares current file hashes with stored hashes.

- **Tampering Detection:** If a file's hash changes, it logs the modification.

- **Jira Ticket Creation:** Sends an alert to Jira by creating a ticket.

- **Continuous Monitoring:** The script runs indefinitely, checking files at set intervals.
## Example Output

```
Enter directory path: /home/user/Documents
Enter time interval in seconds: 300
Monitoring folder for file integrity changes...
/home/user/Documents/report.pdf is safe!
/home/user/Documents/data.txt is safe!
Next check in 300 seconds...
```
**If a file changed is detected:**
```
File integrity issue detected: /home/user/Documents/report.pdf
Jira ticket created successfully for /home/user/Documents/report.pdf.
```
## Jira Ticket Example

**Summary:** File Integrity Alert: report.pdf

**Description:** File integrity change detected for ```/home/user/Documents/report.pdf on 2025-02-05 14:30:00```

**Issue Type:** Task

## License

This project is owned by [Pavin Das](https://github.com/PavinDas)


## Authors

Developed by Your [Pavin Das](https://www.github.com/PavinDas). Contributions are welcome!

Feel free to reach out for improvements or issues.


# Login Attempt Analyzer

A simple Python tool that analyzes server login logs to detect suspicious activity, such as brute-force login attempts.

## Why this project?

As a Cybersecurity diploma graduate, I wanted to combine my security knowledge with programming skills by building a practical tool that solves a real security problem: detecting repeated failed login attempts from the same IP address, a common sign of brute-force attacks.

## Features

- Reads any login log file
- Counts failed login attempts per IP address
- Flags IPs that exceed a user-defined threshold
- Displays color-coded alerts in the terminal
- Saves a clean report to `report.txt`

## Technologies Used

- Python 3
- [colorama](https://pypi.org/project/colorama/) for colored terminal output

## How to Run

1. Clone this repository or download the files
2. Install the required library: pip install colorama
3. Run the script: python analyzer.py
4. Enter the log file name and the failed-attempts threshold when prompted

## Example

Input log line: 2026-08-20 09:01:12 LOGIN_FAILED user=admin ip=192.168.1.15

Output:

WARNING: IP 192.168.1.15 exceeded the limit! (5 attempts)

## Future Improvements

- Support for real-world log formats
- Export report in JSON/CSV format
- Add a simple GUI
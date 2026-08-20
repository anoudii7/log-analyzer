# analyzer.py
from colorama import init, Fore, Style

init(autoreset=True)  # يخلي كل لون يرجع للوضع الطبيعي بعد كل طباعة تلقائيًا

log_filename = input("Enter the log file name (e.g. sample.log): ")
threshold_input = input("Enter the failed-attempts threshold (e.g. 3): ")
THRESHOLD = int(threshold_input)

failed_attempts = {}

with open(log_filename, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    parts = line.split()
    
    status = parts[2]
    ip_raw = parts[4]
    ip = ip_raw.replace("ip=", "")
    
    if status == "LOGIN_FAILED":
        if ip in failed_attempts:
            failed_attempts[ip] = failed_attempts[ip] + 1
        else:
            failed_attempts[ip] = 1

report_lines = []
report_lines.append("=== Failed Login Report ===")
for ip, count in failed_attempts.items():
    report_lines.append(f"{ip} -> {count} failed attempts")

report_lines.append("")
report_lines.append("=== Alerts ===")
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        report_lines.append(f"WARNING: IP {ip} exceeded the limit! ({count} attempts)")

# نطبع بالشاشة مع تلوين
print(Fore.CYAN + "=== Failed Login Report ===")
for ip, count in failed_attempts.items():
    print(f"{ip} -> {count} failed attempts")

print()
print(Fore.CYAN + "=== Alerts ===")
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(Fore.RED + Style.BRIGHT + f"WARNING: IP {ip} exceeded the limit! ({count} attempts)")

# نحفظ التقرير بملف (بدون رموز الألوان، لأنها ما تنفع بملف نصي عادي)
with open("report.txt", "w") as report_file:
    for line in report_lines:
        report_file.write(line + "\n")

print()
print(Fore.GREEN + "Report saved to report.txt")
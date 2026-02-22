log_file = "logs.txt"

print("------ Keylogger Logs ------\n")

try:
    with open(log_file, "r") as file:
        logs = file.read()
        print(logs)
except FileNotFoundError:
    print("No logs found.")
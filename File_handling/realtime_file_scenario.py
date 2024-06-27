import datetime

def log_message(message, log_file="log.txt"):
    with open(log_file, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {message}\n")

def read_logs(log_file="log.txt"):
    try:
        with open(log_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Log file not found."

# Example usage
log_message("This is an info message.")
log_message("This is a warning message.")
log_message("This is an error message.")

print("Logs:")
print(read_logs())

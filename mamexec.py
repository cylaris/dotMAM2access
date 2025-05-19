import os
import subprocess
import webbrowser
import time
from tkinter import Tk, filedialog, messagebox

def parse_mam_file(filepath):
    attributes = {}
    with open(filepath, 'r') as file:
        for line in file:
            if '=' in line:
                key, val = line.strip().split('=', 1)
                attributes[key.strip()] = val.strip()
    return attributes

def execute_urls(attributes):
    urls = [v for k, v in attributes.items() if k.startswith("exec_url_")]
    for url in urls:
        print(f"Opening URL: {url}")
        webbrowser.open(url)
        time.sleep(0.5)  

def launch_executable(attributes):
    path = attributes.get("executable_path")
    if not path or not os.path.exists(path):
        print("Executable path is invalid or not provided.")
        return

    print(f"Launching executable: {path}")
    try:
        subprocess.Popen(path)
    except Exception as e:
        print(f"Error launching executable: {e}")

def main():
    Tk().withdraw()  
    mam_path = filedialog.askopenfilename(title="Select a .mam File",
                                          filetypes=[("MAM files", "*.mam")])
    if not mam_path:
        return

    attributes = parse_mam_file(mam_path)

    if attributes.get("requires_admin", "False").lower() == "true":
        messagebox.showwarning("Admin Required", "This program may require admin privileges.")

    if attributes.get("execute_on_open", "False").lower() == "true":
        execute_urls(attributes)

    if "executable_path" in attributes:
        launch_executable(attributes)

if __name__ == "__main__":
    main()

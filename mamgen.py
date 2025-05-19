import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import uuid

def generate_mam_content(name, version, author, urls, exec_on_open):
    created_at = datetime.now().isoformat()
    unique_id = str(uuid.uuid4())

    urls = [url.strip() for url in urls.splitlines() if url.strip()]

    content = (
        f"name = {name}\n"
        f"version = {version}\n"
        f"author = {author}\n"
        f"created_at = {created_at}\n"
        f"uuid = {unique_id}\n"
        f"execute_on_open = {exec_on_open}\n"
    )

    if urls:
        for i, url in enumerate(urls, 1):
            content += f"exec_url_{i} = {url}\n"

    return content

def save_mam_file():
    name = entry_name.get().strip()
    version = entry_version.get().strip()
    author = entry_author.get().strip()
    urls = text_urls.get("1.0", tk.END).strip()
    exec_on_open = var_exec.get()

    if not name or not version or not author:
        messagebox.showwarning("Missing Input", "Please fill in name, version, and author.")
        return

    content = generate_mam_content(name, version, author, urls, exec_on_open)

    file_path = filedialog.asksaveasfilename(defaultextension=".mam",
                                             filetypes=[("MAM files", "*.mam")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)
        messagebox.showinfo("Success", f".mam file saved to:\n{file_path}")

root = tk.Tk()
root.title(".mam File Generator with URL Execution @deFr0ggy")
root.geometry("500x500")

tk.Label(root, text="Name:").pack(pady=(10, 0))
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Version:").pack(pady=(10, 0))
entry_version = tk.Entry(root, width=50)
entry_version.pack()

tk.Label(root, text="Author:").pack(pady=(10, 0))
entry_author = tk.Entry(root, width=50)
entry_author.pack()

tk.Label(root, text="Execution URLs (one per line):").pack(pady=(15, 0))
text_urls = tk.Text(root, height=5, width=60)
text_urls.pack(pady=(0, 10))

var_exec = tk.BooleanVar()
chk_exec = tk.Checkbutton(root, text="Execute URLs on open", variable=var_exec)
chk_exec.pack()

tk.Button(root, text="Generate .mam File", command=save_mam_file).pack(pady=20)

root.mainloop()

import os
import shutil
import tkinter as tk
from tkinter import messagebox

def organize_desktop(selected_categories):
    desktop_path = os.path.expanduser("~/Desktop")
    if not os.path.exists(desktop_path):
        messagebox.showerror("Error", "Desktop path not found.")
        return

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Music": [".mp3", ".wav", ".ogg"],
        "Archives": [".zip", ".rar", ".7z"],
        "Others": []  # Default category for files with unknown extensions
    }

    # Create folders for each selected category if they don't exist
    for category in selected_categories:
        category_path = os.path.join(desktop_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Organize files into the selected categories
    for filename in os.listdir(desktop_path):
        if filename != "organize_desktop.py":  # Exclude this script from being moved
            src_file = os.path.join(desktop_path, filename)
            if os.path.isfile(src_file):
                file_ext = os.path.splitext(filename)[1].lower()
                dest_category = "Others"  # Default category
                for category, extensions in categories.items():
                    if category in selected_categories and file_ext in extensions:
                        dest_category = category
                        break
                if dest_category in selected_categories:
                    dest_folder = os.path.join(desktop_path, dest_category)
                    shutil.move(src_file, dest_folder)

    messagebox.showinfo("Success", "Desktop organized successfully.")

def create_gui():
    root = tk.Tk()
    root.title("Desktop Organizer")

    categories = ["Images", "Documents", "Videos", "Music", "Archives", "Others"]

    # Dictionary to hold the state of each checkbox
    checkboxes = {}
    
    # Add checkboxes for each category
    for category in categories:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=category, variable=var)
        chk.pack(anchor='w')
        checkboxes[category] = var

    def on_run():
        selected_categories = [category for category, var in checkboxes.items() if var.get()]
        organize_desktop(selected_categories)

    run_button = tk.Button(root, text="Run", command=on_run)
    run_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()

import os
import shutil
import customtkinter as ctk
from tkinter import filedialog

# App Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.geometry("800x650")
app.title("Automated File Organizer by MCA Student")

selected_folder = ""

# Choose Folder Function
def choose_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()

    if selected_folder:
        folder_label.configure(text=selected_folder)

# Organize Files Function
def organize_files():
    if selected_folder == "":
        result_label.configure(text="Please select a folder first!")
        return

    moved_files = 0

    # Clear previous details
    details_box.delete("1.0", "end")

    for file in os.listdir(selected_folder):
        file_path = os.path.join(selected_folder, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Find extension
        if "." in file:
            extension = file.split(".")[-1].lower()
        else:
            extension = "no_extension"

        # Create extension folder if not exists
        target_folder = os.path.join(selected_folder, extension)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Move file
        shutil.move(file_path, os.path.join(target_folder, file))
        moved_files += 1

        # Show moved file details
        details_box.insert(
            "end",
            f"{file}  →  moved to '{extension}' folder\n"
        )

    # Final Result
    result_label.configure(
        text=f"{moved_files} files organized successfully!"
    )

# Reset Function
def reset_app():
    global selected_folder
    selected_folder = ""

    folder_label.configure(text="No folder selected")
    result_label.configure(text="")
    details_box.delete("1.0", "end")

# Title
title = ctk.CTkLabel(
    app,
    text="Automated File Organizer",
    font=("Arial", 30, "bold")
)
title.pack(pady=25)

# Subtitle
subtitle = ctk.CTkLabel(
    app,
    text="Select any folder and organize files automatically by extension",
    font=("Arial", 15)
)
subtitle.pack(pady=5)

# Choose Folder Button
select_button = ctk.CTkButton(
    app,
    text="Choose Folder",
    command=choose_folder,
    width=220,
    height=45,
    font=("Arial", 16, "bold")
)
select_button.pack(pady=20)

# Selected Folder Label
folder_label = ctk.CTkLabel(
    app,
    text="No folder selected",
    wraplength=700,
    font=("Arial", 14)
)
folder_label.pack(pady=10)

# Organize Button
organize_button = ctk.CTkButton(
    app,
    text="Organize Files",
    command=organize_files,
    width=220,
    height=45,
    font=("Arial", 16, "bold")
)
organize_button.pack(pady=15)

# Reset Button
reset_button = ctk.CTkButton(
    app,
    text="Reset",
    command=reset_app,
    width=220,
    height=45,
    font=("Arial", 16, "bold"),
    fg_color="gray"
)
reset_button.pack(pady=10)

# Result Label
result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=20)

# Details Box
details_box = ctk.CTkTextbox(
    app,
    width=700,
    height=220,
    font=("Arial", 14)
)
details_box.pack(pady=10)

# Run App
app.mainloop()
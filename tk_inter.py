import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Login System")
root.geometry("400x300")

# Hardcoded credentials for demonstration
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Function to validate login
def validate_login(): 
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
    elif username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()  # Close the login window
        # Here you can redirect to a new window or dashboard
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# GUI Components
title_label = tk.Label(root, text="Login System", font=("Arial", 20))
title_label.pack(pady=20)

# Username Label and Entry
username_label = tk.Label(root, text="Username:", font=("Arial", 14))
username_label.pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:", font=("Arial", 14))
password_label.pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 14), show="*")  # Hides password with '*'
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", font=("Arial", 14), command=validate_login)
login_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()

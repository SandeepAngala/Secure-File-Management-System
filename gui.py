import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Text
from ttkthemes import ThemedTk
import platform
import subprocess
import tempfile
import logging
from auth_filemanager import Authentication, FileManager  # Dependencies
from database import setup_database  # Dependency

# Logging is already set up in database.py
logging.getLogger(__name__)

class App:
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.auth = Authentication()
        self.username = ""
        self.session_token = ""
        self.root.title("Secure File Management System (MySQL)")
        self.root.geometry("600x500")
        self.show_login_page()

    def show_login_page(self):
        """Display the login page."""
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        tk.Label(self.root, text="TOTP Code").pack(pady=5)
        self.totp_entry = tk.Entry(self.root)
        self.totp_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register).pack(pady=5)


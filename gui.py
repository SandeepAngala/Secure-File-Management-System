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

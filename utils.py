from datetime import datetime

def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_title(text):
    return " ".join(word.capitalize() for word in text.split())

def separator():
    return "-" * 45

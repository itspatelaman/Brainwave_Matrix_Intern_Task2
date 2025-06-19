import re
import string
import math
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Load common passwords from a file
def load_common_passwords(filepath="common_passwords.txt"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return set(pw.strip().lower() for pw in f.readlines())
    except FileNotFoundError:
        return set()

common_passwords = load_common_passwords()

def has_sequential_chars(password, seq_len=3):
    for i in range(len(password) - seq_len + 1):
        segment = password[i:i+seq_len]
        if all(ord(segment[j]) == ord(segment[0]) + j for j in range(seq_len)):
            return True
        if all(ord(segment[j]) == ord(segment[0]) - j for j in range(seq_len)):
            return True
    return False

# Estimate the time to crack a password based on its length and character set
def estimate_crack_time(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 32

    combinations = charset ** len(password)
    guesses_per_second = 1e10  # Adjust for realistic/higher attack models
    seconds = combinations / guesses_per_second

    units = [("seconds", 60), ("minutes", 60), ("hours", 24), ("days", 365), ("years", 100), ("centuries", 10)]
    for unit, divisor in units:
        if seconds < divisor:
            return f"{seconds:.2f} {unit}"
        seconds /= divisor
    return f"{seconds:.2f} millennia"

# Function to evaluate password strength
def evaluate_password_strength(password):
    score = 0
    suggestions = []

    if len(password) < 6:
        suggestions.append("Use at least 6 characters.")
    elif 6 <= len(password) < 8:
        score += 10
        suggestions.append("Try using 8 or more characters.")
    elif 8 <= len(password) < 12:
        score += 20
    else:
        score += 40  # Boosted to support max 100

    if re.search(r'[a-z]', password):
        score += 15
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 15
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r'[0-9]', password):
        score += 15
    else:
        suggestions.append("Add numbers.")

    if re.search(r'[^a-zA-Z0-9]', password):
        score += 15
    else:
        suggestions.append("Add special characters.")

    if re.search(r'(.)\1{2,}', password):
        score -= 10
        suggestions.append("Avoid repeated characters.")

    if has_sequential_chars(password):
        score -= 10
        suggestions.append("Avoid sequential characters like abc or 123.")

    is_common = password.lower() in common_passwords
    if is_common:
        score -= 20
        suggestions.append("This password is too common or has been leaked!")

    # Strength label and color
    if is_common:
        level = "🔴 leaked"
        level_color = "red"
    elif score < 30:
        level = "🔴 Very Weak"
        level_color = "red"
    elif score < 50:
        level = "🟠 Weak"
        level_color = "orange"
    elif score < 70:
        level = "🟡 Good"
        level_color = "yellow"
    elif score < 90:
        level = "🟢 Very Good"
        level_color = "lightgreen"
    else:
        level = "✅ Strong"
        level_color = "lime"

    crack_time = estimate_crack_time(password)

    return {
        "password": password,
        "score": max(0, min(score, 100)),
        "strength": level,
        "crack_time": crack_time,
        "suggestions": suggestions,
        "color": level_color
    }

def run_gui():
    def on_check_strength():
        pwd = entry.get()
        if not pwd:
            result_box.config(state='normal')
            result_box.delete(1.0, tk.END)
            result_box.insert(tk.END, "⚠️ Please enter a password.")
            result_box.config(state='disabled')
            return

        result = evaluate_password_strength(pwd)
        strength_bar["value"] = result["score"]
        strength_label.config(text=f"Strength: {result['strength']}", fg=result["color"])

        result_text = f"Password: {result['password']}\n"
        result_text += f"Score: {result['score']} / 100\n"
        result_text += f"Crack Time Estimate: ⏱️ {result['crack_time']}\n"

        if result["suggestions"]:
            result_text += "\nSuggestions:\n"
            for s in result["suggestions"]:
                result_text += f"- {s}\n"

        result_box.config(state='normal')
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, result_text)
        result_box.config(state='disabled')

    def toggle_password():
        if entry.cget('show') == '':
            entry.config(show='*')
            toggle_btn.config(text='Show')
        else:
            entry.config(show='')
            toggle_btn.config(text='Hide')

    # GUI Setup
    root = tk.Tk()
    root.title("Password Strength Checker")
    root.configure(bg="#121212")

    font_title = ("Consolas", 14, "bold")
    font_text = ("Consolas", 11)

    tk.Label(root, text="Enter Your Password:", font=font_title, bg="#121212", fg="white").pack(pady=10)

    entry_frame = tk.Frame(root, bg="#121212")
    entry_frame.pack()

    entry = tk.Entry(entry_frame, width=35, show='', font=font_text, bg="black", fg="lime", insertbackground="white")
    entry.pack(side=tk.LEFT, padx=5)

    toggle_btn = tk.Button(entry_frame, text="Hide", command=toggle_password, font=font_text, bg="#333", fg="white")
    toggle_btn.pack(side=tk.LEFT)

    tk.Button(root, text="Check Strength", command=on_check_strength, font=font_text, bg="#00b697", fg="black").pack(pady=10)

    strength_bar = ttk.Progressbar(root, length=300, mode='determinate')
    strength_bar["maximum"] = 100
    strength_bar.pack(pady=5)

    strength_label = tk.Label(root, text="Strength: ", font=font_text, bg="#121212", fg="white")
    strength_label.pack()

    result_box = ScrolledText(root, height=15, width=75, font=font_text, bg="#1e1e1e", fg="cyan")
    result_box.pack(pady=10)
    result_box.config(state='disabled')

    tk.Label(root, text="* Uses common_passwords.txt for leak check", font=("Consolas", 8), bg="#121212", fg="gray").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
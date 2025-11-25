import tkinter as tk
from tkinter import messagebox
import string

def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
        remarks.append("•  Good Length ")
    else:
        remarks.append("•  Too Short (Min: 8) ")

    if any(c.islower() for c in password):
        score += 1
        remarks.append("•  Contains Lowercase ")
    else:
        remarks.append("•  Missing Lowercase ")

    if any(c.isupper() for c in password):
        score += 1
        remarks.append("•  Contains Uppercase ")
    else:
        remarks.append("•  Missing Uppercase ")

    if any(c.isdigit() for c in password):
        score += 1
        remarks.append("•  Contains Numbers ")
    else:
        remarks.append("•  Missing Numbers ")

    if any(c in string.punctuation for c in password):
        score += 1
        remarks.append("•  Contains Symbols ")
    else:
        remarks.append("•  Missing Symbols ")

    if score == 5:
        return "🟢 VERY STRONG", remarks, "#008037"
    elif score == 4:
        return "🟡 STRONG", remarks, "#228B22"
    elif score == 3:
        return "🟠 MEDIUM", remarks, "#FF8C00"
    elif score == 2:
        return "🔴 WEAK", remarks, "#B30000"
    else:
        return "⚫ VERY WEAK", remarks, "#5A0000"


def evaluate_password():
    password = entry.get()

    if not password:
        messagebox.showwarning("Alert!", "Please enter a password!")
        return

    strength, details, color = check_password_strength(password)
    result_label.config(text=strength, fg=color)

    details_box.config(state=tk.NORMAL)
    details_box.delete("1.0", tk.END)

    for item in details:
        details_box.insert(tk.END, item + "\n")

    details_box.config(state=tk.DISABLED)


def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
        toggle_btn.config(text="Hide", fg="white", bg="#004d4d")
    else:
        entry.config(show="*")
        toggle_btn.config(text="Show", fg="white", bg="#004d4d")


# -------- GUI --------
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("560x420")
window.configure(bg="#DFF6FF")
window.resizable(False, False)

title = tk.Label(window, text=" Password Strength Checker", 
                 font=("Segoe UI", 18, "bold"), bg="#DFF6FF", fg="#004d4d")
title.pack(pady=15)

entry = tk.Entry(window, width=35, font=("Segoe UI", 13), show="*", relief="solid", bd=1)
entry.pack(pady=5)

# Square toggle button
toggle_btn = tk.Button(window, text="Show", command=toggle_password, font=("Segoe UI", 10, "bold"),
                       width=8, height=1, bg="#006666", fg="white", relief="ridge")
toggle_btn.pack(pady=5)

btn = tk.Button(window, text="Check Strength", command=evaluate_password,
                font=("Segoe UI", 13, "bold"), width=15, bg="#00A19D", fg="white")
btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Segoe UI", 14, "bold"), bg="#DFF6FF")
result_label.pack(pady=5)

details_box = tk.Text(window, height=8, width=50, font=("Segoe UI", 11, "bold"),
                      relief="solid", bd=1, fg="#003333")
details_box.pack(pady=10)
details_box.config(state=tk.DISABLED)

window.mainloop()


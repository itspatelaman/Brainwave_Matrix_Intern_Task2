# 🔐 Password Strength Checker (Tkinter GUI)

A professional-grade password strength checker built using Python and Tkinter. This tool analyzes password complexity, estimates time to crack, and offers actionable suggestions to improve security. It also checks against a list of common passwords to detect reused or compromised credentials.

---

## 🚀 Features

- ✅ Real-time strength analysis with a visual progress bar  
- ✅ Estimates **crack time** using brute-force assumptions  
- ✅ Flags **common or leaked passwords** (from `common_passwords.txt`)  
- ✅ Detects:
  - Repeated characters
  - Sequential patterns (`abc`, `123`)
  - Missing character types (uppercase, digits, special chars)
- ✅ Provides clear **suggestions** to improve password quality  
- ✅ Toggle password visibility (show/hide)  
- ✅ Dark-themed GUI with modern fonts and coloring

---
## 📄 Note: Common Password List Not Included

### ⚠️ Important :
This project uses a large common_passwords.txt file to check whether a password appears in leaked/common password databases.

To keep the repository lightweight and avoid GitHub push issues, this file is not included in the repo.

✅ What You Should Do:
After cloning this repository locally, please do one of the following:

**Option 1** : Use SecLists (Recommended)
Download a trusted common password list from SecLists:
```
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt -O common_passwords.txt
```

**Option 2** : Use Your Own
Place your own common_passwords.txt file in the project root directory. Each password should be on a new line.


#### ℹ️ Why This Matters:
The password checker will only mark passwords as "weak" due to being common if this file exists in the same folder. Without it, the common password check is skipped.

## 📸 Demo Preview

**👉 Want to see how it looks?**

Check out the live results and screenshots on my [LinkedIn Profile](https://www.linkedin.com/in/your-profile-or-post-link).

*This includes sample outputs, UI design, and strength checking in action.*

---

## 🧠 How It Works

The password is scored based on:
- Length
- Character diversity (uppercase, lowercase, digits, symbols)
- Penalties for patterns and repetition
- Comparison against a list of common passwords

An estimated **crack time** is calculated based on the total character set and password length, assuming 10 billion guesses per second (brute-force attack model).

---

## 📁 File Structure
```
├── password_checker.py # Main GUI application
├── common_passwords.txt # List of known weak/common passwords
├── README.md # Project documentation
```

---

## 🛠️ Requirements

- Python 3.7+
- Tkinter (comes with standard Python)
- `common_passwords.txt` file in the same directory

---

## 🔧 Setup & Usage

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

 **Run the Application :**
```
 python password_checker.py
```
--- 

## 📚 Example Output
```
Password: mySecurePass!23
Score: 85 / 100
Crack Time Estimate: ⏱️ 137 years

Suggestions:
- Avoid sequential characters like abc or 123.
```

## 🧩 Customization
* Modify common_passwords.txt to include more passwords.

* Update crack time logic in estimate_crack_time() to reflect real-world attacker models.

* Change GUI colors, fonts, or add features like:

* Password generator

* Copy to clipboard

* Export result to .txt or .pdf

## ⚠️ Disclaimer

This tool is for educational and personal use only.
It should not be solely relied on for enterprise-level password policies. Always follow cybersecurity best practices and use multi-factor authentication where possible.

## 🙌 Credits

Developed by **Aman Patel**

Inspired by real-world password security tools and OWASP standards.

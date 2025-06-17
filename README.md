# 📧 Auto Email Sender

A simple yet powerful Python script that allows you to send a single email message to **multiple recipients** in bulk by listing them in an `emails.txt` file. Ideal for small campaigns, notifications, or announcements. Works best with **Gmail** SMTP.

---

## 🚀 Features

* Send emails to multiple addresses automatically
* Validate recipient email addresses before sending
* Customizable subject and body content via `data.json`
* Uses secure SSL connection

---

## 🛠️ Requirements

Make sure you have the following Python package installed:

```bash
pip install email-validator
```

Or you can run the following command to install all required modules:

```bash
pip install -r requirements.txt
```

> 💡 No need to install `os`, `ssl`, `json`, `smtplib`, or `email.message` — they are built-in modules in Python.

---

## ⚙️ Setup Instructions

### 1. Configure Your Gmail Account 📩

If you're using Gmail:

1. Go to your [Google App Passwords](https://myaccount.google.com/apppasswords)
2. Generate a password for the "Mail" app
3. Copy it into `data.json` like this:

```json
[
  {
    "email-address": "your_email@gmail.com",
    "password": "your_app_password",
    "smtp": "smtp.gmail.com"
  },
  {
    "subject": "Subject of the Email",
    "body": "Body of your email goes here."
  }
]
```

### 2. Add Recipient Emails

List the email addresses line-by-line in `emails.txt`:

```
example1@gmail.com
example2@yahoo.com
```

---

## 💻 Running the Script

Make sure Python is installed on your system, then:

```bash
python app.py
```

You should see status messages about each email being validated and sent. If any email is invalid, it will be skipped with a warning.

---

## ✏️ Customizing SMTP Settings

By default, the script uses `smtp.gmail.com`.
If you're using a different email provider, just update the `smtp` field in `data.json`:

```json
"smtp": "smtp.yourprovider.com"
```

---

## 📁 File Overview

| File Name    | Purpose                                           |
| ------------ | ------------------------------------------------- |
| `app.py`     | Main Python script                                |
| `emails.txt` | Contains recipient email addresses (one per line) |
| `data.json`  | Contains login credentials and email content      |

---

## ❓ FAQ

### 🔧 How do I install dependencies?

Run:

```bash
pip install email-validator
```

### 🚨 What happens if an email is invalid?

The script will skip it and print a warning in the terminal.

### 🌍 Can I use this with Outlook, Yahoo, etc.?

Yes, just change the `smtp` field in `data.json` to the correct SMTP server.

---

## 🙋 Feedback & Contributions

Feel free to open an [issue](https://github.com/Jienniers/AutoEmailSender/issues) or submit a pull request if you find bugs or have feature suggestions.

---

## 👤 Author

**Jienniers**
📫 [GitHub Profile](https://github.com/Jienniers)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---
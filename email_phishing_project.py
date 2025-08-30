def detect_phishing_email(email_text):
    phishing_keywords = ["verify your account", "urgent action required", 
                         "click the link", "password reset", "bank account"]

    for word in phishing_keywords:
        if word.lower() in email_text.lower():
            return "⚠️ Phishing email detected!"
    return "✅ Safe email."

if __name__ == "__main__":
    emails = [
        "Dear user, please verify your account by clicking the link.",
        "Meeting at 5 PM tomorrow, please confirm.",
        "Urgent action required: reset your bank account password now!"
    ]

    for e in emails:
        print(f"Email: {e}")
        print(detect_phishing_email(e))
        print("-" * 50)

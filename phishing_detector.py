import tldextract
import validators

# List of known safe domains (simulation)
safe_domains = ["google.com", "github.com", "gmail.com"]

def is_phishing(url):
    if not validators.url(url):
        return "Invalid URL"

    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    if domain not in safe_domains:
        return f"⚠️ Suspicious URL detected: {url}"
    return f"✅ Safe URL: {url}"

if __name__ == "__main__":
    test_urls = [
        "http://secure-google.com/login",
        "https://github.com/openai",
        "http://fake-bank-login.net"
    ]

    for url in test_urls:
        print(is_phishing(url))

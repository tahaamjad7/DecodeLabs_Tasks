# phishing_checker.py
# Basic tool to scan an email/message and flag things that commonly show up
# in phishing attempts - urgent language, fake links, requests for
# passwords/OTP, mismatched sender domains etc.
#
# This is NOT a spam filter, just a learning tool to understand what
# red flags look like.

import re

# words/phrases that scammers love to use to create panic or urgency
SUSPICIOUS_PHRASES = [
    "verify your account",
    "urgent action required",
    "your account will be suspended",
    "click here immediately",
    "confirm your password",
    "update your billing",
    "you have won",
    "claim your prize",
    "act now",
    "limited time offer",
    "unusual activity detected",
    "your account has been locked",
    "provide your otp",
    "enter your pin",
    "security alert",
    "dear customer",  # generic greeting, real banks usually use your name
]

# domains that are commonly spoofed / free hosting often abused for phishing
SKETCHY_DOMAIN_HINTS = [
    "bit.ly", "tinyurl", "grabify", "shorturl",  # link shorteners hide real destination
    ".xyz", ".top", ".club", ".info",  # cheap TLDs frequently abused
]


def find_links(text):
    # very simple url pattern, good enough for this kind of check
    url_pattern = r"(https?://[^\s]+|www\.[^\s]+)"
    return re.findall(url_pattern, text)


def flag_suspicious_phrases(text):
    text_lower = text.lower()
    found = []
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in text_lower:
            found.append(phrase)
    return found


def flag_suspicious_links(links):
    flagged = []
    for link in links:
        link_lower = link.lower()
        for hint in SKETCHY_DOMAIN_HINTS:
            if hint in link_lower:
                flagged.append(link)
                break
    return flagged


def check_sender_mismatch(display_name, sender_email):
    # e.g. display name says "PayPal Support" but email is from a random domain
    if not display_name or not sender_email:
        return False

    known_brands = ["paypal", "amazon", "microsoft", "apple", "bank", "google"]
    name_lower = display_name.lower()
    email_lower = sender_email.lower()

    for brand in known_brands:
        if brand in name_lower and brand not in email_lower:
            return True
    return False


def analyze_message(display_name, sender_email, body_text):
    red_flags = []

    links = find_links(body_text)
    bad_phrases = flag_suspicious_phrases(body_text)
    bad_links = flag_suspicious_links(links)
    mismatch = check_sender_mismatch(display_name, sender_email)

    if bad_phrases:
        red_flags.append(f"Uses urgency/pressure language: {', '.join(bad_phrases)}")

    if bad_links:
        red_flags.append(f"Contains suspicious links: {', '.join(bad_links)}")

    if links and not bad_links:
        # links exist but weren't flagged by our hint list, still worth a manual check
        red_flags.append("Message contains links - verify the real destination before clicking")

    if mismatch:
        red_flags.append(f"Sender name '{display_name}' doesn't match the actual email domain")

    if "otp" in body_text.lower() or "password" in body_text.lower():
        red_flags.append("Asks for sensitive info (OTP/password) - legitimate companies never do this over email")

    # decide overall risk based on how many red flags we found
    if len(red_flags) == 0:
        risk = "Looks Safe"
    elif len(red_flags) <= 2:
        risk = "Possibly Suspicious"
    else:
        risk = "Likely Phishing"

    return risk, red_flags


def print_report(display_name, sender_email, body_text, risk, red_flags):
    print("\n----------------------------------------")
    print("From        :", display_name, f"<{sender_email}>")
    print("Message     :", body_text[:80] + ("..." if len(body_text) > 80 else ""))
    print("Risk Level  :", risk)

    if red_flags:
        print("Red Flags Found:")
        for i, flag in enumerate(red_flags, start=1):
            print(f"  {i}. {flag}")
    else:
        print("No red flags detected in this message.")
    print("----------------------------------------")


# a few sample messages to demonstrate the tool - mix of safe and phishing
sample_messages = [
    {
        "display_name": "PayPal Support",
        "sender_email": "no-reply@paypa1-secure.xyz",
        "body": "Dear Customer, unusual activity detected on your account. "
                "Verify your account immediately at http://bit.ly/fake-paypal-login "
                "or your account will be suspended within 24 hours."
    },
    {
        "display_name": "Sarah from HR",
        "sender_email": "sarah.khan@company.com",
        "body": "Hi team, just a reminder that the office will be closed this Friday "
                "for maintenance. See you all next week!"
    },
    {
        "display_name": "Amazon",
        "sender_email": "rewards@amaz0n-prize.top",
        "body": "Congratulations! You have won a $500 gift card. Click here immediately "
                "to claim your prize before it expires: http://tinyurl.com/claim-now"
    },
]


def main():
    print("---- Phishing Awareness Analyzer ----")
    print("Running analysis on sample messages...\n")

    for msg in sample_messages:
        risk, red_flags = analyze_message(msg["display_name"], msg["sender_email"], msg["body"])
        print_report(msg["display_name"], msg["sender_email"], msg["body"], risk, red_flags)

    # also let the user try their own message
    print("\nWant to check your own message? (leave blank to skip)")
    own_name = input("Sender display name: ")
    if own_name.strip() != "":
        own_email = input("Sender email: ")
        own_body = input("Message body: ")
        risk, red_flags = analyze_message(own_name, own_email, own_body)
        print_report(own_name, own_email, own_body, risk, red_flags)


if __name__ == "__main__":
    main()

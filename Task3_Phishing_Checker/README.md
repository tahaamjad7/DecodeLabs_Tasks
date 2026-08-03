# Task 3: Phishing Awareness Analyzer

A Python script that scans an email/message and flags common phishing
indicators. This is a learning/awareness tool, not a production spam filter.

## Key Requirements Covered
- **Suspicious links/keywords**: checks for urgency phrases (e.g. "verify
  your account", "act now") and risky link patterns (URL shorteners, cheap
  abused TLDs like `.xyz`/`.top`).
- **Red flags list**: every message is scored and a full list of the red
  flags found is printed (e.g. urgency language, suspicious links, sender
  name/domain mismatch, requests for OTP/password).
- **Why it's unsafe**: each red flag comes with a short explanation of why
  it's a common phishing tactic (e.g. "legitimate companies never ask for
  your OTP/password over email").

## How it works
1. `find_links()` extracts any URLs in the message.
2. `flag_suspicious_phrases()` checks the body against a list of common
   pressure/urgency phrases scammers use.
3. `flag_suspicious_links()` flags links using shorteners or cheap/abused
   domain extensions.
4. `check_sender_mismatch()` compares the sender's display name (e.g.
   "PayPal Support") against the actual email domain, to catch spoofing.
5. `analyze_message()` combines all checks into a red-flag list and an
   overall risk rating: **Looks Safe**, **Possibly Suspicious**, or
   **Likely Phishing**.

## How to run
```bash
python3 phishing_checker.py
```
The script first analyzes 3 built-in sample messages (2 phishing, 1
legitimate) and prints a report for each. You can then optionally enter
your own message to check.

## Example output
```
From        : PayPal Support <no-reply@paypa1-secure.xyz>
Message     : Dear Customer, unusual activity detected on your account...
Risk Level  : Likely Phishing
Red Flags Found:
  1. Uses urgency/pressure language: verify your account, unusual activity detected, ...
  2. Contains suspicious links: http://bit.ly/fake-paypal-login
  3. Sender name 'PayPal Support' doesn't match the actual email domain
```

## Key Skills
Threat analysis, regex/pattern matching, awareness of social engineering
and cyberattack tactics, security-minded thinking.

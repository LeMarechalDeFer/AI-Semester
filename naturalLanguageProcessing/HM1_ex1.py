import re

email_text = "The email addresses are be-mansouri@maine.edu and behrooz.mansouri@cs.maine.edu"
email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(email_pattern, email_text)

print("Email addresses :", emails)

phone_text = "The phone numbers are 207-587-3290, 5583446854, (207) 107-9293, 2075142279x0000"
phone_pattern = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}(?:x\d{1,5})?)"
phones = re.findall(phone_pattern, phone_text)

print("Phone numbers :", phones)
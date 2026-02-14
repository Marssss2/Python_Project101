domain = "example.com"
banned_domains = ["spam.com", "scam.com", "fake.com"]

print(domain in banned_domains) # it will return false because "example.com" is not in the list of banned domains.
print("spam.com" in banned_domains) # it will return true because "spam.com" is in the list of banned domains.
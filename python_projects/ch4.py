# import re
# from collections import Counter

# ----------------------
# ----  problem 1  -----
# ----------------------

# pattern = r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.(com|org|edu)$"
# emails = ["user@example.com", "bad-email", "test@domain.org"]
# valid = [email for email in emails if re.match(pattern, email)]

# print(valid)

# ###################################################
# ----------------------
# ----  problem 2  -----
# ----------------------

# Texts = "I love #Python and #AI"
# hashtags = re.findall(r"#\w+", Texts)
# print(hashtags)

# ###################################################
# ----------------------
# ----  problem 3  -----
# ----------------------

# phones = ["+1-555-1234", "5551234", "123-456-7890"]
# pattern = r"^\+?\d{1,3}[-]?\d{3}[-]?\d{4}$"

# for p in phones:
#     print(f"{p}: {bool(re.match(pattern, p))}")

# ###################################################
# ----------------------
# ----  problem 4  -----
# ----------------------

# Str = "Python, Python! AI is great; Python AI."
# words = re.findall(r"\w+", Str)
# freq = dict(Counter(words))

# print(freq)

# ###################################################
# ----------------------
# ----  problem 5  -----
# ----------------------

# Str = "This is is a test test"
# duplicates = re.findall(r"\b(\w+)\s+\1\b", Str)

# print([f"{w} {w}" for w in duplicates])

# ###################################################
# ----------------------
# ----  problem 6  -----
# ----------------------

# event = "The events are on 2023-05-12 and 2024-01-01."
# pattern = r"\d{4}-\d{2}-\d{2}"
# event_dates = re.findall(pattern, event)

# print(event_dates)

# ###################################################
# ----------------------
# ----  problem 7  -----
# ----------------------

# credit_Card = "Card: 1234-5678-9012-3456"
# masked_Card = re.sub(r"\d(?=[\d-]*\d{4})", "*",credit_Card)
# print(masked_Card)

# ###################################################
# ----------------------
# ----  problem 8  -----
# ----------------------

# Str = "I know Python, Java, and C++ but not Ruby."
# pattern = r"(?<!\w)(Python|Java|C\+\+|C#|Ruby|JavaScript|Go|Rust|Swift|Kotlin)(?!\w)"
# langs = re.findall(pattern,Str,re.IGNORECASE)

# print(langs)
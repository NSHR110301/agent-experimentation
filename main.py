import csv

from core.engine import classify_email
from core.rules import rules

with open("data/emails.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        label = classify_email(row["subject"], row["body"], rules)
        print(f"{row['subject']} → {label}")

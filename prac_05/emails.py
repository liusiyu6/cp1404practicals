"""
Estimated time: 40 minutes
Actual time: 73 minutes
"""

email_to_name = {}

email = input("Email: ").strip()
while email != "":
    # Extract potential name from email
    username = email.split('@')[0]
    name_parts = username.replace('.', ' ').replace('-', ' ').split()
    potential_name = ' '.join(name_parts).title()

    confirmation = input(f"Is your name {potential_name}? (Y/n) ").strip().lower()

    if confirmation == "" or confirmation == "y":
        name = potential_name
    else:
        name = input("Name: ").strip().title()

    email_to_name[email] = name
    email = input("Email: ").strip()

print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")
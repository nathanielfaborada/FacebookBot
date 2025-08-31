import random
import string
import json
from pathlib import Path
from faker import Faker

fake = Faker()

def random_name():
    first = fake.first_name()
    last = fake.last_name()
    return first, last

def random_username(first, last):
    return f"{first.lower()}{last.lower()}{random.randint(1000, 9999)}"

def random_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

def save_to_json(data, filename="account/account_data.json"):
    path = Path(filename)
    if path.exists():
        accounts = json.loads(path.read_text(encoding="utf-8"))
    else:
        accounts = []
    accounts.extend(data)  
    path.write_text(json.dumps(accounts, indent=4), encoding="utf-8")

# --- Main Program ---
def generate_gmail_account(num_accounts=1):
    accounts = []
    for _ in range(num_accounts):
        first, last = random_name()
        username = random_username(first, last)
        password = random_password()

        account_data = {
            "name": f"{first} {last}",
            "gmail": f"{username}@gmail.com",
            "password": password,
        }

        print(f"Generated -> {account_data}")
        accounts.append(account_data)

    save_to_json(accounts)

if __name__ == "__main__":
    try:
        num = int(input("Ilang accounts ang gusto mong i-generate? "))
        generate_gmail_account(num)
        print(f"\n✅ {num} account(s) generated and saved to account/account_data.json")
    except ValueError:
        print("❌ Invalid number. Please enter a valid integer.")

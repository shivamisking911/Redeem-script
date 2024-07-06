import requests
import random
import string

def generate_code(length):
    chars = string.ascii_letters + string.digits
    code = ''.join(random.choice(chars) for _ in range(length))
    return code

def generate_redeem_link():
    base_url = "http://www.linkedin.com/premium/redeem/gift?_ed="
    code = generate_code(24)  # Adjust the code length as needed
    return base_url + code

def check_link_validity(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Generate a redeem link
redeem_link = generate_redeem_link()
print("Generated Redeem Link:", redeem_link)

# Check if the link works
if check_link_validity(redeem_link):
    print("The redeem link is valid and works.")
else:
    print("The redeem link is not valid or does not work.")

import random

import string

user_password = int(input("Enter the password number : "))

user_password_length = int(input("Enter the length of each password:"))



characters = string.ascii_letters + string.digits + string.punctuation

print("\nGenerated Passwords:")
# Step 2: Generate passwords
for i in range(user_password):
    password = ''.join(random.choice(characters) for _ in range(user_password_length))
    print(f"Password {i+1}: {password}")

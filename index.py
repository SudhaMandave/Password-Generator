import random
import string

# Function to generate a random password
def generate_password(length):
  string_value = string.ascii_letters + string.digits + string.punctuation
  return "".join(random.choice(string_value) for i in range(length))

try:
  # Enter the desired paasword length
  password_length = int(input("Enter password length you want: "))
  if password_length <= 0:
    raise ValueError("Password length must be a positive number.")
  password = generate_password(password_length)
  print("Your Generated Password Is: ", password)
except ValueError as e:
  print(f"Invalid input: {e}")
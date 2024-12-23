# Random Password Generator

This is a simple Python script to generate a random password. The user can specify the desired length of the password, and the script will generate a password containing a mix of letters, digits, and punctuation.

## How to Use

1. **Run the Script**: Execute the script in your Python environment.
2. **Enter Password Length**: When prompted, enter the desired length of the password.
3. **Get Your Password**: The script will generate and display a random password of the specified length.

## Code Explanation

```python
import random
import string

# Function to generate a random password
def generate_password(length):
    string_value = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(string_value) for i in range(length))

try:
    # Enter the desired password length
    password_length = int(input("Enter password length you want: "))
    if password_length <= 0:
        raise ValueError("Password length must be a positive number.")
    password = generate_password(password_length)
    print("Your Generated Password Is: ", password)
except ValueError as e:
    print(f"Invalid input: {e}")
```

## Requirements

- Python 3.x

## Running the Script

1. Make sure you have Python 3.x installed on your machine.
2. Save the script to a file, for example, `password_generator.py`.
3. Open a terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using the command: `python password_generator.py`.

Enjoy your secure and random passwords!



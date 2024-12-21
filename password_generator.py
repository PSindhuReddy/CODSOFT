import random
import string
#generates the password of users input length
def password(l):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(l))
    return password

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Generate the password
generated_password = password(password_length)

# Display the generated password
print("Generated Password:", generated_password)

import secrets
import string

def generate_password(length: int = 12) -> str:
    if length < 12:
        length = 12
    # Define the character sets
    digits = string.digits
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    symbols = '!#%*+,-.;=?_' #string.punctuation
    
    # Ensure at least one character from each set is included
    password = [
        secrets.choice(digits),
        secrets.choice(digits),
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(symbols),
    ]
    
    # Fill the rest of the password length with randomly selected characters from all sets
    for _ in range(length - len(password)):
        password.append(secrets.choice(digits + uppercase + lowercase + symbols))
    
    # Shuffle the password to ensure it's not predictable
    secrets.SystemRandom().shuffle(password)
    
    # Join the characters to form the final password string
    password = ''.join(password)
    return password

if __name__ == '__main__':
    for i in range(20):
        pw = generate_password()
        print(pw)

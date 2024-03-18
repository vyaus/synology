import os
import csv
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

def create_user(username, group):
    password = generate_password()
    print(f'synouser -add {username} "{password}" "{group} - {username}" 0 "" 0')

def create_group(groupname, members):
    print(f'synogroup --add "{groupname}" {members}')

def create_share(groupname, member, admin=None):
    if admin is not None:
        print(f'synoshare --add "{groupname} - {member}" "{groupname}" "/volume1/{groupname} - {member}" "" "@{admin},{member}" "@{groupname}" 1 0')
    else:
        print(f'synoshare --add "{groupname} - {member}" "{groupname}" "/volume1/{groupname} - {member}" "" "{member}" "@{groupname}" 1 0')

with open('list.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        group = row[0]
        admin = row[1]
        members = row[1:]
        for username in members:
            create_user(username, group)
        create_group(group, ' '.join(members))
        if len(members) > 2:
            create_group(group + "admin", admin)
            for member in members:
                create_share(group, member, group + "admin")
 
        else:
            for member in members:
                create_share(group, member)

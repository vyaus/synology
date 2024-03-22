import os
import csv
from random_password_generator import generate_password

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

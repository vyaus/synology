# Synology

The format of list.txt is as follow:

 - 1ne line for a group
 - the first field is group name
 - the second is group admin
 - the third to last field is group member

`create_groups_users_shares.py` can:

 - create groups, users, shares
 - generate random password for users
 - set proper permissions for users and groups

Group admin can read/write all members' shared folder, while members can only read each other's shared folders within the same groups.

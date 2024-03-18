# Synology

The format of list.txt is as follow:

 - one line for a group
 - the first field is group name, the second is group admin, the third to last is group members

`create_groups_users_shares.py` can:

 - create groups, users, shares
 - generate random password for users
 - set proper permissions for users and groups

Group admin can read/write all members' shared folder, while members can only read each other's shared folders within the same groups.

Group admin only exist for groups with more than 2 members.

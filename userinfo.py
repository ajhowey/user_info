#!/usr/bin/env python3

import hashlib
import os
from getpass import getpass

####
# gathering user information
####
FName = input('Enter user\'s first name:  ')
FInitial = FName[0]
MInitial = input('Enter user\'s middle initial:  ')
LName = input('Enter user\'s last name:  ')
UserName = FName + ' ' + MInitial + '. ' + LName
LoginID = FInitial.lower() + MInitial.lower() + LName.lower()

####
# setting up the salt and password
####
SALT = str(os.urandom(32).hex())
bSALT = bytes(SALT, encoding='ascii')
PASSWORD = getpass('Enter user\'s password:  ')
PASSWORD = bytes('somePassWord', encoding='ascii')

####
# hashing the password 4096 times
####
hashed_password = hashlib.pbkdf2_hmac('sha3_512', PASSWORD, bSALT, 4096, dklen=None).hex()

UserInfo = [UserName, LoginID, SALT, hashed_password]

print(UserInfo)

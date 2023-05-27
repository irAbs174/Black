'''
phpass hash verificate
developer : #ABS
'''

# Import all requirements
from passlib.hash import phpass


# validate password function
def validate_Opassword(password: str, hashed_password: str) -> bool:
    return phpass.verify(password, hashed_password)

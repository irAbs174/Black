'''
Django Pbkdf2-sha256 and Wordpress phpass Hash validator/generator
Developer : #ABS
'''

# Import necessary modules
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import check_password, make_password
from passlib.hash import phpass
from time import sleep


# Define a custom Django management command
class Command(BaseCommand):
    print('Developer: #ABS')
    help = 'For help type -help'  # Help text for the command

    # Define command arguments
    def add_arguments(self, parser):
        parser.add_argument('command', type=str, help='The password to check')

    # Define the logic of the command
    def handle(self, *args, **options):
        # Define a dictionary of available commands and their corresponding functions
        commands_dict = {
            'phpassGen': RunCommands.phpassGen,
            'pbkdf2Gen': RunCommands.pbkdf2Gen,
            'phpassCheck': RunCommands.phpassCheck,
            'pbkdf2Check': RunCommands.pbkdf2Check,
            '-help': help_function  # Use the help_function method to display the available commands
        }

        command = options['command']
        commands = input('Enter command (for help type: -help): ')
        if commands != '':
            command_func = commands_dict.get(commands)
            if command_func:
                command_func()
            else:
                print('Invalid command!')
        else:
            print('Error: Empty command!')


# Method to display available commands and their descriptions
def help_function():
    content = {
        'generate wordpress hash(phpass)': 'phpassGen',
        'generate django hash(pbkdf2-sha256)': 'pbkdf2Gen',
        'validate wordpress hash(phpass)': 'phpassCheck',
        'validate django hash(pbkdf2-sha256)': 'pbkdf2Check',
        'help': '-help'
    }
    print("Available commands:")
    for key, value in content.items():
        print(f"{key}: {value}")
    print()


# Class containing methods to generate and validate password hashes
class RunCommands:
    # Method to generate WordPress phpass hash
    @staticmethod
    def phpassGen():
        print('Wordpress phpass hash generator')
        while True:
            sleep(1.5)
            password = input('Enter password: ')
            hashC = phpass.hash(password)
            print(f"\nHash: {hashC}\n")

    # Method to generate Django pbkdf2-sha256 hash
    @staticmethod
    def pbkdf2Gen():
        print('Django pbkdf2-sha256 hash generator')
        while True:
            sleep(1.5)
            password = input('Enter password: ')
            hashC = make_password(password, salt='PDHTwqLLv7nIsw60zr767s')
            print(f"\nHash: {hashC}\n")

    # Method to validate WordPress phpass hash
    @staticmethod
    def phpassCheck():
        print('Wordpress phpass Validations Checker!')
        while True:
            sleep(1.5)
            hashC = input('Enter phpass hash: ')
            password = input('Enter password: ')
            is_valid = phpass.verify(password, hashC)
            if is_valid:
                print("\nThe password is valid!\n")
            else:
                print("\nInvalid password :(\n")

    # Method to validate Django pbkdf2-sha256 hash
    @staticmethod
    def pbkdf2Check():
        print('Django pbkdf2-sha256 Validations Checker!')
        while True:
            sleep(1.5)
            hashC = input('Enter pbkdef2-sha256 hash: ')
            password = input('Enter password: ')
            is_valid = check_password(password, hashC)
            if is_valid:
                print("\nThe password is valid!\n")
            else:
                print("\nInvalid password :(\n")
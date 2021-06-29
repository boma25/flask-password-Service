import re
import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_-+|/?><'


def generate_password(password_length):
    while True:
        if password_length < 8:
            password_length = 8
        password = ''
        for x in range(0, password_length):
            password_character = random.choice(characters)
            password += password_character
        return password


def validate_password(password):
    while True:
        if len(password) < 8:
            return 'password too short password must be 8 characters long'
        else:
            if not re.search('[A-Z]', password):
                return 'password must contain an uppercase letter'
            if not re.search('[a-z]', password):
                return 'password must contain a lowercase letter'
            if not re.search('[0-9]', password):
                return 'password must contain digits'
            if not re.search('[@_!#$%^&*()<>?/\|}{~:]', password):
                return 'password must contain special characters'
        return 'password is valid'

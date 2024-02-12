import random
import string

def get_random_password(length):
    letters_lowercase ='abcdefghijklmnopqrstuvwxyz'
    letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    punctuation = '@#$%^&*-_!=[]{}|:'
    
    random_source = letters_lowercase + letters_uppercase + numbers + punctuation
    # select 1 lowercase
    # password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    # password += random.choice(string.ascii_uppercase)
    # select 1 digit
    # password += random.choice(string.digits)
    # select 1 special symbol
    # password += random.choice(string.punctuation)

    password = ''
    # generate other characters
    for i in range(length):
        password += random.choice(random_source)
    
    validate_password = False
    for letter in password:
        if letter in letters_lowercase:
            validate_password = True
        elif letter in letters_uppercase:
            validate_password = True
        elif letter in numbers:
            validate_password = True
        elif letter in punctuation:
            validate_password = True
        if not validate_password:
            get_random_password(length)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print("First Random Password is ", get_random_password(15))
# output  qX49}]Ru!(
print("Second Random Password is ", get_random_password(15))
# Output  3nI0.V#[T

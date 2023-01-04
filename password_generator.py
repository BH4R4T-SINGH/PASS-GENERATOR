import random
import string
import argparse

banner = """
 _____________
< Here is your >
< password    >
 -------------
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\/\\
                ||----w |
                ||     ||
"""

def generate_password(length=None, random_length=False):
    # Initialize a string of characters to use for the password
    char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    # If a length is not specified and random_length is True, generate a random length between 12 and 25
    if length is None and random_length:
        length = random.randint(12, 25)

    # Generate a random password by choosing `length` random characters from `char_set`
    return ''.join(random.choice(char_set) for i in range(length))


# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", type=int, help="length of the password")
parser.add_argument("-r", "--random", action="store_true", help="generate a password with a random length")
parser.add_argument("-t", "--title", help="title for the stored password")
parser.add_argument("-s", "--store", action="store_true", help="store the generated password in a text file")
args = parser.parse_args()

# Generate a password based on the command-line arguments
if args.length:
    password = generate_password(length=args.length)
elif args.random:
    password = generate_password(random_length=True)
else:
    password = generate_password(length=16)

# Print the generated password
print(banner)
print(password)

# If the `store` argument is specified, store the password in a text file
if args.store:
    if args.title:
        # If a title is specified, use it as the file name
        filename = args.title + ".txt"
    else:
        # If no title is specified, use "password" as the file name
        filename = "password.txt"

    with open(filename, "w") as f:
        f.write(password)

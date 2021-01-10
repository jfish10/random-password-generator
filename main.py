import random
import string

print('Run this script to generate a plain-text password for your account (make sure to store it someplace safe afterwards and delete the file)\n> ')

pw_length = int(input('Enter the length of the password:\t'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp_pass = random.sample(all, pw_length)

new_pw = "".join(temp_pass)

with open('temp_pw_file.txt', 'a') as pw:
  pw.write(new_pw)


print('Success! Password created')



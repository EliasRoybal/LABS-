import hashlib
import random


# This method will generate a random password and pass the parameters with it
def pass_list_permutation(max_password_characters, min_password_characters, pass_list, num_passwords_generated):
    if num_passwords_generated < 0:  # base case
        return 1

    password_characters = '0123456789'
    password = ""
    for i in range(min_password_characters, max_password_characters):
        password = password + password.join(
            random.choice(password_characters))  # concatenates password and random password
        pass_list.add(password)  # gets current list and adds new password to it
    pass_list_permutation(max_password_characters, min_password_characters, pass_list, num_passwords_generated - 1)


# This method will read the file and split each line into the three corresponding sections
def readfile(usernames, salt_values, hash_codes):
    file = open('password_file.txt')

    for line in file:
        line = line.rstrip('\n')  # This will remove the \n from the output
        arr = line.split(",")
        usernames.append(arr[0])
        salt_values.append(arr[1])
        hash_codes.append(arr[2])
    file.close()


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))  # 1-4 8 bit bytes
    hex_dig = hash_object.hexdigest()
    return hex_dig


def main():
    usernames = []
    salt_values = []
    hash_codes = []
    readfile(usernames, salt_values, hash_codes)
    # print(usernames)
    # print(salt_values)
    # print(hash_codes)
    plist = set([])
    # plist = []
    pass_list_permutation(7, 3, plist, 994)
    # print(plist)
    for password in plist:
        i = -1
        for salt in salt_values:
            hashcode = hash_with_sha256(password + salt)  # creates hash password and salt
            i = i + 1
            if hashcode in hash_codes:  # compares hashcode with file hash codes
                print("Match found!")
                print("Username: " + usernames[i])
                print("Salt value: " + salt)
                print("Real password: " + password)
                print(" ")


main()

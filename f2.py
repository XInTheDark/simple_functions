def read_source_code(website):
    import urllib.request

    page = urllib.request.urlopen(website)
    content = page.read()
    print(content)
    content = str(content)
    file = open('source-code.txt', 'w')
    file.write(content)
    file.close()
    print("The file named 'source-code.txt' has been created and saved. The source code is stored in that file.")


def rock_paper_scissors():
    import random

    x = 0
    # rock=1
    # paper=2
    # scissors=3
    hscore = 0
    cscore = 0
    draw = 0
    while x == 0:
        comp = random.randint(1, 3)
        human = input('rock (r), paper (p) or scissors (s)? Or enter x to exit the game. Enter>>>')
        if human != 'r':
            if human != 'p':
                if human != 's':
                    if human != 'x':
                        print('Invalid entry! Exiting the game...')
                        break
        if human == 'r':
            if comp == 2:
                print('Computer wins! Rock vs Paper')
                cscore = cscore + 1
            elif comp == 1:
                print('Draw! Rock vs Rock')
                draw = draw + 1
            else:
                print('Human wins! Rock vs Scissors')
                hscore = hscore + 1
        if human == 'p':
            if comp == 1:
                print('Human wins! Paper vs Rock')
                hscore = hscore + 1
            elif comp == 2:
                print('Draw! Paper vs Paper')
                draw = draw + 1
            else:
                print('Computer wins! Paper vs Scissors')
                cscore = cscore + 1
        if human == 's':
            if comp == 1:
                print('Computer wins! Scissors vs Rock')
                cscore = cscore + 1
            if comp == 2:
                print('Human wins! Scissors vs Paper')
                hscore = hscore + 1
            else:
                print('Draw! Scissors vs Scissors')
                draw = draw + 1
        if human == 'x':
            print('Game over.')
            print('Human Score: ' + str(hscore) + '. Computer Score: ' + str(cscore) + '. Draws: ' + str(draw))
            break


def encrypt_msg(message):
    from cryptography.fernet import Fernet
    import pyperclip

    print("For this program to work, please send the file named 'pwkey' and the encrypted code to the other user.")
    key = Fernet.generate_key()
    file = open('pwkey', 'wb')
    file.write(key)
    file.close()
    print('File Generated')
    message2 = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message2)
    encrypted = encrypted.decode("ascii")
    print('Encrypted:', encrypted)
    pyperclip.copy(encrypted)
    print('Please tell the other user to input the encrypted code in the Decrypt program')
    print('(Code copied to Clipboard)')
    print("Note: Please delete the 'pwkey' file after sending it to the other user. It is for one-time use only.")


def decrypt_msg(encrypted):
    from cryptography.fernet import Fernet

    print("For this program to work, make sure you have the file named 'pwkey' in your Python folder and the encrypted "
          "code.")
    file = open('pwkey', 'rb')
    key = file.read()
    file.close()
    print('Key Retrieved')
    encrypted = bytes(encrypted, 'utf-8')
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    decrypted = decrypted.decode()
    print('Decrypted Message:')
    print(decrypted)
    print("Note: Please delete the 'pwkey' file after getting the decrypted message. It is for one-time use only.")


def sys_info():
    import os
    import platform
    import sys
    osname = os.name
    platname = platform.system()
    platrelease = platform.release()
    processor = platform.processor()
    platver = platform.version()
    machine = platform.machine()
    pyfolder = sys.executable

    # The variables below are Python info
    vinfo = sys.version_info
    version = sys.version
    apiv = sys.api_version
    cright = sys.copyright
    print('Below is Python system info')
    print('\nVersion:', version)  # \n to make a new line
    print('Version Info:', vinfo)
    print('API Version:', apiv)
    print('Python folder path:', pyfolder)
    print(cright)
    print('\nBelow is This Computer system info')
    print('Processor:', processor)
    print('\nProcessor Architecture:', machine)
    print('OS Name:', osname)
    print('Platform name:', platname)
    print('Platform Version:', platname, platrelease, '(' + str(platver) + ')')


def sort_nums(numlist: list, order):
    z = []
    numlist = str(numlist)
    y = numlist.split(',')
    for i in y:
        num = int(i)
        z.append(num)
    numlist = z
    # print(x)
    # list.sort(x)
    # print(x)
    z = []
    if order == 'a':
        list.sort(numlist)
        for j in numlist:
            num2 = str(j)
            z.append(num2)
        z = ','.join(z)
        print(z)
    elif order == 'd':
        list.sort(numlist, reverse=True)
        for j in numlist:
            num2 = str(j)
            z.append(num2)
        z = ','.join(z)
        print(z)



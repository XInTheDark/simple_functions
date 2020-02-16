def generate_insult(repeat):
    import random
    insults1 = ['fucking', 'shitty', 'arrogant', 'bad', 'boastful', 'bitchy', 'callous', 'nasty', 'bossy',
                'sucking',
                'gross', 'smelly', 'disgusting']
    insults2 = ['dung', 'shit', 'sucker', 'faeces', 'jerk', 'dunce', 'dipstick', 'wanker', 'arsehole', 'bonehead',
                'bugger',
                'dork', 'idiot']
    repeatnum = 0

    def generate():
        insultnum1 = random.randint(0, len(insults1) - 1)
        insultnum2 = random.randint(0, len(insults1) - 1)
        insult_phrase = str(insults1[insultnum1]) + ' ' + str(insults2[insultnum2])
        if str(insults1[insultnum1][0]) == 'a' or str(insults1[insultnum1][0]) == 'e' or str(
                insults1[insultnum1][0]) == 'i' or str(insults1[insultnum1][0]) == 'o' or str(
            insults1[insultnum1][0]) == 'u':
            print(f'Your insult:\nYou are an {insult_phrase}!')
        else:
            print(f'Your insult:\nYou are a {insult_phrase}!')

    while repeatnum < repeat:
        generate()
        repeatnum += 1


def calc(num1, num2, method):
    from sys import exit

    try:
        float(num1)
    except ValueError:
        print('Invalid!')
        exit()
    try:
        float(num2)
    except ValueError:
        print('Invalid!')
        exit()

    if method == '+':
        result = float(num1) + float(num2)
        if result == int(num1) + int(num2):
            result = int(num1) + int(num2)
            print('Result:', result)
        else:
            print('Result:', result)
    elif method == '-':
        result = float(num1) - float(num2)
        if result == int(num1) - int(num2):
            result = int(num1) - int(num2)
            print('Result:', result)
        else:
            print('Result:', result)
    elif method == '*':
        result = float(num1) * float(num2)
        if result == int(num1) * int(num2):
            result = int(num1) * int(num2)
            print('Result:', result)
        else:
            print('Result:', result)
    elif method == '/':
        result = float(num1) / float(num2)
        if result == int(int(num1) / int(num2)):
            result = int(int(num1) / int(num2))
            print('Result:', result)
        else:
            print('Result:', result)
    else:
        print("Invalid! Enter only '+', '-', '*' or '/'!")


def convert_emoji(message):
    words = message.split(' ')
    emoji_list = {
        ":)": "😊",
        ":(": "😢",
        ":D": "😆",
        "LOL": "😂",
        "ROFL": "🤣",
        ":|": "😶"
    }
    result = ""

    for word in words:
        result += emoji_list.get(word, word) + " "
    print(result)


def test_prime(num):
    import sys
    import math

    for i in range(2, math.ceil((math.sqrt(num)))):
        for j in range(2, math.ceil((math.sqrt(num))) + 1):
            if num % j == 0:
                print('This number is composite!')
                sys.exit()

    print('This number is prime!')


def english_cmd():
    import os

    print("Note: This cmd does not work well on non-English devices.")
    os.system('cmd')


def pingweb():
    def pingbasic():
        import ping3

        print('Starting ping. Please wait a few seconds.')
        ping3.ping('google.com')

    import ping3

    pingcount = 0
    while pingcount < 5:
        if (pingbasic()) is None:
            print('Ping successful. Ping time (in sec):')
            print(ping3.ping('google.com'))
            pingcount += 1


def calc_circle(radius, method):
    import decimal

    decimal.getcontext().prec = 50
    if method == 'area':
        calc_result = decimal.Decimal(3.14159265358979323846264338327950288419716939937510 * radius * radius)
    elif method == 'perimeter':
        calc_result = decimal.Decimal(3.14159265358979323846264338327950288419716939937510 * radius * 2)
    elif method == 'volume':
        calc_result = decimal.Decimal(3.14159265358979323846264338327950288419716939937510 * (4 / 3) * (radius ** 3))
    elif method == 'surface':
        calc_result = decimal.Decimal(3.14159265358979323846264338327950288419716939937510 * 4 * radius * radius)
    else:
        print('Invalid! Exiting program...')
        exit('Exit Successfully')

    print('Your result is', str(calc_result) + '!')


calc_circle(1, 'lol;9')

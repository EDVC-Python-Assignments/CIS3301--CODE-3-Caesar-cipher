import os,sys
from mock_input_tests import *
from code_3 import main
import random

def check_if_file_exists():
    try:
        exists = os.path.exists("code_3.py")
        assert exists == True
    except:
        sys.exit()

def test_encryption():
    check_if_file_exists()
    words = ["apple", "orange", "kiwi", "pear", "grape"]
    secret = random.choice(words)
    key = random.randint(1,4)
    set_keyboard_input([secret,key])

    main()
    output = get_display_output()

    assert output == [
        "\nCaesar Cipher - Program",
        "\nEnter the word to encrypt: ",
        "Enter your key: ",
        "\nThe encrypted word is "+"".join([chr(ord(x)+key) for x in secret])+"\n"
    ]

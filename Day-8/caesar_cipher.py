alphabeth = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Former code
'''def encrypt(plain_text, shift_amount):
    cipher_text = " "
    for letter in plain_text:
        position = alphabeth.index(letter)
        new_position = position + shift_amount
        new_letter = alphabeth[new_position]
        cipher_text += new_letter
    print(f"The encrypted text is {cipher_text}")


def decrypt(plain_text, shift_amount):
    decipher_text = " "
    for letter in plain_text:
        position = alphabeth.index(letter)
        new_position = position - shift_amount
        new_letter = alphabeth[new_position]
        decipher_text += new_letter
    print(f"The decoded text is {decipher_text}")

if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(plain_text = text, shift_amount = shift)'''

def caeser(start_text, shift_amount, cipher_direction):
    end_text = " "
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabeth:
            position = alphabeth.index(char)
            new_position = position + shift_amount
            end_text += alphabeth[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")

# figure out if the user wants to continue
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    shift = shift % 26
    caeser(start_text = text, shift_amount = shift, cipher_direction = direction)

    result = input("Type 'yes' if you want to go again, otherwise Type 'no'. \n")
    if result == "no":
        should_continue = False
        print("Goodbye")

    

 
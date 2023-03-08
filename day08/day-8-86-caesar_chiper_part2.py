alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#encrypt function
def encrypt(plain_text, shift_amount):
    print("Welcome to ENCRYPT")
    cipher_text = ""
    for letter in plain_text:
        if alphabet.index(letter)+shift_amount > len(alphabet):
            shift_overlap = alphabet.index(letter)+shift_amount - (len(alphabet)-1)
            cipher_text = cipher_text + alphabet[shift_overlap-1]

        else:
            cipher_text = cipher_text + alphabet[alphabet.index(letter)+shift_amount]    

    print(f"The encoded text is {cipher_text}")

#decrypt function
def decrypt(encoded_text, shift_amount):
    print("Welcome to DECRYPT")
    cipher_text = ""
    for letter in encoded_text:
        if alphabet.index(letter)-shift_amount < 0:
            shift_overlap = alphabet.index(letter)-shift_amount
            cipher_text = cipher_text + alphabet[len(alphabet)+(shift_overlap-1)]
        else:
            cipher_text = cipher_text + alphabet[alphabet.index(letter)-shift_amount]    

    print(f"The decrypted text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(encoded_text=text, shift_amount=shift)

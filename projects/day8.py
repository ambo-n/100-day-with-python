alphabet = ["a", "b", "c", "d", "e", "f", "g", 
            "h", "i", "j", "k", "l", "m", "n", 
            "o", "p", "q", "r", "s", "t", "u", 
            "v", "w", "x", "y", "z"]
print("Welcome to my Caesar Cipher")
def caesar(direction, original_text, shift_amount):
    output_text=""
    if direction == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shift_index = alphabet.index(letter)+shift_amount
            shift_index %= len(alphabet)
            output_text+=alphabet[shift_index]
        else:
            output_text+= letter
    print(f"Here is your {direction}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text=input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(direction,text,shift)
    status = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    if status == 'yes':
        continue
    else:
        should_continue=False
        print("Goodbye")

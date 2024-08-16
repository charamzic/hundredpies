alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cypher(direction: str, text: str, shift_amount: int):
    output_text = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in text:
        if letter in alphabet:
            shifted_pos = alphabet.index(letter) + shift_amount
            shifted_pos %= len(alphabet)
            output_text += alphabet[shifted_pos]
        else:
            output_text += letter

    print(f"Here is the {direction}d result: {output_text}")
    print("===============================================")


should_continue = True

while should_continue:
    direction = input(
        "Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))

    caesar_cypher(direction, text, shift)

    restart = input("Press ENTER to continue, or type 'exit' to exit.\n")
    if restart == "exit":
        should_continue = False
        print("Goodbye then.")

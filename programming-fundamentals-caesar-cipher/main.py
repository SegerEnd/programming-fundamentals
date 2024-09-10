
# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encode( text, shift):
    """ Encode the text by shifting the letters in the alphabet """
    result = ""

    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += letter

    return result

def decode( text, shift):
    """ Decoding is encoding with a negative shift """
    return encode( text, -shift)

def main():
    session = True

    while session:
        result = ""
        action = input("Voer de gewenste actie in: encode of decode: ")
        text = input("Voer de tekst in die je wilt versleutelen of ontsleutelen: ")
        shift = int(input("Geef het aantal posities op waarmee je de letters wilt verschuiven (shift number): "))

        if action == "encode":
            result = encode( text, shift)
        elif action == "decode":
            result = decode( text, shift)

        print(result)

        session = input("Wil je nog een keer? (ja/nee): ").strip()[0].lower() == "j"

if __name__ == "__main__":
    main()

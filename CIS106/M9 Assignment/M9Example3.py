# Example 3 - String Case Converter

def convert_string(text):
    if text.islower():
        return text.upper()
    else:
        return text.lower()

while True:
    original = input("Enter a string (or STOP to quit): ")

    if original.upper() == "STOP":
        break

    new_string = convert_string(original)

    print(f"Original String: {original}")
    print(f"New String: {new_string}")
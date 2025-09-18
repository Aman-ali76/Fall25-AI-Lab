string = "Kuch Bhi; Kuch, Bhi!"
new_string = ""
for char in string:
    if char.isalpha() or char == " ":
        new_string += char

print(new_string)
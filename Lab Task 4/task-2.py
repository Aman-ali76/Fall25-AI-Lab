
def bubble_sort_words(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ord(words[j][0]) > ord(words[j+1][0]):
                words[j], words[j+1] = words[j+1], words[j]
    return words

def bubble_sort_chars(chars):
    n = len(chars)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ord(chars[j]) > ord(chars[j+1]):
                chars[j], chars[j+1] = chars[j+1], chars[j]
    return chars


# text = input("Enter a string: ")
text = "I am Rasikh"

words = text.split(" ")
sorted_words = bubble_sort_words(words)

chars = list(text.replace(" ", "")) 
sorted_chars = bubble_sort_chars(chars)

print("\nOriginal String: ", text)
print("Sorted by Words : ", " ".join(sorted_words))
print("Sorted by Characters: ", "".join(sorted_chars))

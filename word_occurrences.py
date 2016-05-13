"""
hi rohit
"""
sentence = input("enter any sentence:")
frequency_words = {}
words = sentence.split()
for word in words:
    if word in frequency_words:
        frequency_words[word] += 1
    else:
        frequency_words[word] = 1
print("Text : ", sentence)
for word in sorted(frequency_words):
    print("{:<} : {} ".format(word, frequency_words[word]))



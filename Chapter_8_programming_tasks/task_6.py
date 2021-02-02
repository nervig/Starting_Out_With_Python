read_text = open("text.txt", "r")
sentence = 0
words = 0
for line in read_text:
    print(line)
    sentence += 1
    words += len(line.split())
print(sentence)
print(words)
average_words_in_sentence = words / sentence
print(average_words_in_sentence)
read_text.close()
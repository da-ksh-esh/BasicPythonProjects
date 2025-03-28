from textblob import TextBlob

words = ["Arrtificial", "Intelliggence"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))

print("Wrong words: ", words)
print("Correct Words are: ")

for i in corrected_words:
    print(i.correct(), end = ' ')
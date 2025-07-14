N = int(input())

words = []
for i in range(N):
    words.append(input())


unique_words = list(set(words))
unique_words.sort(key=lambda word: (len(word),word))    #lamda식으로 word가 key, len(word)와word

for word in unique_words:
    print(word)

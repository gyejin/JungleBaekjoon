N = int(input())

words = []
for i in range(N):
    words.append(input())


unique_words = list(set(words))
unique_words.sort(key=lambda word: (len(word),word))    #파이썬은 튜플을 비교할 때, 첫 번째 요소부터 비교하고 그게 같으면 두 번째 요소를 비교

for word in unique_words:
    print(word)

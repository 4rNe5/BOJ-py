word = input()
alp = list(range(97, 123))

for vocab in alp:
    print(word.find(chr(vocab)))
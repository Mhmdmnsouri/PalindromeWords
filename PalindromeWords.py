word = input('Please enter your word: ').lower()
letters = []

for i in range(len(word)):
    letters.append(word[i])

letters.reverse()
reverseWord = ''.join(letters)

if reverseWord == word:
    print('%s is Palindrome :)' % (word))
else:
    print('%s is not Palindrome :(' % (word))

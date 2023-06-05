# build a python automation to receive word from the user
# send http request to this link:
# https://api.dictionaryapi.dev/api/v2/entries/en/<word>
# search for the definitions and word keys
# insert them text file using the commands you learned

import requests

word = input('please enter a word')
print(word)

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word
res = requests.get(url)
word_data = res.json()
print(word_data[0]['word'])
print(word_data[0]['meanings'][0]['definitions'][0]['definition'])
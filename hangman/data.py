import json
import os
import random

def select_catgory():
    ''' let user select catagory and randomly choose the word
        Return word, catagory, hint '''

    catagories = load_catagory()
    print('    Select Catagory : ')
    for i, catagory in enumerate(catagories):
        print(f"      {i+1}. {catagory.split('.')[0]}")
    select = int(input(f'    Enter (1-{len(catagories)}) : '))
    words = load_words(catagories[select - 1])
    word = random.choice(words)
    return word['word'], catagories[select-1].split('.')[0], word['hint']

def load_words(filename):
    ''' return all words and hint for each words '''

    words = []
    with open(os.path.join('Words', filename), 'r') as f:
        data = json.load(f)
        words = data['words']
    return words

def load_catagory():
    ''' return all catagory in Words directory '''

    catagories = []
    for filename in os.listdir('Words'):
        catagories.append(filename)
    return catagories

def add_word():
    ''' add new catagory and dump to json file '''

    data = {}
    catagory = str(input('Enter catagory : '))
    data['catagory'] = catagory
    data['words'] = []
    print()
    while True:
        new_word = {}
        new_word['word'] = str(input('Enter word ["DONE" to exit] : '))
        if new_word['word'] == 'DONE':
            break
        new_word['hint'] = str(input('Enter hint :'))
        data['words'].append(new_word)

    with open(os.path.join('Words', f'{catagory}.json'), 'w') as f:
        json.dump(data, f)
        print(f'Dumped to {f.name}')

if __name__ == '__main__':
    add_word()
    # print(load_catagory())
    # print(select_catgory())
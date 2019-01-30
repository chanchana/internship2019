import random

def input_error(string, guessed):
    ''' validate input, return None if valid else return error string '''

    if len(string) == 0:
        return 'Type some letter'
    elif len(string) > 1:
        return 'Guess only one letter'
    elif not string.isalpha():
        return 'Can guess only letter'
    elif string in guessed:
        return 'You already guessed that letter'
    else:
        return None

class Hangman:
    ''' hangeman ui '''

    def __init__(self, lives, word, catagory, hint):
        ''' init hangman object '''

        self.score = 0
        self.lives = lives
        self.streak = 0
        self.word = word
        self.catagory = catagory
        self.hint = hint
        self.guessed = []
        self.valid = True

    def guess(self):
        ''' ui for getting new letter '''

        print(f'    Your guess')
        string = str(input('>>> ')).upper()
        error = input_error(string, self.guessed)
        while error:
            self.valid = False
            self.show()
            print(f'    Your guess [ {error}! ]')
            string = str(input('>>> ')).upper()
            error = input_error(string, self.guessed)
        self.valid = True
        self.guessed.append(string)
        return string

    def win(self):
        ''' win ui '''

        print('      ------ Congratulation You Win!! ------')
        input()

    def gameover(self):
        ''' gameover ui '''

        print('      ------------ x GAME OVER x -----------')
        input()
    
    def show(self):
        ''' show ui '''

        self.print_header(0)
        self.print_man()
        self.print_word()

    def update(self, add_score):
        ''' show ui that adding score happening '''

        self.score += add_score
        self.print_header(add_score)
        self.print_man()
        self.print_word()

    def print_header(self, add_score):
        ''' print header ui '''

        add_score_string = '' if add_score == 0 else f'(+{add_score} points)'
        head = f'''
        ---------------------[Terminal Man]---------------------

        Catagory : {self.catagory}
        Hint     : {self.hint}

        Score  : {self.score}   {add_score_string}
        Streak : {self.streak}
        Lives  : {'|||||||'[0:self.lives]}

        '''
        print(head)

    def print_word(self):
        ''' print word holder [_ _ _ _ _ _] and replace woth the correct letter '''

        show_word = '    '
        for i in range(len(self.word)):
            if not self.word[i].isalpha():
                show_word += '   '
            elif self.word[i] not in self.guessed:
                show_word += ' _'
            else:
                show_word += ' ' + self.word[i]

        show_guessed = list(filter(lambda x: x not in list(self.word), self.guessed))
        print(show_word)
        print('    Wrong guessed : ' + ' '.join(show_guessed))
        print('')


    def print_man(self):
        ''' print hangman by getting current lives'''

        # setup arm / leg / body
        body = ['/', '\\', '/', '/', '\\', '\\', '||']
        # setup face, message
        face = self.hangman_face()
        message = self.hangman_message()
        # remove the loose part
        for i in range(7 - self.lives):
            body[i] = ' '
        # string
        man = f'''
             |
             |
            ({face})  <( {message} )
            {body[0]}{body[6]}{body[1]}
             {body[3]}{body[5]}
            {body[2]}  {body[4]}
        '''
        print(man)

    def hangman_face(self):
        ''' return hangman face of each round '''

        faces = ['XX', 'TT', 'OO', 'UU', 'OO', ';;', 'OO', '^^']
        if self.streak > 0:
            return '^^'
        else:
            return faces[self.lives]

    def hangman_message(self):
        ''' return hangeman message of each round '''

        messages = ['...',
                    '... your last chance...',
                    'Nevermind',
                    'Well, I still can walk',
                    'Oh no!',
                    'Just.. Help me',
                    'What! My arm has gone!',
                    'Hello! I\'m totally fine!']
        correct_messages = ['Wow! You got it', 'Keep going!', 'Fantastic!']
        if not self.valid:
            return 'Try again'
        elif self.streak > 0:
            return random.choice(correct_messages)
        else:
            return messages[self.lives]
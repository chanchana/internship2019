from ui import Hangman
from data import select_catgory

MAX_LIVES = 7
DEFAULT_SCORE = 100

def play(word, catagory, hint):
    ''' start playing '''

    def gameover():
        ''' check if lives is zero '''

        return True if hangman.lives == 0 else False
    
    def win():
        ''' check if player win '''

        for char in words:
            if char not in hangman.guessed:
                return False
        return True

    def score(letter):
        ''' check letter that player guessed and calculate adding score 
            return score from that round '''

        points = 0
        if letter in words:
            # correct
            hangman.streak += 1
            points = DEFAULT_SCORE * hangman.streak
        else:
            # incorrect
            hangman.lives -= 1
            hangman.streak = 0
            points = 0
        return points

    def win_score():
        ''' final addition score for lives lelf '''
        return hangman.lives * 1000

    # list of all letter in word
    words = list(filter(lambda x: x.isalpha(), list(set(word))))
    # setup hangeman ui
    hangman = Hangman(MAX_LIVES, word, catagory, hint)
    hangman.show()
    while not gameover() and not win():
        letter = hangman.guess()
        add_score = score(letter)
        hangman.update(add_score)
        # check player status
        if win():
            hangman.update(win_score())
            hangman.win()
        if gameover():
            hangman.gameover()

if __name__ == '__main__':
    word, catagory, hint = select_catgory()
    play(word, catagory, hint)
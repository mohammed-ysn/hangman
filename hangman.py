class Hangman:
    def __init__(self):
        self.word = self.get_word()

        self.correct_letters = dict.fromkeys(self.word, False)

        lives = 7

        while lives > 0 and any(not correct for correct in self.correct_letters.values()):
            self.display_slots()

            guess = input('Guess: ').upper()

            if guess in self.word:
                print(f'{guess} is correct!')
                self.correct_letters[guess] = True
            else:
                print(f'{guess} is incorrect!')
                lives -= 1

        if lives == 0:
            print('Hangman! No more lives left...')
        else:
            print(f'You correctly guessed the word: {self.word}')

    def name_input(self, num):
        return input(f'Player {num} name: ')

    def get_word(self):
        return input('Word: ').upper()

    def display_slots(self):
        msg = ''

        for letter in self.word:
            msg += letter if self.correct_letters[letter] else '_'

        print(msg)


def main():
    Hangman()


if __name__ == '__main__':
    main()

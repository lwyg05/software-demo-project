import random

class GithubWordGame:
    def __init__(self):
        self.words = [
            'repository',
            'commit',
            'branch',
            'merge',
            'pull request',
            'issue',
            'fork',
            'clone',
            'collaborator',
            'workflow',
            'API',
            'CI/CD',
            'markdown',
            'git',
            'node',
            'package'
        ]
        self.chosen_word = random.choice(self.words)
        self.guesses = []
        self.lives = 6

    def display_word(self):
        displayed_word = ''.join([letter if letter in self.guesses else '_' for letter in self.chosen_word])
        return displayed_word

    def make_guess(self, guess):
        if guess in self.guesses:
            return "You've already guessed that word!"
        self.guesses.append(guess)
        if guess not in self.chosen_word:
            self.lives -= 1
            return 'Incorrect! Lives left: {}'.format(self.lives)
        return 'Correct!'

    def is_game_over(self):
        if self.lives <= 0:
            return True, 'Game Over! The word was: {}'.format(self.chosen_word)
        if all(letter in self.guesses for letter in self.chosen_word):
            return True, 'Congratulations! You guessed the word: {}'.format(self.chosen_word)
        return False, ''

    def play(self):
        print("Welcome to the GitHub Word Guessing Game!")
        while True:
            print(self.display_word())
            guess = input("Make a guess: ")
            response = self.make_guess(guess)
            print(response)
            game_over, message = self.is_game_over()
            if game_over:
                print(message)
                break


if __name__ == "__main__":
    game = GithubWordGame()
    game.play()
    

"""
    Bulls and cows. Logic game.
    Rule: number is setted. Number set is MAX_DIGIT from 1 to MAX_DIGIT.
    Number has DIGITS_COUNT places.
    DIGITS_COUNT < MAX_DIGIT.
"""

import random

MAX_DIGIT = 5
DIGITS_COUNT = 3
GUESS_ENTER = f"Угадай число с {DIGITS_COUNT} цифрами и цифры в диапазоне 1-{MAX_DIGIT}"
GUESS = "Введи число "
BULLS_COWS = "%d быков и %d коров"
#GUESS_ENTER = f"Guess number with {m} digits and digit in range 1-{N}"
#BULLS_COWS = "%d bulls and %d cows"

class BullCowGen:
    def __init__(self, m, N):
        self.digits = m
        self.max_digit = N
        generate_lst = list(range(1, self.max_digit+1))
        self.num = random.sample(generate_lst, self.digits)

    def check_guess(self, guess):
        cows, bulls = 0, 0
        for i in range(self.digits):
            digit = guess % 10
            if digit == self.num[-1-i]:
                bulls += 1
            elif digit in self.num:
                cows += 1
            guess = (guess - digit) // 10
        return bulls, cows

    def get_number(self):
        num = 0
        for d in self.num:
            num *= 10
            num += d
        return num

def getGuess(digit_count):
    guess = ''
    while len(guess) != digit_count or not guess.isdigit():
        guess = input(GUESS)
    return guess


if __name__ == "__main__":
    num = BullCowGen(DIGITS_COUNT, MAX_DIGIT)
    print(GUESS_ENTER)
    #print(num.get_number())
    attempts = 0
    while True:
        guess = int(getGuess(DIGITS_COUNT))
        assert guess // 10**(DIGITS_COUNT-1) != 0
        attempts += 1
        bulls, cows = num.check_guess(guess)
        print(BULLS_COWS % (bulls, cows))
        if bulls == DIGITS_COUNT:
            #print("You guesed! The number was", num.num, "Attempts were", attempts)
            print("Ты угадал! Число было", num.get_number(), "Попыток было", attempts)
            break
        
        

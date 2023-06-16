import random
from colorama import init, Fore, Back, Style

# initialie colorama
init(autoreset=True)


with open("wordle_list.txt", "r") as f:
    """convert words to array"""
    words = [line.strip() for line in f.readlines()]


def choose_random_word():
    """choose random word from words array"""
    return words[random.randint(0, len(words) - 1)]


def check_guess(guess, word):
    """compare guess to actual word

    Args:
        guess (str): guess made by user
        word (str): actual word 

    Returns:
        lst: return list describing accuracy of guess 
    """
    list_guess = list(guess)
    list_word = list(word)
    output = []
    for i in range(len(guess)):
        if list_guess[i] == list_word[i]:
            output.append(2)
        elif list_guess[i] in list_word:
            j = list_word.index(list_guess[i])
            output.append(1)
            list_word[j] = None
        else:
            output.append(0)
    return output


def feasible_guess(usr_guess):
    if len(usr_guess) == 5 and usr_guess.isalpha():
        return True
    return False


if __name__ == '__main__':
    selected_word = choose_random_word()
    correct = False
    op = []
    while correct == False:
        print('')
        usr_guess = input('enter your guess: ').casefold()
        if feasible_guess(usr_guess):
            if check_guess(usr_guess, selected_word) == [2, 2, 2, 2, 2]:
                print(Back.GREEN + 'Correct' + ' the word was ' + selected_word)
                # guesses_list.append(check_guess(usr_guess, selected_word))
                correct == True
                break
            else:
                guess = check_guess(usr_guess, selected_word)
                usr_guess_list = list(usr_guess)
                for i in range(len(usr_guess_list)):
                    if guess[i] == 0:
                        op.append('')
                        op.append(usr_guess_list[i].upper())
                    elif guess[i] == 1:
                        op.append(Fore.YELLOW)
                        op.append(usr_guess_list[i].upper())
                    else:
                        op.append(Fore.GREEN)
                        op.append(usr_guess_list[i].upper())
                print()
                op.append('\n')
                for i in range(1, len(op), 2):
                    print(op[i-1] + op[i], end='')
                print()
        else:
            print(
                Back.RED + "guess must be only contain alphabets and must be 5 characters long")

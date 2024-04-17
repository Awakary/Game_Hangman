import random


def load_words(file_name):

    """Loads words from file"""

    with open(file_name, 'r', encoding='utf-8') as file:
        words = [i.strip() for i in file.readlines()]
        return words


def choose_word(words):

    """Chooses word from loaded words"""

    return random.choice(words)


def show_word(open_letters):

    """Prints hide/open letters"""

    print(' '.join(open_letters))


def draw_man(count_mistakes):

    """Draws man based on count_mistakes"""

    man = ['_____\n', '  |  \n',  '  0 \n',  ' \\', '|', '/\n', '  |  \n', ' /', ' \\\n']
    draw_index = count_mistakes + 2
    for i in man[:draw_index]:
        print(i, end='')
    print()


def is_valid(user_letter):

    """Validates entered symbols"""

    if len(user_letter) == 0:
        print('Не введено никаких символов')
        return False
    elif len(user_letter) > 1:
        print('Введено больше одного символа')
        return False
    elif not 1072 <= ord(user_letter) <= 1103:
        print('Такой буквы нет в русском алфавите')
        return False
    return True


def is_used_letter(user_letter, used_letters):

    """Checks for letter in used_letters"""

    if user_letter in used_letters:
        print('Вы уже называли эту букву')
        return True
    return False


def calculate_count_mistakes(user_letter, hidden_word, count_mistakes):

    """Calculates_count_mistakes"""

    if user_letter not in hidden_word:
        count_mistakes += 1
    return count_mistakes


def update_open_letters(open_letters, user_letter, hidden_word):

    """Updates_open_letters"""

    for i in range(len(hidden_word)):
        if hidden_word[i] == user_letter:
            open_letters[i] = user_letter


def play(available_words):

    """The game process"""

    hidden_word = choose_word(available_words)
    open_letters = ['_'] * len(hidden_word)
    used_letters = []
    count_mistakes = 0
    print('Игра началась! Слово загадано!')
    while True:
        show_word(open_letters)
        user_letter = input('Введите пожалуйста букву ').lower()
        if is_valid(user_letter) and not is_used_letter(user_letter, used_letters):
            used_letters.append(user_letter)
            count_mistakes = calculate_count_mistakes(user_letter, hidden_word, count_mistakes)
            update_open_letters(open_letters, user_letter, hidden_word)
        print('Совершено ошибок - ', count_mistakes)
        draw_man(count_mistakes)
        if open_letters == list(hidden_word):
            print('Поздравляем, Вы выиграли')
            break
        elif count_mistakes == 7:
            print('К сожалению, Вы проиграли')
            print('Слово - ', hidden_word)
            break


if __name__ == '__main__':
    while True:
        command = input('Начать игру - введите 1, выйти из приложения - введите 2 ')
        if command == '1':
            file_name = 'dictionary.txt'
            available_words = load_words(file_name)
            play(available_words)
        elif command == '2':
            print('Приложение закрыто, спасибо за игру!')
            break
        else:
            print('Введена некорректная команда')













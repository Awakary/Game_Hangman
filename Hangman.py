import random

dictionary = ('разработчик', 'компьютер', 'фреймворк', 'контейнер', 'приложение')


class DrawMan:

    def __init__(self):
        self.actions = ['_____', '  |  ',]

    def head(self):
        self.actions.append('  0  ')

    def limb(self, direction, part):
        if part == 'hand':
            self.actions[3] = ' \|  '  if direction == 'left' else ' \|/ '
        else:
            if direction == 'left':
                self.actions.append(' /   ')
            else:
                self.actions[-1] = ' / \\'

    def body(self):
        self.actions.extend(['  |  '] * 2)

    def picture(self, count_mistakes):
        match count_mistakes:
            case 1:
                self.head()
            case 2:
                self.body()
            case 3:
                self.limb('left', 'hand')
            case 4:
                self.limb('right', 'hand')
            case 5:
                self.limb('left', 'leg')
            case 6:
                self.limb('right', 'leg')


class Word:

    def __init__(self, dictionary):
        self.hidden = random.choice(dictionary)
        self.open_letters = ['_'] * len(self.hidden)
        self.used_letters = []

    def show(self):
        print(' '.join(self.open_letters))

    def validation_letter(self, user_letter):
        if not 1072 <= ord(user_letter) <= 1103:
            print('Такой буквы нет в русском алфавите')
            return False
        if user_letter in self.used_letters:
            print('Вы уже называли эту букву')
            return False
        return True


    def guess(self, count_mistakes, man):
        while True:
            user_letter = input('Введите пожалуйста букву ').lower()
            if self.validation_letter(user_letter):
                 break
        if user_letter in self.hidden:
            for i in range(len(self.hidden)):
                if self.hidden[i] == user_letter:
                    self.open_letters[i] = user_letter
        else:
           count_mistakes += 1
           man.picture(count_mistakes)
        self.used_letters.append(user_letter)
        print(*man.actions, sep='\n')
        print('Совершено ошибок - ', count_mistakes)
        return count_mistakes

if __name__ == '__main__':
    count_mistakes = 0
    while True:
        command = input('Начать игру - введите 1, выйти из приложения - введите 2 ')
        if command == '1':
            word = Word(dictionary)
            man = DrawMan()
            print('Игра началась! Слово загадано!')
            while True:
                word.show()
                count_mistakes = word.guess(count_mistakes, man)
                if word.open_letters == list(word.hidden):
                    print('Поздравляем, Вы выиграли')
                    break
                if count_mistakes == 6:
                    print('К сожалению, Вы проиграли')
                    print('Слово - ', word.hidden)
                    break

        elif command == '2':
            print('Приложение закрыто, спасибо за игру!')
            break

        else:
            print('Введена некорректная команда')


















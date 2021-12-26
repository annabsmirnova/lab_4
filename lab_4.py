class Sport:

    def get_injured(self):
        self.energy -= 40
        print('Получил травму')

    def win(self):
        self.level += 1
        print('Энергия -', self.energy, ', уровень -', self.level)

    def recovery(self):
        self.energy += 20
        print('Отдохнул и восстановился')


class Badminton(Sport):

    def __init__(self, name, level, speed):
        self.name = name
        self.level = level
        self.health = 10
        self.energy = 100
        self.speed = speed
        print(f'Меня зовут {self.name}, я занимаюсь бадминтоном, у меня {self.level} уровень.')

    def train(self, hours_of_training):
        self.energy -= hours_of_training * 10
        self.speed += hours_of_training
        print(f'Тренировался {hours_of_training} часов')

    def compete(self, qualities_of_opponent):
        if self.speed + self.energy > qualities_of_opponent:
            self.energy -= 20
            print('Победа!')
            return self.win()
        elif self.speed + self.energy < qualities_of_opponent:
            self.energy -= 20
            print('Проигрыш!')
        else:
            self.energy -= 20
            print('Ничья!')


class Gymnastic(Sport):

    def __init__(self, name, level, power):
        self.name = name
        self.level = level
        self.health = 10
        self.energy = 100
        self.power = power
        print(f'Меня зовут {self.name}, я занимаюсь гимнастикой, у меня {self.level} уровень.')

    def train(self, hours_of_training):
        self.energy -= hours_of_training * 10
        self.power += hours_of_training
        print('Потренировался.')

    def get_a_new_skill(self, needed_for_a_new_skill):
        if self.power + self.energy > needed_for_a_new_skill:
            print('Получил новый навык!')
            return self.win()
        else:
            print('Недостаточно ресурсов для получения нового навыка.')


class Basketball(Sport):
    def __init__(self, name, level, teamwork):
        self.name = name
        self.level = level
        self.health = 10
        self.energy = 100
        self.teamwork = 20
        print(f'Меня зовут {self.name}, я занимаюсь баскетболом, у меня {self.level} уровень.')

    def train(self, hours_of_training):
        self.energy -= hours_of_training * 10
        self.teamwork += hours_of_training
        print('Потренировался')

    def compete(self, level_of_opponent, qualities_of_opponent):
        if level_of_opponent == self.level:
            if self.teamwork + self.energy > qualities_of_opponent:
                self.energy -= 20
                print('Победа!')
                return self.win()
            elif self.teamwork + self.energy < qualities_of_opponent:
                self.energy -= 20
                print('Проигрыш!')
            else:
                self.energy -= 20
                print('Ничья!')
        else:
            print('Нельзя играть с соперником, у которого другой уровень')


class Swimming(Sport):
    def __init__(self, name, level, endurance, best_time):
        self.name = name
        self.level = level
        self.health = 10
        self.energy = 100
        self.endurance = endurance
        self.best_time = best_time
        print(f'Меня зовут {self.name}, я занимаюсь плаванием, у меня {self.level} уровень.')

    def train(self, hours_of_training):
        self.energy -= hours_of_training * 10
        self.endurance += hours_of_training
        print('Потренировался')

    def compete(self, qualities_of_opponent):
        if self.endurance + self.energy > qualities_of_opponent:
            self.energy -= 20
            print('Победа!')
            return self.win()
        elif self.endurance < qualities_of_opponent:
            self.energy -= 20
            print('Проигрыш!')
        else:
            self.energy -= 20
            print('Ничья!')

    def beat_a_personal_best(self, time):
        if time < self.best_time:
            self.level += 1
            self.best_time = time
            print('Установлен новый личный рекорд -', self.best_time,'!')
        else:
            print('Личный рекорд не установлен!')
        self.energy -= 20


class Wrestling(Sport):
    def __init__(self, name, level, reaction):
        self.name = name
        self.level = level
        self.health = 10
        self.energy = 100
        self.reaction = reaction
        print(f'Меня зовут {self.name}, я занимаюсь борьбой, у меня {self.level} уровень.')

    def train(self, hours_of_training):
        self.energy -= hours_of_training * 10
        self.reaction += hours_of_training
        print('Потренировался.')

    def battle(self, level_of_oppenent, qualities_of_opponent):
        if self.level == level_of_oppenent:
            if self.reaction + self.energy > qualities_of_opponent:
                self.energy -= 20
                print('Победа!')
                return self.win()
            else:
                self.energy -= 20
                print('Проигрыш!')
        else:
            print('Нельзя выходить на бой с противником другого уровня')


badminton_player = Badminton('Bob', 5, 20)
print('Энергия -', badminton_player.energy, ', скорость -', badminton_player.speed)
badminton_player.get_injured()
print('Энергия -', badminton_player.energy)
qualities_of_opponent = 60
print(f'Соревнования с противником, у которого (энергия + скорость) = {qualities_of_opponent}:')
badminton_player.compete(qualities_of_opponent)
print()

gymnast = Gymnastic('Sam', 9, 20)
print('Энергия -', gymnast.energy, ', сила -', gymnast.power)
gymnast.train(3)
print('Энергия -', gymnast.energy, ', сила -', gymnast.power, ', уровень -', gymnast.level)
needed_for_a_new_skill = 91
print(f'Для освоения навыка (энергия + сила) должны быть больше {needed_for_a_new_skill}')
gymnast.get_a_new_skill(needed_for_a_new_skill)
print()

basketball_player = Basketball('Tom', 1, 5)
basketball_player.train(2)
print('Энергия -', basketball_player.energy, ', работа в команде -', basketball_player.teamwork, ', уровень -',
      basketball_player.level)
qualities_of_opponent = 120
print(f'Игра с противником, у которого такой же уровень, а (энергия + работа в команде) = {qualities_of_opponent}:')
basketball_player.compete(1, qualities_of_opponent)
print()

swimmer = Swimming('Liz', 11, 25, 2.6)
print('Энергия -', swimmer.energy, ', выносливость -', swimmer.endurance, ', уровень -', swimmer.level)
print('Попытаться побить личный рекорд -', swimmer.best_time)
swimmer.beat_a_personal_best(2.5)
print('Энергия -', swimmer.energy, ', выносливость -', swimmer.endurance, ', уровень -', swimmer.level)
print()

wrestler = Wrestling('Ann', 4, 9)
print('Энергия -', wrestler.energy, ', реакция -', wrestler.reaction, ', уровень -', wrestler.level)
qualities_of_opponent = 80
level_of_opponent = 4
print(f'Бой с противником того же уровня и с (реакция + энергия) = {qualities_of_opponent}')
wrestler.battle(level_of_opponent, qualities_of_opponent)
wrestler.recovery()
print('Энергия -', Wrestler.energy, ', реакция -', Wrestler.reaction, ', уровень -', Wrestler.level)

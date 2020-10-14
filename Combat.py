import random


class Warrior:

    def __init__(self, name, health=100, strength=40, agility=40, luck=50):
        self.name = name
        self.hit = 1
        self.health = health
        self.hp = self.health
        self.strength = strength
        self.agility = agility
        self.luck = luck
        self.chance = 1
        self.fate = 1
        self.min = 1
        self.max = 100

    def make_damage(self):
        self.min = (self.luck/100) * self.strength
        self.max = self.strength
        self.hit = random.randint(self.min, self.max)
        return self.hit

    def take_damage(self, other):
        self.hp -= other.hit
        return self.hp

    def dodge(self):    # шанс увернуться от удара
        chance = self.chance
        fate = self.fate
        self.chance = (self.agility + self.luck)/2
        self.fate = random.randint(0, 100)
        if chance > fate:       # што за хуйня с этим условием????!1
            return True
        else:
            return False
        # Метод dodge отрабатывает криво. Условие не выполняется.
        # Избегание или получение удара не зависит от соотношения chance > fate
        # где-то ошибка
        # и после смерти игрока здоровье противника сохраняется. Нужно обновлять противника.

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False


class Play:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.min = 1
        self.max = 1
        self.hit = 1
        self.chance = 1
        self.fate = 1
        self.wins = 0


    # def choose_your_destiny(self):  # ЗАПИЛИТЬ!
        # выбираешь перса

    # def random_enemy(self):       # ЗАПИЛИТЬ!
        # подсовывает противника из разных экземпляров Warrior

    # def fight_or_run(self):       # ЗАПИЛИТЬ!
    # будет предлагать выбор избежать схватки, если враг слишком сильный
    # или свалить из боя, если процент здоровья ниже какого-то предела
        ''' What are you going to do: fight (f) or run away (r)?") 
                      while True:
            try:
                your_choice = input()
                if your_choice == 'f':
                    return Play.combat(self)
                elif your_choice == 'r':
                    return print("You ran away from the enemy. \n\
You are still alive, but you haven't gained any glory.")
                else:
                    print("Make your decision: \u2694 (f) or \U0001F3C3 (r)?")
            finally:
                pass     
        '''


    def start(self):
        print(f"You have faced an enemy: {player2.name} ({player2.hp} HP) \n\
What are you going to do: fight (f) or run away (r)?")
        while True:
            try:
                your_choice = input()
                if your_choice == 'f':
                    return Play.combat(self)
                elif your_choice == 'r':
                    return print("You ran away from the enemy. \n\
You are still alive, but you haven't gained any glory.")
                # в случае бегства нужно возвращаться к встрече с новым противником
                else:
                    print("Make your decision: \u2694 (f) or \U0001F3C3 (r)?")
            finally:
                pass
                # print()
                # Play.start(self)

    def combat(self):
        p1 = player1.is_alive()     # почему нужно обозначать переменные, а нельзя просто использовать их значения?
        p2 = player2.is_alive()
        while p1 and p2:
            print("p1 бьёт p2")
            player1.make_damage()
            print('{} min, {} max, {} hit'.format(player1.min, player1.max, player1.hit))
            print("p2 пытается увернуться")
            p2d = player2.dodge()
            print('{} chance, {} fate, dodge = {}'.format(player2.chance, player2.fate, player2.dodge()))
            if p2d:
                print(f"The {player2.name} dodged a punch. The {player1.name} missed.")
                print()
                pass
            else:
                player2.take_damage(player1)
                print(f"The {player2.name} got hit for {player1.hit} HP.")
                print(f"{player2.name}: {player2.hp} HP")  # player2.is_alive
                p2 = player2.is_alive()
                print("Живой?", player2.is_alive())
                print()

            print("p2 бьёт p1")
            player2.make_damage()
            print('{} min, {} max, {} hit'.format(player2.min, player2.max, player2.hit))
            print("p1 пытается увернуться")
            p1d = player1.dodge()
            print('{} chance, {} fate, dodge = {}'.format(player1.chance, player1.fate, player1.dodge()))
            if p1d:
                print(f"The {player1.name} dodged a punch. The {player2.name} missed.")
                print()
                pass
            else:
                player1.take_damage(player2)
                print(f"The {player1.name} got hit for {player2.hit} HP.")
                print(f"{player1.name}: {player1.hp} HP")  # player1.is_alive
                p1 = player1.is_alive()
                print("Живой?", player1.is_alive())
                print()
        else:
            if not player2.is_alive:
                self.wins += 1
                print(f"\U0001F339 Congratulations, brave {player1.name}! You've overwhelmed the {player2.name} \U0001F339")
                print()
                Play.start(self)
            else:
                print("\U0001F480 You've been killed. \n\
   Game over.")
                print(f"   You achieved '{self.wins}' victories. \U0001F480")


if __name__ == '__main__':
    player1 = Warrior('Knight')
    player2 = Warrior('Ogre', 200, 80, 10, 40)

    game = Play(player1, player2)
    game.start()



"""
# Первая версия
while knight.hp > 0:
    if ogre.hp <= 0:
        print()
        print("\U0001F339 Congratulations, brave knight! You've overwhelmed the ogre \U0001F48B")
        break
    else:   # Удары наносятся одновременно. Если все умерли, ты проиграл. Если ты не умер - выиграл.
        knight.attack(ogre)
        print(f'\U0001F479 The Ogre was hit for {knight.hit} HP.')
        print(f'\u2764 Ogre: {ogre.hp} HP remains.')

        ogre.attack(knight)
        print(f'\u2694 The Knight was hit for {ogre.hit} HP.')
        print(f'\u2764 Knight: {knight.hp} HP remains.')
else:
    print()
    print("\U0001F480 You've been killed. Game over. \U0001F480")



    def attack(self, other):
        self.hit = random.randint(0, 30)  # воин наносит случайный ущерб в диапазоне
        other.hp -= self.hit        # от здоровья "другого" отнимается величина ущерба
        if other.hp < 0:
            other.hp = 0    # это чтобы не показывало отрицательное здоровье
        return other.hp
"""





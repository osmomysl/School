import random


class Voen:

    def __init__(self):  # вот без этого __init__ ничего не работает. НЕ ПОНЯТНО, что сюда надо писать
        self.hit = 0
        self.hp = 100   # у юнита 100 здоровья

    def attack(self, other):
        self.hit = random.randint(0, 30)  # воин наносит случайный ущерб в диапазоне
        other.hp -= self.hit        # от здоровья "другого" отнимается величина ущерба
        if other.hp < 0:
            other.hp = 0    # это чтобы не показывало отрицательное здоровье
        return other.hp


if __name__ == '__main__':      # тоже не сильно понятно назначение этой строки
    knight = Voen()     # оба соперника относятся к одному классу и равны по силе
    ogre = Voen()

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








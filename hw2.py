import random
x=random.randint(1,20)
i=1
while i<=5:
    number=int(input('Угадай число-'))
    if number==x:
        print('Класс! Вы угадали')
        break
    elif number>x:
        print('Слишком много')
    else:
        print('Слишком мало')
    i+=1
if i>5:
    print("“Все, вы не выиграли. Игра завершилась”.")

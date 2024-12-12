import time
import random

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

player_name = (input('Введит свое имя '))
horseshoes = 4

print(f'{Color.RED}Волшебное дерево: Желаете разбогатеть, странник?{Color.RESET}' )

time.sleep(1)

print(f'{Color.RED}Волшебное дерево: Только сегодня и только здесь, самый большой приз!\nДва полцарства! Рискни и почувствуй удачу на вкус!  {Color.RESET} ')

time.sleep(2)


print(f'{Color.RED}Волшебное дерево: Нуу ? Хочешь сыграть ? {Color.RESET}')

time.sleep(2)

print(f'{player_name.title()}: \n1 - кивнуть \n2 - не кивать и пройти дальше ')

player_choise = int(input()) 
time.sleep(1)
def kill_player():
    print(f'{Color.RED}Волшебное дерево: Eй парни снимите с него шкуру {Color.RESET}')
def game():
    player_points = 0
    print(f'{Color.RED}Волшебное дерево: на что играть будем ?  {Color.RESET}')
    time.sleep(2)
    print(f'{player_name}: на подковы ')
    time.sleep(1)
    print(f'{Color.RED}Волшебное дерево: на подковы так на подковы  {Color.RESET}')
    time.sleep(1)
    print(f'{Color.RED}Волшебное дерево: положи подковы сюда  {Color.RESET}')
    time.sleep(1)
    horseshoess = horseshoes - 1
    print(f'{Color.RED}Волшебное дерево: и угадай число от 1 до 10 \nвсе очень просто я загадываю ты отгадываешь  ){Color.RESET}')
    time.sleep(1)
    print(f'{Color.RED}Волшебное дерево: иии так ваше числооо  {Color.RESET}')
    player_rd1 = int(input())
    print(f'{player_name} эээээээ {player_rd1} ')
    print(f'{Color.RED}Волшебное дерево: ПРАВИЛЬНО ВАШ ВЫИГРАШ СОСТАВИЛ 10 ОЧКОВ\nПопробуете еще раз ? {Color.RESET}')
    time.sleep(1)
    answer = input('Да или нет ')
    if answer == 'да' or answer == 'Да' or answer == 'ДА' or answer == 'da':
        print(f'{player_name}: Конечно же !! Это же так просто   ')
        time.sleep(1)
        print(f'{Color.RED}Волшебное дерево: и таак делайте ваши ставки  {Color.RESET}')
        horseshoess = horseshoes - 1
    else:
        kill_player()
    print(f'{Color.RED}Волшебное дерево: хмммм опять подкова ? \nчтожж приянто ) {Color.RESET}')
    time.sleep(1)
    print(f'{Color.RED}Волшебное дерево: ваше числооо  {Color.RESET}')
    player_rd2 = int(input())
    time.sleep(1)

    print(f'{player_name}:  {player_rd2} ')
    horseshoess = horseshoes - 1
    print(f'{Color.RED}Волшебное дерево: ОПЯТЬ ПРАВИЛЬНО ЕЩЕ 10 ОЧКОВ ДА ВЫ ВЕЗУНЬЧИК КАКОЙ ТО  {Color.RESET} ')
    time.sleep(1)

    print(f'{player_name}: АХАХАХАХА ВЕЗУНЧИК ДА УЧДАЧА МОЕ ВТОРОЕ ИМЯ ДАВАЙ ЕЩЕ   ')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: и так делайте вашу ставку   {Color.RESET}')
    time.sleep(1)

    print(f'{player_name}: ИГРАЕМ НА ВСЕ   ')
    time.sleep(1)

    horseshoess = horseshoes - 2
    print(f'{Color.RED}Волшебное дерево: ииии числооооооо  {Color.RESET}')
    time.sleep(1)

    player_rd3 = int(input())
    print(f'{player_name} : {player_rd3} ')
    time.sleep(2)

    print(f'{Color.RED}Волшебное дерево: мне нравится этот парень он опять выиграл мухахахахах {Color.RESET}')
    time.sleep(1)

    print(f'{player_name} : Ребята.., сегодня не ваш день! ')
    time.sleep(1)

    print(f'{player_name} : ытья ытья 40 очков 40 очков ')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: АХААА кажется наступило время сыграть в супер игру и выиграть ДВА ПОЛ ЦАРСТВА  {Color.RESET}')
    time.sleep(1)

    print(f'{player_name} : ДАДА ПРИШЛО ВРЕМЯ ДАВАЙ ДАВАЙ   {Color.RESET}')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: И ТАК  ствака 100 очков  {Color.RESET}')
    time.sleep(1)

    print(f'{player_name} : ( но у меня всего 40 очков  ')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: хммммммммммммммммммммммммммм  дайте ка подумать   {Color.RESET}')
    time.sleep(1)
    print(f'{Color.RED}Волшебное дерево: * {Color.RESET}')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: ** {Color.RESET}')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: *** {Color.RESET}')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: ХОРОШО 40 очков и твоя шкура  {Color.RESET}')
    time.sleep(1)

    print(f'{player_name}: моя шкура ? ')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: ТВОИ ДВА ПОЛ ЦАРСТВА  {Color.RESET}')
    time.sleep(1)

    print(f'{player_name}: согласен по рукам  \n******не делайте так в реальной жизни*****')
    time.sleep(1)

    print(f'{Color.RED}Волшебное дерево: итак ваше числооооо  {Color.RESET}')
    time.sleep(1)

    print(f'{player_name}: так так так  {player_rd1} было {player_rd2} {player_rd3} было \nзначит по теории вероятности ....')
    time.sleep(2)
    numbers = list(range(1, 11))
    if player_rd1 in numbers:
        numbers.remove(player_rd1)
    if player_rd2 in numbers:
        numbers.remove(player_rd2)
    if player_rd3 in numbers:
        numbers.remove(player_rd3)


    final_number = random.choice(numbers)

    player_rd4 = int(input())
    print(f'{player_name} : {player_rd4} ')
    time.sleep(2)
    

    if final_number == player_rd4 :
        print(f'{Color.RED}Волшебное дерево: Ты выиграл ДВА ПОЛ ЦАРСТВА поздравляем  {Color.RESET}')
    else:
        print(f'{Color.RED}Волшебное дерево: ЖААААЛЛЛЛЬЬЬ но вы проиграли  {Color.RESET}')
        time.sleep(1)
        print(f'{Color.RED}Волшебное дерево: ЕЙ РЕБЯТА СНИМИТИКА С НЕГО ШКУРУ  {Color.RESET}')

        time.sleep(2)
        print(f'{Color.RED}Вы стоите с открытым ртом, как на счет того что бы сбежать ? И позвать Алешу ? {Color.RESET}')



if player_choise == 1:
    game()
if player_choise == 2:
   kill_player()
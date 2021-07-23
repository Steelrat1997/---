import time
import random

def special_print(text):       #Вывод выделенного сообщения 
    stroka_razdelenya = "- - - - - - - - - - - - - - - - - - - - - - - - "
    time.sleep(0.3)
    print(stroka_razdelenya)
    print(text)
    print(stroka_razdelenya)
    
def game_field(list, message):     #Вывод игрового поля
    print("\n"+message)
    for i in range(3):
        print(" ", list[i][0], "|", list[i][1], "|", list[i][2])
        if i!=2:
            print(" -----------")
    print()
    return 0

def win_check(list, simvol):       #Проверка, не выиграл ли игрок с данным символом
    if list[0][0] == list[1][1] == list[2][2] == simvol:
            return 1
    if list[2][0] == list[1][1] == list[0][2] == simvol:
            return 1 

    for i in range(3):
        if list[0][i] == list[1][i] == list[2][i] == simvol:
            return 1
        if list[i][0] == list[i][1] == list[i][2] == simvol:
            return 1
    return 0

def ending_check(list, schetchik, simvol1, simvol2):     #Проверка, какой игрок выиграл, и проверка на ничью
    if win_check(list, simvol1) == 1:
        print()
        special_print("Вы победили!")
        return 1
    if win_check(list, simvol2) == 1:
        print()
        special_print("Победил компьютер =(((")
        return 1
    if schetchik == 9:
        print()
        special_print("Ничья")
        return 1
    return 0

def two_in_row_check(list, simvol1, simvol2):        #Нахождение ряда, в которой можно поставить третий символ и выиграть
    k = 0
    position = 0
    for i in range(3):
        k += int(list[i][i] == simvol1) - int(list[i][i] == simvol2)
        if list[i][i] not in [simvol1, simvol2]:
            position = i*4
    if k == 2:
        return position 
    
    k = 0
    for i in range(3):
        k += int(list[2-i][i] == simvol1) - int(list[2-i][i] == simvol2)
        if list[2-i][i] not in [simvol1, simvol2]:
            position = 3*(2-i)+i
    if k == 2:
        return position

    for i in range(3):
        k = 0
        for j in range(3):
            k += int(list[i][j] == simvol1) - int(list[i][j] == simvol2)
            if list[i][j] not in [simvol1, simvol2]:
                position = i*3+j
        if k == 2:
            return position   
    
    for i in range(3):
        k = 0
        for j in range(3):
            k += int(list[j][i] == simvol1) - int(list[j][i] == simvol2)
            if list[j][i] not in [simvol1,simvol2]:
                position = j*3+i
        if k == 2:
            return position

    return -1   

list = [[1,2,3], [4,5,6], [7,8,9]]
stroka_razdelenya = "- - - - - - - - - - - - - - - - - - - - - - - - "

print()
special_print('Приветствуем вас в игре "крестики-нолики против компьтера!')
print()

difficulty = ""
while difficulty not in ["СР","ПР"]:
    difficulty = input("Выберите сложность(простая или средняя) Пр/Cр \n")
    difficulty = difficulty.upper()
    if difficulty not in ["СР","ПР"]:
        print("\nНекорректный ввод, попробуйте еще раз:")


end_of_game = 0
schetchik = 0
answers = []
print()
game_field(list, "Текущее поле:")
simvol1 = 'X'
simvol2 = 'o'

while end_of_game == 0:            #Ход игрока
    valid = 0
    while not valid:
        print()
        print(stroka_razdelenya)
        answer = input("Введите номер свободного поля, чтобы поставить " + simvol1 + ": ")
        print(stroka_razdelenya)
        try:
            answer = int(answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if answer in list[0] or answer in list[1] or answer in list[2]:
            valid = 1
        else:
            print ("Вы уверены, что ввели номер свободного поля?")
      
    list[(answer-1)//3][(answer-1)%3] = simvol1     #Изменение и отображение игрового поля
    print()
    schetchik += 1
    answers.append(answer)
    game_field(list, "Текушее поле")

    end_of_game = ending_check(list, schetchik, simvol1, simvol2)     #Проверка на окончание игры
        
    if schetchik != 9 and end_of_game != 1:         #Ход компьютера
        special_print("Ход компьютера...")
        time.sleep(1)
        position1 = two_in_row_check(list, simvol2, simvol1)
        position2 = two_in_row_check(list, simvol1, simvol2)
        if position1 != -1 and difficulty != "ПР":
            list[position1//3][position1%3] = simvol2
        elif position2 != -1  and difficulty != "ПР":
            list[position2//3][position2%3] = simvol2
        else:
            i = 0
            j = 0
            while list[i][j] in [simvol1,simvol2]:
                i = random.choice([0,1,2])
                j = random.choice([0,1,2])
            list[i][j] = simvol2
        schetchik += 1
        game_field(list,"Компьютер походил:")

    if end_of_game != 1:                              #Вторая проверка на окончание игры
        end_of_game = ending_check(list, schetchik, simvol1, simvol2)

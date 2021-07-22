import time
import random

def special_print(text):
    stroka_razdelenya = "- - - - - - - - - - - - - - - - - - - - - - - - "
    time.sleep(0.5)
    print(stroka_razdelenya)
    print(text)
    print(stroka_razdelenya)
    
def game_field(list, message):
    print("\n"+message)
    for i in range(3):
        print(" ", list[i][0], "|", list[i][1], "|", list[i][2])
        if i!=2:
            print(" -----------")
    print()
    return 0

def win_check(list, simvol):
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

def two_in_row_check(list, simvol1, simvol2):
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
            position = 3*(2 - i)+i
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
            if list[j][i] not in ['x','o']:
                position = j*3+i
        if k == 2:
            return position

    return -1   

def ending_check(list, schetchik):
    if win_check(list, 'x') == 1:
        print()
        special_print("Вы победили!")
        return 1
    if win_check(list, 'o') == 1:
        print()
        special_print("Победил компьютер =(")
        return 1
    if schetchik == 9:
        print()
        special_print("Ничья")
        return 1
    return 0

list = [[1,2,3], [4,5,6], [7,8,9]]
stroka_razdelenya = "- - - - - - - - - - - - - - - - - - - - - - - - "

print()
special_print('Приветствуем вас в игре "крестики-нолики против компьтера!')
print()

print()
difficulty = ""
while difficulty != "П" and difficulty != "С":
    difficulty = input("Выберите сложность(простая или сложная) П/C \n")
    difficulty = difficulty.upper()
    if difficulty != "П" and difficulty != "С":
        print("\nНекорректный ввод, попробуйте еще раз:")

#if vibor_hoda == "Д" and difficulty == "С":

end_of_game = 0
simvol = ''
schetchik = 0
answers = []
print()
game_field(list, "Текущее поле:")

while end_of_game == 0:
    valid = 0
    simvol = 'x'
    while not valid:
        print()
        print(stroka_razdelenya)
        answer = input("Введите номер свободного поля, чтобы поставить " + simvol + ": ")
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
      
    list[(answer-1)//3][(answer-1)%3] = simvol
    print()
    schetchik += 1
    answers.append(answer)
    game_field(list, "Текушее поле")

    end_of_game = ending_check(list, schetchik)
        
    if schetchik != 9 and end_of_game != 1:
        print(stroka_razdelenya)
        print("Ход компьютера...")
        print(stroka_razdelenya)
        time.sleep(2)
        position1 = two_in_row_check(list, 'o', 'x')
        position2 = two_in_row_check(list, 'x', 'o')
        if position1 != -1:
            list[position1//3][position1%3] = 'o'
        elif position2 != -1:
            list[position2//3][position2%3] = 'o'
        else:
            i = 0
            j = 0
            while list[i][j] in ['x','o']:
                i = random.choice([0,1,2])
                j = random.choice([0,1,2])
            list[i][j] = 'o'
        schetchik += 1
        game_field(list,"Компьютер походил:")

    if end_of_game != 1:
        end_of_game = ending_check(list, schetchik)
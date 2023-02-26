Table={
    'A1':' ','A2':' ','A3':' ',
    'B1':' ','B2':' ','B3':' ',
    'C1':' ','C2':' ','C3':' ',
}

player=1
total_moves=0
end_check=0

def check():
    global player
    if Table['A1']=='X' and Table['A2']=='X' and Table['A3']=='X':
        print('Player one won! ')
        return 1

    if Table['B1']=='X' and Table['B2']=='X' and Table['B3']=='X':
        print('Player one won! ')
        return 1

    if Table['C1'] == 'X' and Table['C2'] == 'X' and Table['C3'] == 'X':
        print('Player One Won!!')
        return 1
    
    if Table['A1'] == 'X' and Table['B2'] == 'X' and Table['C3'] == 'X':
        print('Player One Won!!')
        return 1

    if Table['A1'] == 'X' and Table['B1'] == 'X' and Table['C1'] == 'X':
        print('Player One Won!!')
        return 1
    
    if Table['A2'] == 'X' and Table['B2'] == 'X' and Table['C2'] == 'X':
        print('Player One Won!!')
        return 1
    
    if Table['A3'] == 'X' and Table['B3'] == 'X' and Table['C3'] == 'X':
        print('Player One Won!!')
        return 1
    
    if Table['A1'] == 'O' and Table['A2'] == 'O' and Table['A3'] == 'O':
        print('Player Two Won!!')
        return 1

    if Table['B1'] == 'O' and Table['B2'] == 'O' and Table['B3'] == 'O':
        print('Player Two Won!!')
        return 1

    if Table['C1'] == 'O' and Table['C2'] == 'O' and Table['C3'] == 'O':
        print('Player Two Won!!')
        return 1
    
    if Table['A1'] == 'O' and Table['B2'] == 'O' and Table['C3'] == 'O':
        print('Player Two Won!!')
        return 1
    
    if Table['A1'] == 'O' and Table['B1'] == 'O' and Table['C1'] == 'O':
        print('Player Two Won!!')
        return 1

    if Table['A2'] == 'O' and Table['B2'] == 'O' and Table['C2'] == 'O':
        print('Player Two Won!!')
        return 1
    
    if Table['A3'] == 'O' and Table['B3'] == 'O' and Table['C3'] == 'O':
        print('Player Two Won!!')
        return 1
    return 0

print('A1|A2|A3')
print('- +- +-')
print('B1|B2|B3')
print('- +- +-')
print('C1|C2|C3')
print('*'*20)

while True:
    print(Table['A1']+'|'+Table['A2']+'|'+Table['A3'])
    print('- +- +-')
    print(Table['B1']+'|'+Table['B2']+'|'+Table['B3'])
    print('- +- +-')
    print(Table['C1']+'|'+Table['C2']+'|'+Table['C3'])
    end_check=check()
    if total_moves==9:
        break
    while True:
        if player==1:
            p1_input=input('Player1: ')
            if p1_input.upper() in Table and Table[p1_input.upper()]==' ':
                Table[p1_input.upper()]='X'
                player=2
                break
            else:
                print('Invalid input,please try again')
        else:
            p2_input=input('player two: ') 
            if p2_input.upper() in Table and Table[p2_input.upper()]==" ":
                Table[p2_input.upper()]='O'
                player = 1
                break
            else:
                print('Invalid input, please try again')
                continue
    total_moves += 1
    print('*'*20)
    print()
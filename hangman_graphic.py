def lives_9():
    # 9 lives left
    print("             ")
    print("             ")
    print("             ")
    print("             ")
    print("             ")
    print("             ")
    print("             ")
    print('"""""')

def lives_8():
    # 8 lives left
    print("             ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  | ")
    print('"""""')

def lives_7():
    # 7 lives left
    print("  _ _ _ _ _  ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  | ")
    print('"""""')

def lives_6():
    # 6 lives left
    print("  _ _ _ _ _  ")
    print("  |        | ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  | ")
    print('"""""')

def lives_5():
    # 5 lives left
    print("  _ _ _ _ _  ")
    print("  |        | ")
    print("  |        O ")
    print("  |          ")
    print("  |          ")
    print("  |          ")
    print("  | ")
    print('"""""')

def lives_4():
    # 4 lives left
    print("  _ _ _ _ _   ")
    print("  |        |  ")
    print("  |        O  ")
    print("  |        |  ")
    print("  |        |  ")
    print("  |           ")
    print("  | ")
    print('"""""')

def lives_3():
    # 3 lives left
    print("  _ _ _ _ _   ")
    print("  |        |  ")
    print("  |        O  ")
    print("  |       \|  ")
    print("  |        |  ")
    print("  |           ")
    print("  | ")
    print('"""""')

def lives_2():
    # 2 lives left
    print("  _ _ _ _ _   ")
    print("  |        |  ")
    print("  |        O  ")
    print("  |       \|/ ")
    print("  |        |  ")
    print("  |           ")
    print("  | ")
    print('"""""')

def lives_1():
    # 1 lives left
    print("  _ _ _ _ _   ")
    print("  |        |  ")
    print("  |        O  ")
    print("  |       \|/ ")
    print("  |        |  ")
    print("  |       /   ")
    print("  | ")
    print('"""""')

def lives_0():
    # 0 lives left
    print("  _ _ _ _ _   ")
    print("  |        |  ")
    print("  |        O  ")
    print("  |       \|/ ")
    print("  |        |  ")
    print("  |       / \ ")
    print("  | ")
    print('"""""')

def lives_num(num):
    if num == 9:
        return lives_9()
    elif num == 8:
        return lives_8()
    elif num == 7:
        return lives_7()
    elif num == 6:
        return lives_6()
    elif num == 5:
        return lives_5()
    elif num == 4:
        return lives_4()
    elif num == 3:
        return lives_3()
    elif num == 2:
        return lives_2()
    elif num == 1:
        return lives_1()
    elif num == 0:
        return lives_0()


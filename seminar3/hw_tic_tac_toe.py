class Tic_tac_toe:
    arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __init__(self):
        pass

    def make_a_move(self):
        move_row = int(input("В какой строке (сверху вниз) ставим крестик? "))
        move_column = int(input("В каком столбце (слева направо) ставим крестик? "))
        if move_column > 3 or move_row > 3 or move_column < 1 or move_row < 1:
            raise Exception("Введите корректный номер строки и столбца (1-3).")
        else:
            if self.arr[move_row - 1][move_column - 1] == " ":
                self.arr[move_row - 1][move_column - 1] = "X"
                print(self.arr[0])
                print(self.arr[1])
                print(self.arr[2])
            else:
                print("Это поле занято, сделайте новый ход.")
                self.make_a_move()

    def my_turn_to_make_a_move(self):
        move_is_found = False

        for i in range(3):
            for j in range(3):
                if self.arr[i][j] == " ":
                    self.arr[i][j] = "O"
                    print(self.arr[0])
                    print(self.arr[1])
                    print(self.arr[2])
                    move_is_found = True
                    if move_is_found:
                        break
            if move_is_found:
                break

    def to_play_a_game(self):
        self.make_a_move()
        print('')
        self.my_turn_to_make_a_move()
        print('')
        game_in_process = True
        turn_of_player = True
        while game_in_process:
            if (self.arr[0][0] == self.arr[0][1]) & (self.arr[0][1] == self.arr[0][2]) & (self.arr[0][0] != " ") or \
                    (self.arr[1][0] == self.arr[1][1]) & (self.arr[1][1] == self.arr[1][2]) & (self.arr[1][0] != " ") or \
                    (self.arr[2][0] == self.arr[2][1]) & (self.arr[2][1] == self.arr[2][2]) & (self.arr[2][0] != " ") or \
                    (self.arr[0][1] == self.arr[0][2]) & (self.arr[0][0] == self.arr[0][2]) & (self.arr[0][0] != " ") or \
                    (self.arr[1][0] == self.arr[1][1]) & (self.arr[1][1] == self.arr[1][2]) & (self.arr[1][0] != " ") or \
                    (self.arr[2][0] == self.arr[2][1]) & (self.arr[2][1] == self.arr[2][2]) & (self.arr[2][0] != " ") or \
                    (self.arr[0][0] == self.arr[1][1]) & (self.arr[1][1] == self.arr[2][2]) & (self.arr[0][0] != " ") or \
                    (self.arr[0][2] == self.arr[1][1]) & (self.arr[2][0] == self.arr[1][1]) & (self.arr[1][1] != " ") or \
                    ((" " not in self.arr[0]) & (" " not in self.arr[1]) & (" " not in self.arr[2])):
                print("Игра окончена")
                game_in_process = False

            else:
                if turn_of_player:
                    self.make_a_move()
                    print('')
                    turn_of_player = False
                else:
                    self.my_turn_to_make_a_move()
                    print('')
                    turn_of_player = True


game1 = Tic_tac_toe()

game1.to_play_a_game()

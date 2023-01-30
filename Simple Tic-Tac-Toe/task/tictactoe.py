from collections import Counter
from itertools import chain

def print_grid(grid):
    print("---------")
    for row in grid:
        print("|", row[0], row[1], row[2], "|")
    print("---------")


# def input_grid():
#     input_line = input()
#     if ("X" and "O" or "_") not in input_line:
#         print("Wrong input")
#     grid = []
#     n = 0
#     for i in range(3):
#         temporary_list = []
#         for j in range(3):
#             temporary_list.append(input_line[n])
#             n += 1
#         grid.append(temporary_list)
#     return grid


def who_win():
    global grid
    win = []
    grid_transpose = list(map(list, zip(*grid)))
    for player in ["X", "O"]:
        for matrix in [grid, grid_transpose]:
            for row in matrix:
                if row[0] == row[1] == row[2] == player:
                    win.append(player)
        if (grid[0][0] == grid[1][1] == grid[2][2] == player or
                grid[-1][0] == grid[-2][1] == grid[-3][2] == player):
            win.append(player)
    if len(win) > 1:
        return "Impossible"
    elif len(win) == 0:
        return None
    else:
        return win[0]


def is_it_finished():
    global grid
    full_row = 0
    for row in grid:
        if "_" in row:
            return False
        else:
            full_row += 1
    if full_row == 3:
        return True

def is_it_posible():
    global grid
    count = Counter(chain.from_iterable(grid))
    if abs(count["X"] - count["O"]) > 1:
        return False


def check_state_of_game():
    winner = who_win()
    if is_it_posible() == False:
        print("Impossible")
    else:
        if winner == "Impossible":
            print("Impossible")
        else:
            if winner == None:
                if is_it_finished() == False:
                    return "ongoing"
                else:
                    print("Draw")
            else:
                print(winner, "wins")


def empty_grid():
    grid =  [[[] for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            grid[i][j] = "_"
    return grid


def user_move(player):
    global grid
    try:
        coordinate = input()
        coordinate = coordinate.split(" ")
        coordinate[0] = eval(coordinate[0]) - 1
        coordinate[1] = eval(coordinate[1]) - 1
        if grid[coordinate[0]][coordinate[1]] != "_":
            print("This cell is occupied! Choose another one!")
            user_move(player)
        else:
            grid[coordinate[0]][coordinate[1]] = player

    except IndexError:
        print("Coordinates should be from 1 to 3!")
        return user_move(player)
    except ValueError:
        print("You should enter numbers!")
        return user_move(player)



def game():
    global grid
    print_grid(grid)
    i = 0
    while check_state_of_game() == "ongoing":
        player = i % 2
        players = ["X", "O"]
        user_move(players[player])
        print_grid(grid)
        i += 1


grid = empty_grid()
game()

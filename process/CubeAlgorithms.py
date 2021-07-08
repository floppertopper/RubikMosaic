#Cube Algorithms
#Vic Tong
#June 4th 2021

#colours as numbers (temporary)
white = 1
yellow = 6
red = 2
orange = 5
green = 3
blue = 4


list_of_cubefaces = [
  [[red, red, red],
  [red, red, red],
  [red, red, red]],

  [[red, orange, red],
  [red, red, red],
  [green, red, yellow]],
]

centerpiece = list_of_cubefaces[0][1][1]

input = []
output = []
counter = 0

#converting everything from the face into an array
for i in list_of_cubefaces[0]:
    for j in i:
        if counter != 4:
            input.append(j)
        counter+=1

counter = 0
for i in list_of_cubefaces[1]:
    for j in i:
        if counter != 4:
            output.append(j)
        counter+=1

#returns the index of the different values in the lists in their respective order
def difference_in_lists (output): #input and output have to be the same length
    differences = [["", "", "", ""], ["", "", "", ""]]
    for i in range(0, len(output)):
        if input[i] != output[i]:
            if is_edge_piece(i):
                differences[0][edge_index(i, True)] = output[i]
            else:
                differences[1][edge_index(i, False)] = output[i]

    return differences


def is_edge_piece(index):
    edge = [1,3,4,6]
    return index in edge

def edge_index(index, is_edge):
    edge = [1,3,4,6]
    corner = [0,2,5,7]
    if is_edge:
        return edge.index(index)

    return corner.index(index)


def kill_char(string, n): # n = position of which character you want to remove
    begin = string[:n]    # from beginning to n (n not included)
    end = string[n+1:]    # n+1 through end of string
    return begin + end

def move_reverse(moveset):
    reversed = []
    moveset.reverse()
    for move in moveset:
        if move[-1] == "'":
            reversed.append(kill_char(move, len(move)-1))
        elif move[-1] == "2":
            reversed.append(move)
        else:
            reversed.append(move+"'")

    return reversed

def instructions(output):
    T_perm = ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"]
    cube_labels = {
        white : ["A", "B", "C", "D"],
        green : ["E", "F", "G", "H"],
        red : ["I", "J", "K", "L"],
        blue : ["M", "N", "O", "P"],
        orange : ["Q", "R", "S", "T"],
        yellow : ["U", "V", "W", "X"]
    }

    difference_list = difference_in_lists(output)

    for i in difference_list[0]:
        if i != '':
            label = cube_labels[i][0] #current cube label
            offset_label = offset(centerpiece, label) #returns the offsetted label if the centerpiece isn't red
            setup = edge_setup_move(offset_label) #returns the setup move to swap pieces


            print(setup)
            print(T_perm)
            print(move_reverse(setup)) #setup move is now reversed

            label = cube_labels[difference_list[0].index(i)]
            cube_labels[centerpiece].pop(0)#deletes the current label from the dictionary so it doesn't get reused



    for i in difference_list[1]:#corners tbd
        pass
        #print("corner piece")


def edge_setup_move(piece):
    if piece == "A":
        return ["Lw2", "D", "L2"]
    elif piece == "C": #D and B doesn't need setup moves
        return ["Lw2", "D'", "L2"]
    elif piece == "E":
        return ["L'", "Dw", "L'"]
    elif piece == "F":
        return ["Dw'", "L"]
    elif piece == "G":
        return ["L", "Dw", "L'"]
    elif piece == "H":
        return ["Dw", "L'"]
    elif piece == "I":
        return ["Lw", "D'", "L2"]
    elif piece == "J":
        return ["Dw2", "L"]
    elif piece == "K":
        return ["Lw", "D'", "L2"]
    elif piece == "L":
        return ["L'"]
    elif piece == "M":
        return ["J perm"]
    elif piece == "N":
        return ["Dw", "L"]
    elif piece == "O":
        return ["D2", "L'", "Dw'", "L"]
    elif piece == "P":
        return ["Dw'", "L'"]
    elif piece == "Q":
        return ["Lw'", "D", "L2"]
    elif piece == "R":
        return ["L"]
    elif piece == "S":
        return ["Lw'", "D'", "L2"]
    elif piece == "T":
        return ["Lw2", "L'"]

def offset(centerpiece, label):
    if centerpiece == white:
        return chr(ord(label)-8)
    elif centerpiece == red:
        return label
    elif centerpiece == blue:
        return (chr(ord(label) + 4))
    elif centerpiece == green:
        return (chr(ord(label) - 4))
    elif centerpiece == orange:
        return (chr(ord(label) + 8))
    elif centerpiece == yellow:
        return (chr(ord(label) + 12))

instructions(output)

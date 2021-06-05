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

  [[red, blue, red],
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

#returns the different values of the lists in their respective order
def difference_in_lists (input, output): #input and output have to be the same length
    differences = []
    for i in range(0, len(input)):
        if input[i] != output[i]:
            differences.append(i)

    return differences


def piece(index):
    edge = [1,3,4,6]
    return index in edge

def instructions ():
    for i in difference_in_lists(input, output):
        edge_piece = piece(i)
        print(edge_piece)

instructions()

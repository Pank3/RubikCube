from tkinter import *
import Cube as c

board = Tk()
board.geometry('800x600')
board.resizable(0, 0)

display = Label(board,borderwidth = 2,relief="sunken",bg = 'black',fg = 'white',font = ("ALGERIAN",10))
display.place(x =50,y = 520,height = 50,width =  700)


selectionVariavle = None

colorToPos = {
    'white':"U",
    'blue':"F",
    'red':"L",
    'orange':"R",
    "green":"B",
    "yellow":"D",

}

frontVal = c.Front()
backVal  = c.Back()
leftVal = c.Left()
rightVal = c.Right()
topVal = c.Up()
downVal = c.Down()


topSet = [[Button()] * 3 for i in range(3)]
leftSet = [[Button()] * 3 for i in range(3)]
frontSet = [[Button()] * 3 for i in range(3)]
rightSet = [[Button()] * 3 for i in range(3)]
backSet = [[Button()] * 3 for i in range(3)]
downSet = [[Button()] * 3 for i in range(3)]


def cubeGuard():
    guard = Label(board, bg="gray", borderwidth=3, relief='raised')
    guard.place(x=16, y=46, height=454, width=604)


def ColorChanging(i,j,cubeSet):
    global selectionVariavle
    #print(selectionVariavle,i,j)
    if selectionVariavle and not (i==1 and j==1):
        if cubeSet == topSet:
            topVal[i][j] = colorToPos[selectionVariavle]
        elif cubeSet == leftSet:
            leftVal[i][j] = colorToPos[selectionVariavle]
        elif cubeSet ==frontSet:
            frontVal[i][j] = colorToPos[selectionVariavle]
        elif cubeSet == rightSet:
            rightVal[i][j] = colorToPos[selectionVariavle]
        elif cubeSet == backSet:
            backVal[i][j] = colorToPos[selectionVariavle]
        elif cubeSet == downSet:
            downVal[i][j] = colorToPos[selectionVariavle]
        cubeSet[i][j].configure(bg = selectionVariavle)

def topCubes(x, y, color):
    topSet[0][0] = Button(board, bg=color, command=lambda: ColorChanging(0,0, topSet))
    topSet[0][0].place(x=x, y=y, height=48, width=48)
    topSet[0][1] = Button(board, bg=color, command=lambda: ColorChanging(0,1, topSet))
    topSet[0][1].place(x=x+50, y=y, height=48, width=48)
    topSet[0][2] = Button(board, bg=color, command=lambda: ColorChanging(0,2, topSet))
    topSet[0][2].place(x=x+100, y=y, height=48, width=48)
    topSet[1][0] = Button(board, bg=color, command=lambda: ColorChanging(1,0, topSet))
    topSet[1][0].place(x=x, y=y+50, height=48, width=48)
    topSet[1][1] = Button(board, bg=color, command=lambda: ColorChanging(1,1, topSet))
    topSet[1][1].place(x=x+50, y=y+50, height=48, width=48)
    topSet[1][2] = Button(board, bg=color, command=lambda: ColorChanging(1,2, topSet))
    topSet[1][2].place(x=x+100, y=y+50, height=48, width=48)
    topSet[2][0] = Button(board, bg=color, command=lambda: ColorChanging(2,0, topSet))
    topSet[2][0].place(x=x, y=y+100, height=48, width=48)
    topSet[2][1] = Button(board, bg=color, command=lambda: ColorChanging(2,1, topSet))
    topSet[2][1].place(x=x+50, y=y+100, height=48, width=48)
    topSet[2][2] = Button(board, bg=color, command=lambda: ColorChanging(2,2, topSet))
    topSet[2][2].place(x=x+100, y=y+100, height=48, width=48)

def leftCubes(x, y, color):
    leftSet[0][0] = Button(board, bg=color, command=lambda: ColorChanging(0,0, leftSet))
    leftSet[0][0].place(x=x, y=y, height=48, width=48)
    leftSet[0][1] = Button(board, bg=color, command=lambda: ColorChanging(0,1, leftSet))
    leftSet[0][1].place(x=x+50, y=y, height=48, width=48)
    leftSet[0][2] = Button(board, bg=color, command=lambda: ColorChanging(0,2, leftSet))
    leftSet[0][2].place(x=x+100, y=y, height=48, width=48)
    leftSet[1][0] = Button(board, bg=color, command=lambda: ColorChanging(1,0, leftSet))
    leftSet[1][0].place(x=x, y=y+50, height=48, width=48)
    leftSet[1][1] = Button(board, bg=color, command=lambda: ColorChanging(1,1, leftSet))
    leftSet[1][1].place(x=x+50, y=y+50, height=48, width=48)
    leftSet[1][2] = Button(board, bg=color, command=lambda: ColorChanging(1,2, leftSet))
    leftSet[1][2].place(x=x+100, y=y+50, height=48, width=48)
    leftSet[2][0] = Button(board, bg=color, command=lambda: ColorChanging(2,0, leftSet))
    leftSet[2][0].place(x=x, y=y+100, height=48, width=48)
    leftSet[2][1] = Button(board, bg=color, command=lambda: ColorChanging(2,1, leftSet))
    leftSet[2][1].place(x=x+50, y=y+100, height=48, width=48)
    leftSet[2][2] = Button(board, bg=color, command=lambda: ColorChanging(2,2, leftSet))
    leftSet[2][2].place(x=x+100, y=y+100, height=48, width=48)

def frontCubes(x, y, color):
    frontSet[0][0] = Button(board, bg=color, command=lambda: ColorChanging(0, 0, frontSet))
    frontSet[0][0].place(x=x, y=y, height=48, width=48)
    frontSet[0][1] = Button(board, bg=color, command=lambda: ColorChanging(0, 1, frontSet))
    frontSet[0][1].place(x=x + 50, y=y, height=48, width=48)
    frontSet[0][2] = Button(board, bg=color, command=lambda: ColorChanging(0, 2, frontSet))
    frontSet[0][2].place(x=x + 100, y=y, height=48, width=48)
    frontSet[1][0] = Button(board, bg=color, command=lambda: ColorChanging(1, 0, frontSet))
    frontSet[1][0].place(x=x, y=y + 50, height=48, width=48)
    frontSet[1][1] = Button(board, bg=color, command=lambda: ColorChanging(1, 1, frontSet))
    frontSet[1][1].place(x=x + 50, y=y + 50, height=48, width=48)
    frontSet[1][2] = Button(board, bg=color, command=lambda: ColorChanging(1, 2, frontSet))
    frontSet[1][2].place(x=x + 100, y=y + 50, height=48, width=48)
    frontSet[2][0] = Button(board, bg=color, command=lambda: ColorChanging(2, 0, frontSet))
    frontSet[2][0].place(x=x, y=y + 100, height=48, width=48)
    frontSet[2][1] = Button(board, bg=color, command=lambda: ColorChanging(2, 1, frontSet))
    frontSet[2][1].place(x=x + 50, y=y + 100, height=48, width=48)
    frontSet[2][2] = Button(board, bg=color, command=lambda: ColorChanging(2, 2, frontSet))
    frontSet[2][2].place(x=x + 100, y=y + 100, height=48, width=48)

def rightCubes(x, y, color):
    rightSet[0][0] = Button(board, bg=color, command=lambda: ColorChanging(0, 0, rightSet))
    rightSet[0][0].place(x=x, y=y, height=48, width=48)
    rightSet[0][1] = Button(board, bg=color, command=lambda: ColorChanging(0, 1, rightSet))
    rightSet[0][1].place(x=x + 50, y=y, height=48, width=48)
    rightSet[0][2] = Button(board, bg=color, command=lambda: ColorChanging(0, 2, rightSet))
    rightSet[0][2].place(x=x + 100, y=y, height=48, width=48)
    rightSet[1][0] = Button(board, bg=color, command=lambda: ColorChanging(1, 0, rightSet))
    rightSet[1][0].place(x=x, y=y + 50, height=48, width=48)
    rightSet[1][1] = Button(board, bg=color, command=lambda: ColorChanging(1, 1, rightSet))
    rightSet[1][1].place(x=x + 50, y=y + 50, height=48, width=48)
    rightSet[1][2] = Button(board, bg=color, command=lambda: ColorChanging(1, 2, rightSet))
    rightSet[1][2].place(x=x + 100, y=y + 50, height=48, width=48)
    rightSet[2][0] = Button(board, bg=color, command=lambda: ColorChanging(2, 0, rightSet))
    rightSet[2][0].place(x=x, y=y + 100, height=48, width=48)
    rightSet[2][1] = Button(board, bg=color, command=lambda: ColorChanging(2, 1, rightSet))
    rightSet[2][1].place(x=x + 50, y=y + 100, height=48, width=48)
    rightSet[2][2] = Button(board, bg=color, command=lambda: ColorChanging(2, 2, rightSet))
    rightSet[2][2].place(x=x + 100, y=y + 100, height=48, width=48)

def backCubes(x, y, color):
    backSet[0][0] = Button(board, bg=color, command=lambda: ColorChanging(0, 0, backSet))
    backSet[0][0].place(x=x, y=y, height=48, width=48)
    backSet[0][1] = Button(board, bg=color, command=lambda: ColorChanging(0, 1, backSet))
    backSet[0][1].place(x=x + 50, y=y, height=48, width=48)
    backSet[0][2] = Button(board, bg=color, command=lambda: ColorChanging(0, 2, backSet))
    backSet[0][2].place(x=x + 100, y=y, height=48, width=48)
    backSet[1][0] = Button(board, bg=color, command=lambda: ColorChanging(1, 0, backSet))
    backSet[1][0].place(x=x, y=y + 50, height=48, width=48)
    backSet[1][1] = Button(board, bg=color, command=lambda: ColorChanging(1, 1, backSet))
    backSet[1][1].place(x=x + 50, y=y + 50, height=48, width=48)
    backSet[1][2] = Button(board, bg=color, command=lambda: ColorChanging(1, 2, backSet))
    backSet[1][2].place(x=x + 100, y=y + 50, height=48, width=48)
    backSet[2][0] = Button(board, bg=color, command=lambda: ColorChanging(2, 0, backSet))
    backSet[2][0].place(x=x, y=y + 100, height=48, width=48)
    backSet[2][1] = Button(board, bg=color, command=lambda: ColorChanging(2, 1, backSet))
    backSet[2][1].place(x=x + 50, y=y + 100, height=48, width=48)
    backSet[2][2] = Button(board, bg=color, command=lambda: ColorChanging(2, 2, backSet))
    backSet[2][2].place(x=x + 100, y=y + 100, height=48, width=48)

def downCubes(x, y, color):
    downSet[0][0] = Button(board, bg=color, command=lambda: ColorChanging(0, 0, downSet))
    downSet[0][0].place(x=x, y=y, height=48, width=48)
    downSet[0][1] = Button(board, bg=color, command=lambda: ColorChanging(0, 1, downSet))
    downSet[0][1].place(x=x + 50, y=y, height=48, width=48)
    downSet[0][2] = Button(board, bg=color, command=lambda: ColorChanging(0, 2, downSet))
    downSet[0][2].place(x=x + 100, y=y, height=48, width=48)
    downSet[1][0] = Button(board, bg=color, command=lambda: ColorChanging(1, 0, downSet))
    downSet[1][0].place(x=x, y=y + 50, height=48, width=48)
    downSet[1][1] = Button(board, bg=color, command=lambda: ColorChanging(1, 1, downSet))
    downSet[1][1].place(x=x + 50, y=y + 50, height=48, width=48)
    downSet[1][2] = Button(board, bg=color, command=lambda: ColorChanging(1, 2, downSet))
    downSet[1][2].place(x=x + 100, y=y + 50, height=48, width=48)
    downSet[2][0] = Button(board, bg=color, command=lambda: ColorChanging(2, 0, downSet))
    downSet[2][0].place(x=x, y=y + 100, height=48, width=48)
    downSet[2][1] = Button(board, bg=color, command=lambda: ColorChanging(2, 1, downSet))
    downSet[2][1].place(x=x + 50, y=y + 100, height=48, width=48)
    downSet[2][2] = Button(board, bg=color, command=lambda: ColorChanging(2, 2, downSet))
    downSet[2][2].place(x=x + 100, y=y + 100, height=48, width=48)

def ColorSelectionBorder():
    border = Label(board, bg='black', borderwidth=2)
    border.place(x=668, y=99, height=151, width=101)

def selectColor(color):
    global selectionVariavle
    selectionVariavle = color

def ColorSelectionSection():
    x, y = 670, 100

    whiteSelect = Button(board, bg="white", command=lambda: selectColor("white"))
    whiteSelect.place(x=x, y=y, height=48, width=48)

    yellowSelect = Button(board, bg="yellow", command=lambda: selectColor("yellow"))
    yellowSelect.place(x=x + 50, y=y, height=48, width=48)

    blueSelect = Button(board, bg="blue", command=lambda: selectColor("blue"))
    blueSelect.place(x=x, y=y + 50, height=48, width=48)

    greenSelect = Button(board, bg="green", command=lambda: selectColor("green"))
    greenSelect.place(x=x + 50, y=y + 50, height=48, width=48)

    redSelect = Button(board, bg="red", command=lambda: selectColor("red"))
    redSelect.place(x=x, y=y + 100, height=48, width=48)

    orangeSelect = Button(board, bg="orange", command=lambda: selectColor("orange"))
    orangeSelect.place(x=x + 50, y=y + 100, height=48, width=48)

def evaluation():
    evaL = Button(board,text= "EVAL",bg = "cyan",font = ("Arial",20),command = letsGo)
    evaL.place(x = 670,y = 300,height = 40,width = 100)

def getLst(val):
    lst = ""
    for i in range(3):
        for j in range(3):
           lst+=val[i][j]
    return lst

def letsGo():
    final_list = getLst(topVal)+getLst(rightVal)+getLst(frontVal)+\
                 getLst(downVal)+getLst(leftVal)+getLst(backVal)
    solve = c.solving(final_list)
    display.configure(text = solve)



def main():
# Cubes Place
    cubeGuard()
    cubes_x, cubes_y = 20, 200

    leftCubes(cubes_x, cubes_y, "red")
    frontCubes(cubes_x + 150, cubes_y, "blue")
    rightCubes(cubes_x + 300, cubes_y, "orange")
    backCubes(cubes_x + 450, cubes_y, "green")
    topCubes(cubes_x + 150, cubes_y - 150, "white")
    downCubes(cubes_x + 150, cubes_y + 150, "yellow")

    evaluation()

    ColorSelectionBorder()
    ColorSelectionSection()

    board.mainloop()

if __name__=="__main__":
    main()
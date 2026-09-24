import os
import random

dead = " "
alive = "#"


class Cell:
    def __init__(self, alive, x, y) -> None:
        self.alive = alive
        self.x = x
        self.y = y


class Game:
    def __init__(self, width, height, speed) -> None:
        self.width = width
        self.height = height
        self.cellList = []

    def initCells(self):
        for x in range(self.width):
            for y in range(self.height):
                isAlive = random.randint(1, 5) == 5  # 1 / 10 chance am leben zu sein
                newCell = Cell(isAlive, x, y)
                self.cellList.append(newCell)

    def startSimulation(self):
        self.initCells()
        iterationCount = 1
        while True:
            self.drawCells()
            self.updateCells()
            if input("Iteration: " + str(iterationCount) + "    ") == "q":
                break
            iterationCount += 1

    def getNeighborPositions(self, cell):
        currentPos = (cell.x, cell.y)
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        positions = []
        for offset in offsets:
            newPos = (currentPos[0] + offset[0], currentPos[1] + offset[1])
            positions.append(newPos)
        return positions

    def updateCells(self):
        for cell in self.cellList:
            neighborPos = self.getNeighborPositions(cell)  # -> list
            aliveNeighbors = 0
            for pos in neighborPos:
                try:
                    if self.coordAliveDict[pos] == alive:
                        aliveNeighbors += 1
                except:
                    pass
            if cell.alive:
                if aliveNeighbors <= 1:  # under population
                    cell.alive = False
                if aliveNeighbors >= 4:  # over population
                    cell.alive = False

            elif cell.alive == False:  # if the cell is dead
                if aliveNeighbors == 3:
                    cell.alive = True  # if the cell has 3 alive neighbors then it will get populated

    def drawCells(self):
        self.coordAliveDict = {}  # (x,y): " " oder "#"
        for cell in self.cellList:
            if cell.alive:
                symbol = alive
            else:
                symbol = dead

            self.coordAliveDict[(cell.x, cell.y)] = symbol
        os.system("cls")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += self.coordAliveDict[(x, y)]

            print(row)


col = Game(100, 10, 10)
col.startSimulation()

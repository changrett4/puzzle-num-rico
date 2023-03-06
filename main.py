import pygame
import time
import random
from mod import *
from configs import *
import PuzzleState as ps

class Jogo:
    final_state = [[0,1,2],[3,4,5],[6,7,8]]
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.tempoShuffle = 0
        self.startShuffle = False
        self.escolha = ""
        self.start = False
        self.startTime = False
        self.tempo = 0
        self.cont = 0

    def drawTiles(self):
        self.tiles = []
        for i, x in enumerate(self.gridTiles):
            self.tiles.append([])
            for j, tile in enumerate(x):
                if tile != 0:
                    self.tiles[i].append(Tile(self, j, i, str(tile)))
                else:
                    self.tiles[i].append(Tile(self, j, i, "empty"))

    def new(self):
        self.sprt = pygame.sprite.Group()
        
        self.gridTiles = self.final_state
        self.gridTileF = self.final_state
        self.puzzleState = ps.PuzzleState(self.gridTiles)
        self.tempo = 0
        self.startTime = False
        self.start = False
        self.venceu = False
        self.buttons = []
        self.buttons.append(Button(500, 100, 200, 50, "Embaralhar", white, black))
        self.buttons.append(Button(500, 170, 200, 50, "Resolver", white, black))
        self.drawTiles()

    def update(self):
        if self.start:
            if self.gridTiles == self.gridTileF:
                self.start = False

            if self.startTime:
                self.timer = time.time()
                self.startTime = False
            self.tempo = time.time() - self.timer

        if self.startShuffle:
            self.shuffle()
            self.drawTiles()
            self.tempoShuffle += 1
            if self.tempoShuffle > 120:
                self.startShuffle = False
                self.start = True
                self.startTime = True

        self.sprt.update()

    def drawGrid(self):
        for i in range(-1, 3 * tam, tam):
            pygame.draw.line(self.screen, grey, (i, 0), (i, 3 * tam))
        for j in range(-1, 3 * tam, tam):
            pygame.draw.line(self.screen, grey, (0, j), (3 * tam, j))

    def draw(self):
        self.screen.fill(blue)
        self.sprt.draw(self.screen)
        self.drawGrid()
        for button in self.buttons:
            button.drawButton(self.screen)
        pygame.display.flip()

    def shuffle(self):
        movimento = []
        for i, tiles in enumerate(self.tiles):
            for j, tile in enumerate(tiles):
                if tile.text == "empty":
                    if tile.right():
                        movimento.append("RIGHT")
                    if tile.left():
                        movimento.append("LEFT")
                    if tile.up():
                        movimento.append("UP")
                    if tile.down():
                        movimento.append("DOWN")
                    break
            if len(movimento) > 0:
                break

        if self.escolha == "RIGHT":
            movimento.remove("LEFT") if "LEFT" in movimento else movimento
        elif self.escolha == "LEFT":
            movimento.remove("RIGHT") if "RIGHT" in movimento else movimento
        elif self.escolha == "DOWN":
            movimento.remove("UP") if "UP" in movimento else movimento
        elif self.escolha == "UP":
            movimento.remove("DOWN") if "DOWN" in movimento else movimento

        choice = random.choice(movimento)
        self.escolha = choice
        if choice == "RIGHT":
            self.gridTiles[i][j], self.gridTiles[i][j + 1] = self.gridTiles[i][j + 1], self.gridTiles[i][j]
        elif choice == "LEFT":
            self.gridTiles[i][j], self.gridTiles[i][j - 1] = self.gridTiles[i][j - 1], self.gridTiles[i][j]
        elif choice == "DOWN":
            self.gridTiles[i][j], self.gridTiles[i + 1][j] = self.gridTiles[i + 1][j], self.gridTiles[i][j]
        elif choice == "UP":
            self.gridTiles[i][j], self.gridTiles[i - 1][j] = self.gridTiles[i - 1][j], self.gridTiles[i][j]

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                for i, tiles in enumerate(self.tiles):
                    for j, tile in enumerate(tiles):
                        if tile.clickMouse(mouseX, mouseY):
                            if tile.right() and self.gridTiles[i][j + 1] == 0:
                                self.gridTiles[i][j], self.gridTiles[i][j + 1] = self.gridTiles[i][j + 1], self.gridTiles[i][j]

                            if tile.left() and self.gridTiles[i][j - 1] == 0:
                                self.gridTiles[i][j], self.gridTiles[i][j - 1] = self.gridTiles[i][j - 1], self.gridTiles[i][j]

                            if tile.up() and self.gridTiles[i - 1][j] == 0:
                                self.gridTiles[i][j], self.gridTiles[i - 1][j] = self.gridTiles[i - 1][j], self.gridTiles[i][j]

                            if tile.down() and self.gridTiles[i + 1][j] == 0:
                                self.gridTiles[i][j], self.gridTiles[i + 1][j] = self.gridTiles[i + 1][j], self.gridTiles[i][j]

                            self.drawTiles()

                for button in self.buttons:
                    lista = []
                    if button.clickMouse(mouseX, mouseY):
                        if button.text == "Embaralhar":
                            self.tempoShuffle = 0
                            self.startShuffle = True
                        if button.text == "Resolver":
                                                       
                            solution = self.puzzleState.solve_puzzle()

                            if(solution == -1):
                               print("IMPOSSÍVEL RESOLVER A PARTIR DESSE ESTADO")
                            else:
                               for i in range(len(solution)):
                                   self.gridTiles = solution[i].puzzle
                                   self.update()
                                   self.draw()
                                   self.drawTiles()
                                   self.cont += 1
                                   pygame.time.delay(600)
                                   print(f"Movimento: {solution[i].move} ; Cost: {solution[i].heuristic() + i}; Número de passos: {i}")
                            self.venceu = True
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

game = Jogo()
while True:
    game.new()
    game.run()
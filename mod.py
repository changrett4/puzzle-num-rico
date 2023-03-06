import pygame
from configs import *

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.sprt
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tam, tam))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect()
        if self.text != "empty":
            self.font = pygame.font.SysFont("Calibri", 50)
            fontS = self.font.render(self.text, True, black)
            self.image.fill(white)
            self.fontTam = self.font.size(self.text)
            drawX = (tam / 2) - self.fontTam[0] / 2
            drawY = (tam / 2) - self.fontTam[1] / 2
            self.image.blit(fontS, (drawX, drawY))
        else:
            self.image.fill(blue)

    def update(self):
        self.rect.x = self.x * tam
        self.rect.y = self.y * tam

    def clickMouse(self, mouseX, mouseY):
        return self.rect.left <= mouseX <= self.rect.right and self.rect.top <= mouseY <= self.rect.bottom

    def right(self):
        return self.rect.x + tam < (3 * tam)

    def left(self):
        return self.rect.x - tam >= 0

    def up(self):
        return self.rect.y - tam >= 0

    def down(self):
        return self.rect.y + tam < (3 * tam)


class Interface:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Calibri", 30)
        text = font.render(self.text, True, black)
        screen.blit(text, (self.x, self.y))

class Button:
    def __init__(self, x, y, width, height, text, colour, txtColour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colour = colour
        self.txtColour = txtColour

    def clickMouse(self, mouseX, mouseY):
        return self.x <= mouseX <= self.x + self.width and self.y <= mouseY <= self.y + self.height
        
    def drawButton(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Calibri", 30)
        text = font.render(self.text, True, self.txtColour)
        self.fontTam = font.size(self.text)
        drawX = self.x + (self.width / 2) - self.fontTam[0] / 2
        drawY = self.y + (self.height / 2) - self.fontTam[1] / 2
        screen.blit(text, (drawX, drawY))
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TILE_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH //TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE
FPS = 540


BLACK = (0,0,0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()


def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])

def DrawGrid(positions):
    for position in positions:
        column, row = position
        top_left = (column * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (SCREEN_WIDTH, row * TILE_SIZE))

    for column in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (column * TILE_SIZE, 0), (column * TILE_SIZE, SCREEN_HEIGHT))

def AdjustGrid(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = GetNeighbors(position)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2,3]:
            new_positions.add(position)
    for position in all_neighbors:
        neighbors = GetNeighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions
def GetNeighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1,0,1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1,0,1]:
            if (dx == 0 and dy == 0) or (y + dy < 0 or y + dy > GRID_HEIGHT):
                continue

            neighbors.append((x + dx, y + dy))
    return neighbors

def main():
    run = True
    playing = False
    count = 0
    update_freq = 120


    positions = set()
    while(run):
        clock.tick(FPS) #LIMITS HOW FAST THE LOOP EXECUTES

        if playing: count += 1

        if count >= update_freq:
            count = 0
            positions = AdjustGrid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                column = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (column, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event. key == pygame.K_SPACE:
                    playing = not playing

                if event. key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(4,10) * GRID_WIDTH)

        screen.fill(GREY)
        DrawGrid(positions)
        pygame.display.update()


    pygame.quit()


if __name__ == "__main__":
    main() #don't run simulation in other files

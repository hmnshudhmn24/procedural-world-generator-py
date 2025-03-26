import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
tile_size = 20
cols, rows = WIDTH // tile_size, HEIGHT // tile_size

# Colors
green = (34, 139, 34)
blue = (70, 130, 180)
brown = (139, 69, 19)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedural World Generator")
clock = pygame.time.Clock()

def generate_world():
    world = []
    for y in range(rows):
        row = []
        for x in range(cols):
            noise = random.random()
            if noise < 0.3:
                row.append(blue)  # Water
            elif noise < 0.6:
                row.append(green)  # Grass
            else:
                row.append(brown)  # Mountain
        world.append(row)
    return world

def draw_world(world):
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen, world[y][x], (x * tile_size, y * tile_size, tile_size, tile_size))

def main():
    world = generate_world()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        draw_world(world)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()
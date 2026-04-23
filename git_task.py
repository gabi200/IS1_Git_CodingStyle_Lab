import random

import pygame

GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 60


def generate_grid() -> list[list[tuple[int, int, int]]]:
    """Generate a 10x10 grid of random RGB colors."""
    return [
        [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


def draw_grid(surface: pygame.Surface, grid: list[list[tuple[int, int, int]]]) -> None:
    """Draw the color grid onto the given surface."""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, grid[y][x], rect)


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")
    clock = pygame.time.Clock()

    grid = generate_grid()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                grid = generate_grid()

        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
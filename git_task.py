import random

import pygame

# --- Constants ---
GRID_SIZE = 10       # Number of cells along each axis
CELL_SIZE = 50       # Pixel dimensions of each cell
WINDOW_SIZE = GRID_SIZE * CELL_SIZE  # Total window width and height in pixels
FPS = 60             # Cap the loop to 60 frames per second
REGEN_INTERVAL = 5000  # Auto-regenerate the grid every 5 seconds (in milliseconds)


def generate_grid() -> list[list[tuple[int, int, int]]]:
    """Generate a 10x10 grid of random RGB colors."""
    # Build a 2D list where each cell holds a random (R, G, B) tuple
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
            # Convert grid coordinates to pixel coordinates for the rectangle
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, grid[y][x], rect)


def main() -> None:
    pygame.init()

    # --- Window setup ---
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")
    clock = pygame.time.Clock()

    # Register a custom timer event that fires every REGEN_INTERVAL milliseconds
    REGEN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(REGEN_EVENT, REGEN_INTERVAL)

    # Generate the initial grid and start the main loop
    grid = generate_grid()
    running = True

    while running:
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Close button pressed — exit the loop
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                grid = generate_grid()  # Spacebar pressed — regenerate immediately
            elif event.type == REGEN_EVENT:
                grid = generate_grid()  # Timer fired — auto-regenerate every 5 seconds

        # --- Drawing ---
        screen.fill((0, 0, 0))   # Clear the screen with black each frame
        draw_grid(screen, grid)  # Paint all grid cells
        pygame.display.flip()    # Push the updated frame to the display

        clock.tick(FPS)          # Throttle to the target frame rate

    pygame.quit()


if __name__ == "__main__":
    main()
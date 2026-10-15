
import random
import pygame

# ==========================================
# SNAKE GAME USING PYTHON AND PYGAME
# ==========================================

pygame.init()

# Screen settings
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 25

WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Snake Game")

clock = pygame.time.Clock()

# Colors: RGB values
BLACK = (20, 20, 25)
GREEN = (50, 205, 80)
DARK_GREEN = (30, 140, 55)
RED = (240, 65, 65)
WHITE = (245, 245, 245)
GRAY = (45, 45, 55)
YELLOW = (255, 220, 70)

font = pygame.font.SysFont("arial", 25, bold=True)
small_font = pygame.font.SysFont("arial", 18)


def create_food(snake):
    """Create food at a position not occupied by the snake."""
    available = [
        (x, y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x, y) not in snake
    ]

    if not available:
        return None

    return random.choice(available)


def reset_game():
    """Create a fresh game and return its initial state."""
    snake = [
        (GRID_WIDTH // 2, GRID_HEIGHT // 2),
        (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
        (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2),
    ]

    direction = (1, 0)
    food = create_food(snake)
    score = 0

    return snake, direction, food, score, False, False


def draw_text(text, font_object, color, x, y, center=True):
    """Display text on the game screen."""
    image = font_object.render(text, True, color)

    if center:
        rect = image.get_rect(center=(x, y))
    else:
        rect = image.get_rect(topleft=(x, y))

    screen.blit(image, rect)


def draw_game(snake, food, score, game_over, paused):
    """Draw the background, snake, food and score."""
    screen.fill(BLACK)

    # Draw subtle grid lines
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    # Draw food
    if food is not None:
        food_x, food_y = food
        food_rect = pygame.Rect(
            food_x * CELL_SIZE + 2,
            food_y * CELL_SIZE + 2,
            CELL_SIZE - 4,
            CELL_SIZE - 4,
        )
        pygame.draw.ellipse(screen, RED, food_rect)

    # Draw snake
    for index, (x, y) in enumerate(snake):
        rect = pygame.Rect(
            x * CELL_SIZE + 1,
            y * CELL_SIZE + 1,
            CELL_SIZE - 2,
            CELL_SIZE - 2,
        )

        color = GREEN if index == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, rect, border_radius=5)

    # Score
    draw_text(f"Score: {score}", font, WHITE, 10, 8, center=False)

    if paused and not game_over:
        draw_text(
            "PAUSED",
            font,
            YELLOW,
            WIDTH // 2,
            HEIGHT // 2,
        )
        draw_text(
            "Press SPACE to resume",
            small_font,
            WHITE,
            WIDTH // 2,
            HEIGHT // 2 + 35,
        )

    if game_over:
        draw_text(
            "GAME OVER",
            font,
            RED,
            WIDTH // 2,
            HEIGHT // 2 - 45,
        )
        draw_text(
            f"Final Score: {score}",
            font,
            WHITE,
            WIDTH // 2,
            HEIGHT // 2,
        )
        draw_text(
            "Press R to restart or Q to quit",
            small_font,
            YELLOW,
            WIDTH // 2,
            HEIGHT // 2 + 45,
        )

    pygame.display.flip()


def main():
    snake, direction, food, score, game_over, paused = reset_game()

    running = True
    next_direction = direction

    while running:
        # Handle keyboard and window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

                elif event.key == pygame.K_r and game_over:
                    (
                        snake,
                        direction,
                        food,
                        score,
                        game_over,
                        paused,
                    ) = reset_game()
                    next_direction = direction

                elif event.key == pygame.K_SPACE:
                    if not game_over:
                        paused = not paused

                elif not game_over and not paused:
                    # Do not allow immediate reversal
                    if event.key in (pygame.K_UP, pygame.K_w):
                        if direction != (0, 1):
                            next_direction = (0, -1)

                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        if direction != (0, -1):
                            next_direction = (0, 1)

                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        if direction != (1, 0):
                            next_direction = (-1, 0)

                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        if direction != (-1, 0):
                            next_direction = (1, 0)

        if not game_over and not paused:
            direction = next_direction

            # Calculate the next head position
            head_x, head_y = snake[0]
            dx, dy = direction

            new_head = (head_x + dx, head_y + dy)

            # Check wall collision
            hit_wall = (
                new_head[0] < 0
                or new_head[0] >= GRID_WIDTH
                or new_head[1] < 0
                or new_head[1] >= GRID_HEIGHT
            )

            # Check whether food is eaten
            eating = new_head == food

            # The tail moves away unless food is eaten.
            # This allows moving into the current tail cell safely.
            body_to_check = snake if eating else snake[:-1]
            hit_self = new_head in body_to_check

            if hit_wall or hit_self:
                game_over = True

            else:
                snake.insert(0, new_head)

                if eating:
                    score += 10
                    food = create_food(snake)
                    if food is None:
                        game_over = True
                else:
                    snake.pop()

        draw_game(snake, food, score, game_over, paused)

        # Increase speed as the score increases
        speed = min(18, 8 + score // 50)
        clock.tick(speed)

    pygame.quit()


if __name__ == "__main__":
    main()

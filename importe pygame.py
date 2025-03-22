import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 45
BIRD_SIZE = 20
PIPE_WIDTH = 60
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_VELOCITY = -10
PIPE_VELOCITY = 3
FONT_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 191, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixelated Flappy Bird")

# Load fonts
font = pygame.font.SysFont("arial", FONT_SIZE)

# Bird class
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = JUMP_VELOCITY

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y >= HEIGHT - BIRD_SIZE:  # Hit the ground
            self.y = HEIGHT - BIRD_SIZE
            self.velocity = 0

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, BIRD_SIZE, BIRD_SIZE))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT - PIPE_GAP - 100)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP)
        self.passed = False

    def move(self):
        self.x -= PIPE_VELOCITY
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

    def off_screen(self):
        return self.x + PIPE_WIDTH < 0

# Main game loop
def game_loop():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BLUE)  # Sky color

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Bird movement
        bird.move()
        bird.draw()

        # Pipe movement and generation
        if pipes[-1].x < WIDTH - 300:  # Create new pipe when the last one is far enough
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.move()
            pipe.draw()
            if pipe.off_screen():
                pipes.remove(pipe)

            # Check if the bird has passed the pipe
            if not pipe.passed and bird.x > pipe.x + PIPE_WIDTH:
                pipe.passed = True
                score += 1  # Increment score when passing through a pipe

        # Collision detection
        for pipe in pipes:
            if bird.x + BIRD_SIZE > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + BIRD_SIZE > pipe.height + PIPE_GAP:
                    running = False  # Game over on collision

        # Draw the score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.flip()

    # Game Over screen
    game_over_text = font.render("Game Over!", True, BLACK)
    final_score_text = font.render(f"Score: {score}", True, BLACK)
    screen.fill(WHITE)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))
    screen.blit(final_score_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Show game over for 3 seconds
    pygame.quit()

# Run the game loop
game_loop()

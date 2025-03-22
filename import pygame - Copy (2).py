import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
FPS = 144
DINO_WIDTH, DINO_HEIGHT = 50, 50
CACTUS_WIDTH, CACTUS_HEIGHT = 20, 40
JUMP_VELOCITY = -15
GRAVITY = 1
MAX_JUMP_HEIGHT = 15
CACTUS_VELOCITY = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 250)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Google Dinosaur Game")

# Load dinosaur image
dino_img = pygame.Surface((DINO_WIDTH, DINO_HEIGHT))
dino_img.fill(GREEN)

# Create a clock object to manage FPS
clock = pygame.time.Clock()

# Dinosaur class
class Dinosaur:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - DINO_HEIGHT - 10
        self.velocity = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity = JUMP_VELOCITY
            self.is_jumping = True

    def move(self):
        if self.is_jumping:
            self.y += self.velocity
            self.velocity += GRAVITY
            if self.y >= HEIGHT - DINO_HEIGHT - 10:
                self.y = HEIGHT - DINO_HEIGHT - 10
                self.is_jumping = False

    def draw(self):
        screen.blit(dino_img, (self.x, self.y))

# Cactus class
class Cactus:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT - CACTUS_HEIGHT - 10
        self.width = CACTUS_WIDTH
        self.height = CACTUS_HEIGHT
        self.color = BROWN

    def move(self):
        self.x -= CACTUS_VELOCITY
        if self.x < -self.width:
            self.x = WIDTH + random.randint(100, 500)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Main Game Loop
def game_loop():
    # Create a dinosaur instance
    dino = Dinosaur()
    cacti = [Cactus() for _ in range(3)]  # Create a list of cacti

    score = 0
    running = True
    while running:
        clock.tick(FPS)
        screen.fill(SKY_BLUE)  # Background color

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Jump when spacebar is pressed
                    dino.jump()

        # Move and draw the dinosaur
        dino.move()
        dino.draw()

        # Move and draw cacti
        for cactus in cacti:
            cactus.move()
            cactus.draw()

            # Collision detection
            if (dino.x + DINO_WIDTH > cactus.x and dino.x < cactus.x + cactus.width and
                dino.y + DINO_HEIGHT > cactus.y):
                running = False  # End game on collision

        # Update score (each frame passed = 1 point)
        score += 1

        # Draw score on the screen
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (WIDTH - 150, 20))

        # Update the screen
        pygame.display.flip()

    # Game Over Screen
    game_over_font = pygame.font.SysFont(None, 50)
    game_over_text = game_over_font.render("Game Over!", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))

    pygame.display.flip()
    pygame.time.wait(3000)  # Show game over for 3 seconds
    pygame.quit()

# Run the game loop
game_loop()

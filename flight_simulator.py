import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)  # Color for afterburners
ORANGE = (255, 165, 0)  # Color for afterburners

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flight Simulator")

# Aircraft class
class Aircraft:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.width = 60
        self.height = 30
        self.speed = 5

    def draw(self, screen):
        # Draw the fighter jet (simple representation)
        pygame.draw.polygon(screen, BLUE, [
            (self.x, self.y),  # Nose
            (self.x - self.width // 2, self.y + self.height),  # Left wing
            (self.x + self.width // 2, self.y + self.height),  # Right wing
        ])
        # Draw afterburners
        self.draw_afterburners(screen)

    def draw_afterburners(self, screen):
        # Draw two afterburners behind the aircraft
        afterburner_width = 15
        afterburner_height = 10
        afterburner_offset = 5  # Offset from the aircraft

        # Left afterburner
        pygame.draw.ellipse(screen, ORANGE, (self.x - afterburner_width, self.y + afterburner_offset, afterburner_width, afterburner_height))
        # Right afterburner
        pygame.draw.ellipse(screen, YELLOW, (self.x + self.width, self.y + afterburner_offset, afterburner_width, afterburner_height))

    def move(self, keys):
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

# Obstacle class
class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = random.randint(0, SCREEN_HEIGHT - 50)
        self.width = 50
        self.height = 50

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= 5

# Main game loop
def main():
    clock = pygame.time.Clock()
    aircraft = Aircraft()
    obstacles = []
    score = 0
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        aircraft.move(keys)
        aircraft.draw(screen)

        # Create obstacles
        if random.randint(1, 100) < 5:  # 5% chance to create an obstacle
            obstacles.append(Obstacle())

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw(screen)
            if obstacle.x < 0:
                obstacles.remove(obstacle)
                score += 1  # Increase score when obstacle is passed

            # Collision detection
            if (aircraft.x < obstacle.x + obstacle.width and
                aircraft.x + aircraft.width > obstacle.x and
                aircraft.y < obstacle.y + obstacle.height and
                aircraft.y + aircraft.height > obstacle.y):
                print("Game Over! Your score:", score)
                running = False

        # Display score
        font = pygame.font.SysFont("comicsans", 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import random


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
DINO_WIDTH = 40
DINO_HEIGHT = 40
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 40
GRAVITY = 1
JUMP_STRENGTH = 10  # Lower jump strength for a more realistic jump


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


dino_image = pygame.image.load('c:\Users\Administrator\Downloads\dinosaur.png')
dino_image = pygame.transform.scale(dino_image, (DINO_WIDTH, DINO_HEIGHT))
cactus_image = pygame.image.load('c:\Users\Administrator\Downloads\cactus.png')
cactus_image = pygame.transform.scale(cactus_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dinosaur Game")


class Dinosaur:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT - DINO_HEIGHT
        self.width = DINO_WIDTH
        self.height = DINO_HEIGHT
        self.is_jumping = False
        self.jump_count = JUMP_STRENGTH

    def draw(self):
        screen.blit(dino_image, (self.x, self.y))

    def jump(self):
        if self.is_jumping:
            if self.jump_count >= -JUMP_STRENGTH:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = JUMP_STRENGTH


class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - OBSTACLE_HEIGHT
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT

    def draw(self):
        screen.blit(cactus_image, (self.x, self.y))

    def move(self):
        self.x -= 5


def main():
    clock = pygame.time.Clock()
    dino = Dinosaur()
    obstacles = []
    score = 0
    run = True

    while run:
        clock.tick(30)
        screen.fill(WHITE)

      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not dino.is_jumping:
            dino.is_jumping = True

       
        dino.jump()

        if random.randint(1, 100) < 5:  # 5% chance to create an obstacle
            obstacles.append(Obstacle())

       
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw()
            if obstacle.x < 0:
                obstacles.remove(obstacle)
                score += 1  # Increase score when obstacle is passed

           
            if (dino.x < obstacle.x + obstacle.width and
                dino.x + dino.width > obstacle.x and
                dino.y < obstacle.y + obstacle.height and
                dino.y + dino.height > obstacle.y):
                print("Game Over! Your score:", score)
                run = False

       
        dino.draw()

       
        font = pygame.font.SysFont("comicsans", 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

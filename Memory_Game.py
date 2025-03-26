import pygame
import random
import time

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 4
CARD_SIZE = WIDTH // GRID_SIZE

# Generate number pairs
numbers = list(range(1, (GRID_SIZE * GRID_SIZE // 2) + 1)) * 2
random.shuffle(numbers)
board = [numbers[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)

# Fonts
font = pygame.font.Font(None, 80)
timer_font = pygame.font.Font(None, 40)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Card Game")

def draw_card(x, y, num, revealed, matched):
    """ Draw a card on the board """
    rect = pygame.Rect(x * CARD_SIZE, y * CARD_SIZE, CARD_SIZE, CARD_SIZE)
    pygame.draw.rect(screen, BLUE if not revealed and not matched else WHITE, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    if revealed or matched:
        text = font.render(str(num), True, BLACK)
        screen.blit(text, (x * CARD_SIZE + CARD_SIZE // 3, y * CARD_SIZE + CARD_SIZE // 4))

# Card state tracking
revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
selected = []
matched = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]

# Timer
start_time = time.time()

# Game loop
running = True
while running:
    screen.fill(WHITE)
    elapsed_time = round(time.time() - start_time, 2)
    timer_text = timer_font.render(f"Time: {elapsed_time} sec", True, BLACK)
    screen.blit(timer_text, (20, 20))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and len(selected) < 2:
            x, y = event.pos[0] // CARD_SIZE, event.pos[1] // CARD_SIZE
            if not revealed[y][x] and not matched[y][x]:
                revealed[y][x] = True
                selected.append((x, y))
    
    # Draw cards
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            draw_card(i, j, board[j][i], revealed[j][i], matched[j][i])
    
    pygame.display.flip()
    
    # Check for a match
    if len(selected) == 2:
        pygame.time.delay(500)  # Pause for 0.5 seconds to show the second card
        x1, y1 = selected[0]
        x2, y2 = selected[1]
        if board[y1][x1] == board[y2][x2]:
            matched[y1][x1] = True
            matched[y2][x2] = True
        else:
            revealed[y1][x1] = False
            revealed[y2][x2] = False
        selected = []
    
    if all(all(row) for row in matched):
        print(f"You won in {elapsed_time} seconds!")
        running = False

pygame.quit()

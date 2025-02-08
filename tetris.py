import pygame
import time
import random
pygame.init()
pygame.mixer.init()

music = pygame.mixer.Sound('tetris.wav')

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

def add_line(screen, text, x, y):
    # used to print the status of the variables
    text = font.render(text, True, (200, 200, 200))
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)

font = pygame.font.Font("freesansbold.ttf", 32)

points = 0

blocks = []

jl = input('would you like to play easy, normal, or hard? [e/n/h]').lower()

if jl == 'e':
    pblocks = [
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0]], 
            [[0, 0, 0, 0], [30, 0, 30, 0], [30, 30, 30, 30]]
            ]
    


elif jl == 'h':

    pblocks = [
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [120, 0, 120, 0]], 
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [120, 0, 120, 0]], 
            
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [90, 30, 90, 30]], 
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [90, -30, 90, -30]], 
            
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [60, 30, 60, 30]], 
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0], [60, -30, 60, -30]], 
            
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [60, 30, 60, 30], [90, 30, 90, 30]], 
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [60, -30, 60, -30], [90, -30, 90, -30]], 
            
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [0, 30, 0, 30], [0, 60, 0, 60]], 
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [0, -30, 0, -30], [0, -60, 0, -60]], 
            
            [[30, 30, 30, 30], [30, 0, 30, 0], [60, 0, 60, 0], [0, 30, 0, 30], [0, 60, 0, 60]], 
            [[30, -30, 30, -30], [30, 0, 30, 0], [60, 0, 60, 0], [0, -30, 0, -30], [0, -60, 0, -60]], 
            
            [[0, 0, 0, 0], [30, 30, 30, 30], [60, 30, 60, 30], [0, 30, 0, 30], [0, 60, 0, 60]], 
            [[0, 0, 0, 0], [30, -30, 30, -30], [60, -30, 60, -30], [0, -30, 0, -30], [0, -60, 0, -60]], 
            
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [30, 30, 30, 30], [60, 30, 60, 30]], 
            [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [30, -30, 30, -30], [60, -30, 60, -30]], 
            
            [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [60, 30, 60, 30], [60, 0, 60, 0]], 
            [[0, 0, 0, 0], [0, -30, 0, -30], [30, -30, 30, -30], [60, -30, 60, -30], [60, 0, 60, 0]], 
            
            [[30, 0, 30, 0], [0, 30, 0, 30], [30, 30, 30, 30], [60, 30, 60, 30], [30, 60, 30, 60]], 
            [[30, 0, 30, 0], [0, 30, 0, 30], [30, 30, 30, 30], [60, 30, 60, 30], [30, 60, 30, 60]], 
            
            [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [60, 30, 60, 30], [60, 60, 60, 60]], 
            [[0, 0, 0, 0], [0, -30, 0, -30], [30, -30, 30, -30], [60, -30, 60, -30], [60, -60, 60, -60]], 
            
            [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [60, 30, 60, 30], [30, 60, 30, 60]], 
            [[0, 0, 0, 0], [0, -30, 0, -30], [30, -30, 30, -30], [60, -30, 60, -30], [30, -60, 30, -60]], 
            ]

else:
    # Default to four squares per piece
    square_tetra = [[0, 0, 0, 0], [30, 0, 30, 0], [0, 30, 0, 30], [30, 30, 30, 30]]

    pblocks = [
                [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [30, 60, 30, 60]],
                [[0, 0, 0, 0], [0, 30, 0, -30], [-30, 30, -30, 30], [-30, 60, -30, 60]], 
                square_tetra,
                square_tetra,
                [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [60, 30, 60, 30]], 
                [[0, 0, 0, 0], [-30, 0, -30, 0], [-60, 0, -60, 0], [-60, 30, -60, 30]], 
                [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0]], 
                [[0, 0, 0, 0], [30, 0, 30, 0], [60, 0, 60, 0], [90, 0, 90, 0]], 
                [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [-30, 30, -30, 30]], 
                [[0, 0, 0, 0], [0, 30, 0, 30], [30, 30, 30, 30], [-30, 30, -30, 30]], 
               ]




nblock = random.choice(pblocks)
no_rotate = False

# cblocks = random.choice(pblocks)
cblocks = []


posx, posy = 0, 0

time1 = 0

pygame.mixer.Sound.play(music)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

r = 0

pressed = False

# Run until the user asks to quit
running = True
while running:
    # Fill the background with white
    screen.fill((0, 0, 0))
    pygame.event.poll()
    keys = pygame.key.get_pressed()
    
    if r <= 1:
        pygame.mixer.Sound.play(music)
    
    if r > (points*10 + 30)*10.5:
        r = 0
    
    if keys[pygame.K_s]:
        if time1 % 2 == 0:
            for i in cblocks:
                i[1] += 30
    
    
    if not pressed:
        if keys[pygame.K_d]:
            for i in cblocks:
                i[0] += 30
        if keys[pygame.K_a]:
            for i in cblocks:
                i[0] -= 30

        # Rotate block
        if keys[pygame.K_e] and not no_rotate:
            b = -1
            c = 1
            for i in cblocks:
                u = cblocks[1]  # axis of rotation
                n = i[0] - u[0]
                m = i[1] - u[1]
                i[0] = m*b + u[0]
                i[1] = n*c + u[1]
        if keys[pygame.K_r] and not no_rotate:
            b = 1
            c = -1
            for i in cblocks:
                u = cblocks[0]
                n = i[0] - u[0]
                m = i[1] - u[1]
                i[0] = m*b + u[0]
                i[1] = n*c + u[1]
    
    if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_r] or keys[pygame.K_e]:
        pressed = True
    else:
        pressed = False
    
    for i in blocks:
        if i[1] == 0:
            running = False
    
    r += 1
    
    time1 += 1
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not cblocks:
        # update the current and next block
        tmp_block = nblock
        nblock = random.choice(pblocks)
        no_rotate = tmp_block is square_tetra
        
        for square in tmp_block:
            cblocks.append([square[0] + 300, square[1], square[0] + 300, square[1]])
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    
    for i in cblocks:
        if time1 % 20 == 0:
            i[1] += 30
        if i[1] >= 600:
            for i in cblocks:
                i[0] = i[2]
                i[1] = i[3]
                blocks.append([i[0], i[1], color])
            cblocks = []
    
    
    j = False
    
    # Freeze a block when it collides with another block
    for i in cblocks:
        for j in blocks:
            if i[0] == j[0]:
                if i[1] == j[1]:
                    for i in cblocks:
                        i[0] = i[2]
                        i[1] = i[3]
                        blocks.append([i[0], i[1], color])
                    cblocks = []

    # Clearing lines
    for i in range(20):
        # Check number of blocks in a row
        h = []
        for j in blocks:
            if j[1] == i*30:
                h.append(j)

        # If blocks in a row is 10 or more, clear it
        if len(h) >= 10:
            for i in h:
                blocks.remove(i)
            for l in blocks:
                if l[1] < h[0][1]:
                    l[1] += 30
            points += 1
            pygame.time.delay(100)

    # Check for edge collisions
    for i in cblocks:
        if i[0] < 150:
            for i in cblocks:
                i[0] = i[2]
                i[1] = i[3]
        if i[0] > 420:
            for i in cblocks:
                i[0] = i[2]
                i[1] = i[3]
    for i in cblocks:
        map1 = pygame.Rect(i[0] + 1, i[1] + 1, 28, 28)
        pygame.draw.rect(screen, color, map1)
        
    for i in blocks:
        map1 = pygame.Rect(i[0] + 1, i[1] + 1, 28, 28)
        pygame.draw.rect(screen, i[2], map1)
    
    map1 = pygame.Rect(0, 0, 150, 600)
    pygame.draw.rect(screen, (128, 128, 128), map1)
    
    map1 = pygame.Rect(450, 0, 150, 600)
    pygame.draw.rect(screen, (128, 128, 128), map1)
    
    map1 = pygame.Rect(480, 100, 120, 120)
    pygame.draw.rect(screen, (0, 0, 0), map1)
    
    for i in nblock:
        map1 = pygame.Rect(i[0]/2 + 520, i[1]/2 + 120, 13, 13)
        pygame.draw.rect(screen, (200, 200, 200), map1)
    
    add_line(screen, f'points: {points}', 0, 0)
    
    for i in cblocks:
        i[2] = i[0]
        i[3] = i[1]
    
    time.sleep(1/(points*3 + 30))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

print(str(points)  + ' points')

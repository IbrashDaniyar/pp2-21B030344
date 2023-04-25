import pygame, enum, random, time
from pygame.mixer import music


# constants
BLOCK_COLOR = (255, 0, 0)
WIDTH, HEIGHT = 600, 600
FPS = 10
BLOCK_SIZE = 10
COUNTER = 0
SCORE = 0

# class Block for snake head and body
class Block:
    def __init__(self, screen, x, y, color= pygame.Color('red')):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.disappear = False 
    
    def init_timer(self, time):
        if self.disappear:
            self.event = pygame.USEREVENT + time
            pygame.time.set_timer(self.event, time * 1000)
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        
    def collide(self, other):
        return self.x == other.x and self.y == other.y

class Direction(enum.Enum):
    up = 4
    down = 3
    left = 2
    right = 1

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4474a2e... commit
=======
>>>>>>> 1f284975c03986ee3845dd5c4a50f0eb6ec17a30
# # Function to get wall positions
# def wall_poses(screen):
#     poses = []
#     for i in range(N - 1):
#         for j in range(M - 1):
#             c = screen.get_at((i * CELL + 1, j * CELL + 1))
#             if c[0] < 20 and c[1] < 20 and c[2] < 20:
#                 poses.append([i, j])
#     return poses
<<<<<<< HEAD
<<<<<<< HEAD
=======
# Function to get wall positions
def wall_poses(screen):
    poses = []
    for i in range(N - 1):
        for j in range(M - 1):
            c = screen.get_at((i * CELL + 1, j * CELL + 1))
            if c[0] < 20 and c[1] < 20 and c[2] < 20:
                poses.append([i, j])
    return poses
>>>>>>> 7ea8f7e... Final commit
=======
>>>>>>> 4474a2e... commit
=======
>>>>>>> 1f284975c03986ee3845dd5c4a50f0eb6ec17a30



def menu(screen):

<<<<<<< HEAD
<<<<<<< HEAD
    image_menu = pygame.image.load('images/snake_menu.jpg')#.convert_alpha
=======
    image_menu = pygame.image.load('images/snake_menu.png')#.convert_alpha
>>>>>>> 7ea8f7e... Final commit
=======
    image_menu = pygame.image.load('images/snake_menu.png')#.convert_alpha
>>>>>>> 1f284975c03986ee3845dd5c4a50f0eb6ec17a30
    image_menu = pygame.transform.scale(image_menu, (WIDTH, HEIGHT))
    screen.blit(image_menu, (0, 0))
    pygame.display.update()
    
    going = True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 250 <= event.pos[0] <= 350 and 240 <= event.pos[1] <= 280:
                    going = False
                    return True
                if 250 <= event.pos[0] <= 350 and 290 <= event.pos[1] <= 310:
                    going = False
                    return False            
                if 250 <= event.pos[0] <= 350 and 315 <= event.pos[1] <= 450:
                    pygame.quit()

def main():
    
    pygame.init()
    global COUNTER, FPS, SCORE
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake_game in 1989')
    
    
    clock = pygame.time.Clock()  
    
    head = Block(screen, 100, 100)
    body = [Block(screen, 100 - BLOCK_SIZE, 100), Block(screen, 100 - 2 * BLOCK_SIZE, 100)]
    food = Block(screen, WIDTH // 2, HEIGHT // 2)
    main_food = Block(screen, WIDTH // 3, HEIGHT // 3, pygame.Color('blue'))
    
    direction = Direction.right
    
    FONT = pygame.font.SysFont('Arial', 20)
    FONT1 = pygame.font.SysFont('Arial', 17)
    text_score = FONT.render(f'score: {SCORE}', True, (0))
    text_speed = FONT.render(f'speed: {FPS}', True, (0))
    
    if menu(screen):
        
        
        going = True
        while going:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    going = False
                
                if main_food.disappear:
                    if event.type == main_food.event:
                        main_food.x = 1000
                                
            # events in keyboard buttons
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and direction != Direction.down:
                direction = Direction.up
            elif key[pygame.K_DOWN] and direction != Direction.up:
                direction = Direction.down
            elif key[pygame.K_LEFT] and direction != Direction.right:
                direction = Direction.left
            elif key[pygame.K_RIGHT] and direction != Direction.left:
                direction = Direction.right

            # defined that snake head collisioned with body
            for i in body:
                if head.collide(i):
                    pygame.mixer.music.load('sounds/crush.mp3')
                    pygame.mixer.music.play()
                    time.sleep(2)
                    going = False

            # defined that snakes and foods are collisioned
            if head.collide(food):

                pygame.mixer.music.load('sounds/eating.mp3')
                pygame.mixer.music.play()
                SCORE += 5
                COUNTER += 1
                if COUNTER % 3 == 0:
                    FPS += 1
                body.append(Block(screen, body[-1].x, body[-1].y))
                search = True
                while search:
                    food.x = random.randint(0, WIDTH // BLOCK_SIZE - 10) * BLOCK_SIZE
                    food.y = random.randint(0, HEIGHT // BLOCK_SIZE - 10) * BLOCK_SIZE
                    if head.collide(food):
                        continue
                    search = False
                    for i in body:
                        if i.collide(food):
                            search = True
                            break
               
            if head.collide(main_food):

                pygame.mixer.music.load('sounds/eating.mp3')
                pygame.mixer.music.play()
                SCORE += 25
                COUNTER += 1
                if COUNTER % 3 == 0:
                    FPS += 1
                body.append(Block(screen, body[-1].x, body[-1].y))
                main_food.x = -20
                main_food.y = -20
                search = True
                while search:
                    food.x = random.randint(0, WIDTH // BLOCK_SIZE - 10) * BLOCK_SIZE
                    food.y = random.randint(0, HEIGHT // BLOCK_SIZE - 10) * BLOCK_SIZE
                    if head.collide(main_food):
                        continue
                    search = False
                    for i in body:
                        if i.collide(main_food):
                            search = True
                            break         
            # adding head in first position 
            body.insert(0, Block(screen, head.x, head.y))

            # delete last element in the body
            body.pop()

            # define (dx, dy) to snake
            if direction == Direction.up:      head.y -= BLOCK_SIZE         
            elif direction == Direction.down:  head.y += BLOCK_SIZE
            elif direction == Direction.left:  head.x -= BLOCK_SIZE
            elif direction == Direction.right: head.x += BLOCK_SIZE

            # walls
            if head.x < -10:        
                going = False 
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()
            if head.x > HEIGHT + 10:   
                going = False
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()
            if head.y < -10:        
                going = False
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()
            if head.y > WIDTH + 10:    
                going = False
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()

            # strings about score and speed
            text_score = FONT.render(f'score: {SCORE}', True, (0))
            text_speed = FONT.render(f'speed: {FPS}', True, (0))

            # we must fill screen
            screen.fill((255, 255, 255))

            # draw food
            food.draw()

            if COUNTER % 3 == 0 and COUNTER != 0:
                main_food.disappear = True
                main_food.init_timer(3)
                main_food.draw()
            
            # draw all body except head
            for i in body:
                i.draw()

            # output texts score and speed
            screen.blit(text_score, (5, 5))
            screen.blit(text_speed, (5, 25))

            # update the screen
            pygame.display.update()

            # FramePerSecond
            clock.tick(FPS)

        # close library pygame
        pygame.quit()
    
    else:
        screen.fill((25, 255, 25))
        about_image = pygame.image.load('images/about.png')
        about_image = pygame.transform.scale(about_image, (WIDTH, HEIGHT))
        text0 = 'Snake game'
        text1 = 'Inspired by zetcode.com Java 2D games'
        text2 = 'Snake is a video game that originated during the late 1970s in arcades becoming'
        text3 = 'something of a classic. It became the standard pre-loaded game'
        text4 = 'on Nokia phones in 1998.'
        text5 = 'The player controls a long, thin creature,'
        text6 = 'resembling a snake, which roams around on'
        text7 = 'a bordered plane, picking up food (or some'
        text8 = 'other item), trying to avoid hitting its own tail'
        text9 = 'or the edges of the playing area. Each time'
        text10 = 'the snake eats a piece of food, its tail grows'
        text11 = 'longer, making the game increasingly'
        text12 = 'difficult. The user controls the direction of'
        text13 = "the snake's head (up, down, left, or right),"
        text14 = "and the snake's body follows."
        text = [text0, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14]
    
        # text_about = FONT1.render(f'More Information: \n{text}', True, (255, 0, 0))
    
        text_exit = FONT.render('EXIT', True, (0, 0, 0))
        text_about = FONT.render('More Information:', True, (0, 0, 255))
        screen.blit(about_image, (0, 0))
        screen.blit(text_about, (10, 10))
        
        going = True
        while going:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    going = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 500 <= event.pos[0] <= 520 and 540 <= event.pos[1] <= 560:
                        main()
            
            for i in range(15):
                text_about = FONT1.render(f'{text[i]}', True, (0, 0, 0))
                screen.blit(text_about, (15, 15 + (i + 1) * 30))
            
            screen.blit(text_exit, (500, 540))
            pygame.display.update()
            clock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()
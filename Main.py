import pygame
def main():
    pygame.init()
    screen_width,screen_height=500,500
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    current_color = pygame.Color("white")
    x,y = 30,30
    sprite_width, sprite_height = 60,60
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x = x-3
        if pressed[pygame.K_RIGHT]: 
            x = x+3
        if pressed[pygame.K_UP]:
            y= y-3
        if pressed[pygame.K_DOWN]:y = y+3
        x = min(max(0,x),screen_width-sprite_width)
        y = min(max(0,y),screen_height-sprite_height)

        if x == 0:
            current_color = pygame.Color("blue")
        elif x == screen_width - sprite_width:
            current_color = pygame.Color("yellow")
        elif y == 0:
            current_color = pygame.Color("red")
        elif y == screen_height - sprite_height:
            current_color = pygame.Color("green")
        else:
            current_color = pygame.Color("white")
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_color,(x,y,sprite_width,sprite_height),0)
        pygame.display.flip()
        clock.tick(90)
if __name__ == "__main__":
    main()


        

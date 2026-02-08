import pygame
def main():
    pygame.init()
    screen_width,screen_height=500,500
    screen = pygame.display.set_mode((screen_width,screen_height))
    color = pygame.Color("white")
    x,y = 220,220
    sheight,swidth = 60,60
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0,0,0))
        pygame.draw.rect(screen,color,(x,y,swidth,sheight),0)
        pygame.draw.rect(screen,pygame.Color("red"),(x+100,y,swidth,sheight),2)
        pygame.draw.circle(screen,pygame.Color("blue"),(60,60),50,0)
        pygame.draw.circle(screen,pygame.Color("blue"),(170,60),50,5)

        pygame.draw.circle(screen,pygame.Color("red"),(280,60),50,3)
        pygame.draw.circle(screen,pygame.Color("orange"),(280,60),45,3)
        pygame.draw.circle(screen,pygame.Color("yellow"),(280,60),40,3)
        pygame.draw.circle(screen,pygame.Color("green"),(280,60),35,3)
        pygame.draw.circle(screen,pygame.Color("blue"),(280,60),30,3)
        pygame.draw.circle(screen,pygame.Color("pink"),(280,60),25,3)
        pygame.draw.circle(screen,pygame.Color("purple"),(280,60),20,3)
        pygame.draw.circle(screen,pygame.Color("brown"),(280,60),15,3)
        pygame.draw.circle(screen,pygame.Color("white"),(280,60),10,3)
        pygame.draw.circle(screen,pygame.Color("indigo"),(280,60),5,3)
        pygame.draw.circle(screen,pygame.Color("dark green"),(280,60),0,3)
        pygame.display.flip()
        clock.tick(90)

if __name__ == "__main__":
    main()

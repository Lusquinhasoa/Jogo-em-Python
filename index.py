import pygame
pygame.init()
x = 400
y = 300
velocidade = 10
bg = pygame.image.load('Slide1.PNG')
car = pygame.image.load('car.jpg')

window = pygame.display.set_mode ((800,600))
pygame.display.set_caption("New game")

window_open = True
while window_open :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_LEFT]:
        x-= velocidade
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT]:
        x+= velocidade


    window.blit(bg,(0,0))
    window.blit(car,(x,y))
    pygame.display.update()
pygame.quit()
import pygame, sys
import random
pygame.init()
window_width,window_height = 800,700
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('simon says')
superhore={
1: {
  'image': pygame.transform.scale(pygame.image.load('10.png'),
                                  (50, 100)),
  'sound': pygame.mixer.Sound('superman.wav')
},
2: {
  'image': pygame.transform.scale(pygame.image.load('ironman.png'),
                                  (50, 100)),
  'sound': pygame.mixer.Sound('ironman.wav')
},
3: {
  'image': pygame.transform.scale(pygame.image.load('batman.png'),
                                  (50, 100)),
  'sound': pygame.mixer.Sound('batman.wav')
},
4: {
  'image':
  pygame.transform.scale(pygame.image.load('spiderman.png'), (50, 100)),
  'sound':
  pygame.mixer.Sound('spiderman.wav')
},
}
sequence=[]
def masegge(msagge):
   font=pygame.font.SysFont('comicsansms', 30)
   text=font.render(msagge, True, (0, 0, 0))
   text_rect = text.get_rect(center=(window_width // 2, window_height //2))
   window.fill((255, 255, 255))
   window.blit(text, text_rect)
   pygame.display.update()
def dsi():
    for i in range(1,5):
        window.blit(superhore[i]['image'],((i-1)*100+25,150))
    pygame.display.update()
def image(length):

    global sequence
    sequence=[random.randint(1,4) for i in range(length)]
    masegge("simon says")
    for superhore_num in sequence:
        superhore[superhore_num]['sound'].play()
        pygame.time.delay(1000)
    masegge("choose your superhore ")
    dsi()
def suara():
    global sequence
    sequence_length = len(sequence)+1
    image(sequence_length)
    # Wait for the player's response
    for superhero_num in sequence:
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    image_rect = superhore[superhero_num]['image'].get_rect(
                        topleft=((superhero_num - 1) * 100 + 25, 150))
                    if image_rect.collidepoint(mouse_x, mouse_y):
                        waiting_for_input = False
                    else:
                        return False  # Wrong sequence, game over

    return True  # Right sequence, continue
pygame.mixer.init()
ju=False
while not ju:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ju=True
        cs=suara()
        if cs:
            masegge("kamu benar")
            pygame.time.delay(1000)
        else:
            masegge("kamu salah")
            pygame.time.delay(1000)
            ju=True

pygame.quit()
sys.exit()













































































































































































































































































































































































































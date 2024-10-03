import pygame

pygame.init()

# Set screen dimensions

screen_width, screen_height = 400, 400

screen = pygame.display.set_mode((screen_width, screen_height))

# Set window caption

pygame.display.set_caption("Adding Images")

# Load and scale images

background = pygame.transform.scale(pygame.image.load("bg.png").convert(), (screen_width, screen_height))

panda = pygame.transform.scale(pygame.image.load("panda.jpg").convert_alpha(), (200, 200))

# Get the panda's rectangle and position it in the center

penguin_rect = panda.get_rect(center=(screen_width // 2, screen_height // 2 - 30))

done = False

clock = pygame.time.Clock()

# Main loop

while not done:

   for event in pygame.event.get():

         if event.type == pygame.QUIT:

           done = True

# Blit images onto the screen

   screen.blit(background, (0, 0))

   screen.blit(panda, penguin_rect)

# Update the display

   pygame.display.flip()

# Control the frame rate

   clock.tick(30)

# Quit pygame

pygame.quit()
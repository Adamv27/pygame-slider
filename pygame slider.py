import pygame
import math

pygame.init()
screen = pygame.display.set_mode((300,300))

GREY = (160, 160, 160)
DARK_GREY = (120,120,120)

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = pygame.Rect(self.x, self.y, 20, 30)
    def update_area(self):
        self.area = pygame.Rect(self.x, self.y, 20, 30)


class Slider:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.slider_length = 200

    def get_value(self):
        # Faction of how far the slider is along the bar
        position = 1 / (self.slider_length / ((box.x + 10) - 50))

        # Total distance from min to max values
        distance = abs(self.min_value - self.max_value)

        value = round((distance * position) + self.min_value, 1)
        return value

           
def update_slider():   
    screen.fill((0,0,0)) 
    # Draw slider line
    pygame.draw.line(screen, GREY, (50, 150), (250, 150), 3)
    # Draw slider box
    pygame.draw.rect(screen, DARK_GREY, (box.x, box.y, 20, 30))
    pygame.display.update()

    
box = Box(150, 135)
slider = Slider(15,20)
while True:
    update_slider()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        # Only accepts left click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Only if the box is clicked on
            if box.area.collidepoint(event.pos):         
                mouse_down = True
                while mouse_down:
                    for sub_event in pygame.event.get():
                        # Mouse button is released
                        if sub_event.type == pygame.MOUSEBUTTONUP:
                            print(slider.get_value())
                            mouse_down = False
                    
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # If mouse isnt farther than the end of the slider
                    # Update the x value of box and the area
                    if  mouse_x < 250 and mouse_x > 50:
                        box.x = mouse_x - 10    
                        box.update_area()
                        update_slider()

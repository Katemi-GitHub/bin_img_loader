import pygame, sys
from pygame import *
from color import *

pygame.init()
clock = pygame.time.Clock()

bin_info = []
cell_posX, cell_posY = 0, 0
index_x, index_y = 0, 0
type = ''

filename = 'img_data/palette_example_4bit' #Name of the file to display

f = open(filename, 'r')
for data in f:
    info = data.split(' ')
    for x in info:
        bin_info.append('0b' + x)

sizeX, sizeY = int(bin_info[0], 2), int(bin_info[1], 2)
pixel_size = int(bin_info[3], 2)
screenHeight = sizeX * pixel_size
screenWidth = sizeY * pixel_size
bit_sizeX = screenHeight / sizeX
bit_sizeY = screenWidth / sizeY
screen = pygame.display.set_mode((screenHeight, screenWidth))

if int(bin_info[2], 2) == 0:
    type = '4-bit'
elif int(bin_info[2], 2) == 1:
    type = '5-bit'
elif int(bin_info[2], 2) == 2:
    type = '6-bit'

bin_info.pop(0)
bin_info.pop(0)
bin_info.pop(0)
bin_info.pop(0)

while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for cell_index in range(sizeX * sizeY):
        cell_posX = index_x * bit_sizeX
        index_x +=1

        if cell_posX >= screenHeight:
            index_y += 1
            index_x = 1
            cell_posX = 0
            cell_posY = index_y * bit_sizeY
        
        if cell_posY >= screenWidth:
            index_x = 1
            index_y = 0
            cell_posX = 0
            cell_posY = 0

        bit_rect = pygame.Rect(cell_posX, cell_posY, bit_sizeX, bit_sizeY)
        if type == '4-bit':
            color = get_color_4bit(int(bin_info[cell_index], 2))
        elif type == '5-bit':
            color = get_color_5bit(int(bin_info[cell_index], 2))
        elif type == '6-bit':
            color = get_color_6bit(int(bin_info[cell_index], 2))
        pygame.draw.rect(screen, color, bit_rect)

    pygame.display.update()
    clock.tick(60)

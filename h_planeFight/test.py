import pygame
import sys
import math

# 每个程序第一步都要把模块以及显示窗口初始化
pygame.init()
pygame.display.init()

# 创建窗口对象
screen = pygame.display.set_mode((500, 500))
# 窗口标签
pygame.display.set_caption("飞机")
# 窗口图标,先加载图片
icon = pygame.image.load("sources\plane.png")
pygame.display.set_icon(icon)

x = -48
while True:
    # 关闭事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color("white"))
    screen.blit(icon, (x, 200 + 60 * math.sin(x / 20)))
    x += 0.05
    if x >= 500:
        x = -48
    pygame.display.update()

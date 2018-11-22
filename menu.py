#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Menu(object):
    state = -1

    def __init__(self, items, font_color=(0, 0, 0), select_color=(0, 255, 0), ttf_font=None, font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)
        # Gera uma lista que possui o retangulo para cada item
        self.rect_list = self.get_rect_list(items)

    def get_rect_list(self, items):
        rect_list = []
        for index, item in enumerate(items):
            # determina a quantidade de espaço necessária para renderizar texto
            size = self.font.size(item)
            # Obter a largura e altura do texto
            width = size[0]
            height = size[1]

            pos_x = (SCREEN_WIDTH / 2) - (width / 2)
            # t_h: altura total do bloco de texto
            t_h = len(items) * height
            pos_y = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)
            # Cria retangulo
            rect = pygame.Rect(pos_x, pos_y, width, height)
            # Adiciona retangulo da lista
            rect_list.append(rect)

        return rect_list

    def collide_points(self):
        index = -1
        mouse_pos = pygame.mouse.get_pos()
        for i, rect in enumerate(self.rect_list):
            if rect.collidepoint(mouse_pos):
                index = i

        return index

    def update(self):
        # atribui collide_points ao estado
        self.state = self.collide_points()
        
    def display_frame(self, screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.select_color)
            else:
                label = self.font.render(item, True, self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            pos_x = (SCREEN_WIDTH / 2) - (width / 2)
            # t_h: altura total do bloco de texto
            t_h = len(self.items) * height
            pos_y = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)
            
            screen.blit(label, (pos_x, pos_y))

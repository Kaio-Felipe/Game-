#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from game import Game

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def main():
    # Inicializa todos os módulos pygame importados
    pygame.init()
    # Define a largura e altura da tela [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Define a legenda da janela atual
    pygame.display.set_caption("Aprendizagem a Matemática básica")
    # Faça um loop até que o usuário clique no botão Fechar
    done = False
    # Usado para gerenciar a velocidade com que as atualizações de tela
    clock = pygame.time.Clock()
    # Criando o objeto game
    game = Game()
    # -------- Loop do programa inicial -----------
    while not done:
        # --- Processar eventos(keystrokes, mouse clicks, etc)
        done = game.process_events()
        # --- Lógica do jogo
        game.run_logic()
        # --- Desenha o quadro atual
        game.display_frame(screen)
        # --- Limite de 30 quadros por segundo
        clock.tick(30)


    pygame.quit()

if __name__ == '__main__':
    main()

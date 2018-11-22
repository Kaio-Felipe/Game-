#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, random
from menu import Menu

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Game(object):
    def __init__(self):
        # Cria a nova fonte do objeto
        self.font = pygame.font.Font(None, 65)
        # Cria fonte para mensagem
        self.score_font = pygame.font.Font("kenvector_future.ttf", 20)
        # Crie um dicionário com as chaves: num1, num2, result
        # Estas variáveis ​​serão usadas para criar o
        # problema aritmético
        self.problem = {"num1": 0, "num2": 0, "result": 0}
        # Crie uma variável que mantenha o nome da operação
        self.operation = ""
        self.symbols = self.get_symbols()
        self.button_list = self.get_button_list()
        # Criar booleano que será verdade quando clicado no botão do mouse
        # Isso é porque temos que esperar alguns quadros para podermos mostrar
        # o retangulo verde ou vermelho
        self.reset_problem = False
        # Cria o menu
        items = ("Adição", "Subtração", "Multiplicaão", "Divisão")
        self.menu = Menu(items, ttf_font="XpressiveBlack Regular.ttf", font_size=50)
        # True: mostrar o menu
        self.show_menu = True
        # cria o contador de pontos
        self.score = 0
        # Conta o número de problemas
        self.count = 0
        # carrega a imagem de fundo
        self.background_image = pygame.image.load("background.jpg").convert()
        # carrega efeitos sonoros
        self.sound_1 = pygame.mixer.Sound("item1.ogg")
        self.sound_2 = pygame.mixer.Sound("item2.ogg")

    def get_button_list(self):
        """ Retornar uma lista com quatro botões """
        button_list = []
        # atribuir um dos botões com a resposta certa
        choice = random.randint(1, 4)
        # definir a largura e altura
        width = 100
        height = 100
        # t_w: largura total
        t_w = width * 2 + 50
        pos_x = (SCREEN_WIDTH / 2) - (t_w / 2)
        pos_y = 150
        if choice == 1:
            btn = Button(pos_x, pos_y, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(pos_x, pos_y, width, height, random.randint(0, 100))
            button_list.append(btn)

        pos_x = (SCREEN_WIDTH / 2) - (t_w/2) + 150
        
        if choice == 2:
            btn = Button(pos_x, pos_y, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(pos_x, pos_y, width, height, random.randint(0, 100))
            button_list.append(btn)

        pos_x = (SCREEN_WIDTH / 2) - (t_w / 2)
        pos_y = 300

        if choice == 3:
            btn = Button(pos_x, pos_y, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(pos_x, pos_y, width, height, random.randint(0, 100))
            button_list.append(btn)

        pos_x = (SCREEN_WIDTH / 2) - (t_w / 2) + 150
            
        if choice == 4:
            btn = Button(pos_x, pos_y, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(pos_x, pos_y, width, height, random.randint(0, 100))
            button_list.append(btn)

        return button_list

    def get_symbols(self):
        """ Devolve um dicionário com todos os símbolos de operação """
        symbols = {}
        sprite_sheet = pygame.image.load("symbols.png").convert()
        image = self.get_image(sprite_sheet, 0, 0, 64, 64)
        symbols["Adição"] = image
        image = self.get_image(sprite_sheet, 64, 0, 64, 64)
        symbols["Subtração"] = image
        image = self.get_image(sprite_sheet, 128, 0, 64, 64)
        symbols["Multiplicação"] = image
        image = self.get_image(sprite_sheet, 192, 0, 64, 64)
        symbols["Divisão"] = image
        
        return symbols

    def get_image(self, sprite_sheet, x, y, width, height):
        """ Este método irá cortar uma imagem e devolvê-la """
        # Cria uma nova imagem em branco
        image = pygame.Surface([width, height]).convert()
        # Copie o sprite da folha grande para o menor
        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        # Retorna a imagem
        return image

    def addition(self):
        """ Estes irão definir num1, num2, resultado para adição """
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a + b
        self.operation = "Adição"

    def subtraction(self):
        """ Estes irão definir num1, num2, resultado para subtração"""
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        if a > b:
            self.problem["num1"] = a
            self.problem["num2"] = b
            self.problem["result"] = a - b
        else:
            self.problem["num1"] = b
            self.problem["num2"] = a
            self.problem["result"] = b - a
        self.operation = "Subtração"

    def multiplication(self):
        """ Estes irão definir  num1,num2, resultado da multiplicação """
        a = random.randint(0, 12)
        b = random.randint(0, 12)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a * b
        self.operation = "multiplicação"

    def division(self):
        """ Estes irão definir num1,num2, resultado da divisão """
        divisor = random.randint(1, 12)
        dividend = divisor * random.randint(1, 12)
        quotient = dividend / divisor
        self.problem["num1"] = dividend
        self.problem["num2"] = divisor
        self.problem["result"] = quotient
        self.operation = "divisão"

    def check_result(self):
        """ Checar o resultado """
        for button in self.button_list:
            if button.isPressed():
                if button.get_number() == self.problem["result"]:
                    # definir cor para verde quando correto
                    button.set_color(GREEN)
                    # aumentar pontuação
                    self.score += 5
                    # Reproduzir efeito sonoro
                    self.sound_1.play()
                else:
                    # definir cor para vermelho quando incorreto
                    button.set_color(RED)
                    # reproduzir efeitos sonoros
                    self.sound_2.play()
                # Defina reset_problem True para poder ir ao
                # próximo problema
                # usaremos reset_problem em display_frame para esperar
                # um segundo
                self.reset_problem = True

    def set_problem(self):
        """ faça outro problema novamente """
        if self.operation == "Adição":
            self.addition()
        elif self.operation == "Subtração":
            self.subtraction()
        elif self.operation == "Multiplicação":
            self.multiplication()
        elif self.operation == "Divisão":
            self.division()
        self.button_list = self.get_button_list()

    def process_events(self):
        for event in pygame.event.get():  # Usuário fez algo
            if event.type == pygame.QUIT:  # Se o usuário clicou perto
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_menu:
                    if self.menu.state == 0:
                        self.operation = "Adição"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 1:
                        self.operation = "Subtração"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 2:
                        self.operation = "Multiplicação"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 3:
                        self.operation = "Divisão"
                        self.set_problem()
                        self.show_menu = False
                
                # Nós vamos para check_result para verificar se o usuário
                # responder corretamente o problema
                else:
                    self.check_result()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu = True
                    # definir pontuação para 0
                    self.score = 0
                    self.count = 0

        return False

    def run_logic(self):
        # Atualização do menu
        self.menu.update()
        
    def display_message(self, screen, items):
        """ exibe cada string que está dentro de uma msg (args) """
        for index, message in enumerate(items):
            label = self.font.render(message, True, BLACK)
            # Obter a largura e a altura do marcador
            width = label.get_width()
            height = label.get_height()
            pos_x = (SCREEN_WIDTH / 2) - (width / 2)
            # t_h: altura total do bloco de texto
            t_h = len(items) * height
            pos_y = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)
            
            screen.blit(label, (pos_x, pos_y))

    def display_frame(self, screen):
        # Desenhe a imagem de fundo
        screen.blit(self.background_image, (0, 0))
        # True: liga pygame.time.wait()
        time_wait = False
        # --- Código de desenho deve ir aqui
        if self.show_menu:
            self.menu.display_frame(screen)
        elif self.count == 20:
            # se a contagem chegar a 20, significa que o jogo acabou
            # e vamos mostrar quantas respostas estavam corretas
            # e a pontuação
            msg_1 = "Você respondeu " + str(self.score / 5) + " corretamente"
            msg_2 = "Sua pontuação foi " + str(self.score)
            self.display_message(screen, (msg_1, msg_2))
            self.show_menu = True
            # redefinir pontuação e contar para 0
            self.score = 0
            self.count = 0
            # set time_wait True para esperar 3 segundos
            time_wait = True
        else:
            # Crie etiquetas para cada número
            label_1 = self.font.render(str(self.problem["num1"]), True, BLUE)
            label_2 = self.font.render(str(self.problem["num2"])+" = ?", True, BLUE)
            # t_w: largura total
            t_w = label_1.get_width() + label_2.get_width() + 64  # 64: comprimento do símbolo
            pos_x = (SCREEN_WIDTH / 2) - (t_w / 2)
            screen.blit(label_1, (pos_x, 50))
            # imprime o símbolo na tela
            screen.blit(self.symbols[self.operation], (pos_x + label_1.get_width(), 40))
            screen.blit(label_2, (pos_x + label_1.get_width() + 64, 50))
            # Vá para cada botão e desenha
            for btn in self.button_list:
                btn.draw(screen)
            # exibir a pontuação
            score_label = self.score_font.render("Pontos: "+str(self.score), True, RED)
            screen.blit(score_label, (10, 10))
            
        # --- Vá em frente e atualize a tela com o que desenhamos
        pygame.display.flip()
        # --- Isto é para o jogo esperar alguns segundos para poder mostrar
        # --- o que temos desenhado antes de mudar para outro quadro
        if self.reset_problem:
            # espera 1 segundo
            pygame.time.wait(1000)
            self.set_problem()
            # Aumentar contagem por 1
            self.count += 1
            self.reset_problem = False
        elif time_wait:
            # aguarde 3 segundos
            pygame.time.wait(3000)


class Button(object):
    def __init__(self, x, y, width, height, number):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render(str(number), True, YELLOW)
        self.number = number
        self.background_color = BLUE

    def draw(self, screen):
        """ Este método irá desenhar o botão para a tela"""
        # Preenchimento a tela com a cor de fundo
        pygame.draw.rect(screen, self.background_color, self.rect)
        # Desenhe as bordas do botão
        pygame.draw.rect(screen, RED, self.rect, 3)
        # Obtém a largura e a altura da superfície de texto
        width = self.text.get_width()
        height = self.text.get_height()
        # Calcular o pos_X e o pos_y
        pos_x = self.rect.centerx - (width / 2)
        pos_y = self.rect.centery - (height / 2)
        # Desenhe a imagem na tela
        screen.blit(self.text, (pos_x, pos_y))

    def isPressed(self):
        """ Retorna verdadeiro se o mouse estiver no botão"""
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def set_color(self, color):
        """ Definir a cor de fundo """
        self.background_color = color

    def get_number(self):
        """ Retorna o número do botão."""
        return self.number

import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
largura = 640
altura = 480

# Configurações da cobra
x_cobra = largura // 2
y_cobra = altura // 2
velocidade = 8
x_controle = velocidade
y_controle = 0

# Configurações da maçã
x_maçã = randint(40, 600)
y_maçã = randint(50, 430)

# Configurações da pontuação
fonte = pygame.font.SysFont('arial', 30, True, True)
pontos = 0

# Configurações de áudio
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('02-CD O MELHOR DA MUSICA ELETRONICA VOL.06 DJ MURILO SOUND.mp3')
pygame.mixer.music.play(-1)
barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

# Configurações da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu primeiro projeto')
relogio = pygame.time.Clock()

# Inicialização da lista da cobra
lista_cobra = []
comprimento_inicial = 5
morreu = False

# Função para aumentar o comprimento da cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

# Função para reiniciar o jogo
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, x_maçã, y_maçã, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura // 2
    y_cobra = altura // 2
    lista_cobra = []
    x_maçã = randint(40, 600)
    y_maçã = randint(50, 430)
    morreu = False

# Loop principal do jogo
while True:
    relogio.tick(20) 
    tela.fill((255, 255, 255))  

    # Exibição da pontuação
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    tela.blit(texto_formatado, (450, 30))

    # Eventos do Pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x_controle != velocidade:
                x_controle = -velocidade
                y_controle = 0
            if event.key == K_d and x_controle != -velocidade:
                x_controle = velocidade
                y_controle = 0
            if event.key == K_w and y_controle != velocidade:
                y_controle = -velocidade
                x_controle = 0
            if event.key == K_s and y_controle != -velocidade:
                y_controle = velocidade
                x_controle = 0

    # Movimento da cobra
    x_cobra += x_controle
    y_cobra += y_controle
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maçã = pygame.draw.rect(tela, (255, 0, 0), (x_maçã, y_maçã, 20, 20))

    # Colisão da cobra com a maçã
    if cobra.colliderect(maçã):
        x_maçã = randint(40, 600)
        y_maçã = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1

    # Verifica se a cobra colidiu consigo mesma
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente.'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()
        morreu = True

        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)            
            pygame.display.update()

    # Atualização da lista da cobra
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)

    fonte2 = pygame.font.SysFont('arial', 20, True, True)

    

    pygame.display.update()

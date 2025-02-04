import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Horror Mystery: Eles Não Param de Vir")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (50, 205, 50)

# Fontes
font = pygame.font.SysFont("arial", 32)
small_font = pygame.font.SysFont("arial", 24)

# Variáveis do jogo
player_hp = 20
enemy_hp = 20
game_over = False
# Mensagem inicial com o clima de mistério/terror
message = "Apenas eles... não sei quem ou o que são, mas eles não param de vir..."

clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    """Função auxiliar para desenhar texto na tela."""
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Se o jogo não acabou, processa as ações do jogador
        if not game_over:
            if event.type == pygame.KEYDOWN:
                # Pressione A para atacar
                if event.key == pygame.K_a:
                    roll = random.randint(1, 20)
                    if roll == 20:
                        message = "Crítico! Você causou um dano devastador no inimigo."
                        enemy_hp -= 10
                    elif roll >= 10:
                        message = "Acerto! O inimigo treme com o golpe."
                        enemy_hp -= 5
                    else:
                        message = "Ele revida! Um golpe inesperado te fere."
                        player_hp -= 1
                # Pressione N para não atacar (ou recuar)
                elif event.key == pygame.K_n:
                    roll = random.randint(1, 20)
                    if roll == 20:
                        message = "Ele critica! Um golpe mortal te atinge."
                        player_hp -= 10
                    elif roll >= 10:
                        message = "Ele acerta! A dor corta sua esperança."
                        player_hp -= 5
                    else:
                        message = "Silêncio... por enquanto, você se mantém seguro."
    
    # Se o inimigo for derrotado, ele "revive" com HP total
    if enemy_hp <= 0:
        message = "Um destino se sela, outro aparece."
        enemy_hp = 20

    # Se o jogador morrer, o jogo acaba
    if player_hp <= 0:
        game_over = True
        message = "Seu destino se sela, tudo se acalma..."

    # Desenha o fundo (preto para o clima sombrio)
    screen.fill(WHITE)

    # Desenha os status do jogador e do inimigo
    draw_text(f"Você: {player_hp} HP", font, GREEN, screen, 20, 20)
    draw_text(f"Inimigo: {enemy_hp} HP", font, RED, screen, 20, 60)
    
    # Instruções e mensagens de ambiente
    draw_text("Pressione [A] para atacar ou [N] para recuar.", small_font, WHITE, screen, 20, HEIGHT - 80)
    draw_text(message, small_font, WHITE, screen, 20, HEIGHT - 120)
    
    # Se o jogo acabou, mostra a mensagem de fim
    if game_over:
        draw_text("GAME OVER", font, RED, screen, WIDTH // 2 - 100, HEIGHT // 2)

    pygame.display.update()
    clock.tick(30)

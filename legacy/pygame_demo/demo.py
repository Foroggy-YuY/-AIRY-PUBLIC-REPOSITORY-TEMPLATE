# demo.py
# Демонстрация визуализации облака Айри

import pygame
import sys
from visuals.cloud import AiryCloud, RenderQuality
from visuals.hud import HUD, HUDMode
from visuals.palette import StateType

def create_gradient_background(width: int, height: int) -> pygame.Surface:
    """Создание фона с градиентом"""
    background = pygame.Surface((width, height))
    
    # Градиент от светло-серого вверху к почти белому внизу
    for y in range(height):
        # Плавный переход
        ratio = y / height
        # Верх: (210, 220, 230), низ: (240, 245, 250)
        r = int(210 + (240 - 210) * ratio)
        g = int(220 + (245 - 220) * ratio)
        b = int(230 + (250 - 230) * ratio)
        
        pygame.draw.line(background, (r, g, b), (0, y), (width, y))
    
    # Добавление мягкого свечения в центре
    center_x, center_y = width // 2, height // 2
    glow_radius = 300
    
    glow_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    
    # Рисуем несколько слоев для мягкого свечения
    for i in range(20, 0, -1):
        alpha = int((i / 20) * 15)  # Очень мягкое свечение
        radius = int(glow_radius * (i / 20))
        pygame.draw.circle(glow_surface, (255, 255, 255, alpha), 
                         (center_x, center_y), radius)
    
    background.blit(glow_surface, (0, 0))
    
    return background

def main():
    """Главная функция"""
    # Инициализация Pygame
    pygame.init()
    
    # Параметры окна
    WIDTH, HEIGHT = 1000, 700
    FPS = 60
    
    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Airy Cloud Visualization - Облако Айри')
    
    # Часы для FPS
    clock = pygame.time.Clock()
    
    # Создание фона
    background = create_gradient_background(WIDTH, HEIGHT)
    
    # Создание облака и HUD
    cloud = AiryCloud(WIDTH, HEIGHT)
    hud = HUD(WIDTH, HEIGHT)
    
    # Флаг отображения подсказок
    show_help = True
    
    # Главный цикл
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Время в секундах
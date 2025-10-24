# hud.py
# Служебный интерфейс для отображения FPS и состояния

import pygame
from typing import Tuple

class HUD:
    """Отображение служебной информации"""
    
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Инициализация шрифта
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 20)
        self.small_font = pygame.font.SysFont('Arial', 16)
        
        # Цвета
        self.text_color = (200, 200, 200)
        self.bg_color = (20, 20, 30, 180)
        
    def render(self, screen: pygame.Surface, fps: float, state_name: str, 
               show_help: bool = True):
        """Отрисовка HUD"""
        
        # FPS
        fps_text = self.font.render(f'FPS: {int(fps)}', True, self.text_color)
        fps_rect = fps_text.get_rect(topleft=(10, 10))
        
        # Подложка для FPS
        bg_surface = pygame.Surface((fps_rect.width + 20, fps_rect.height + 10), 
                                    pygame.SRCALPHA)
        bg_surface.fill(self.bg_color)
        screen.blit(bg_surface, (fps_rect.x - 10, fps_rect.y - 5))
        screen.blit(fps_text, fps_rect)
        
        # Состояние
        state_text = self.font.render(f'Состояние: {state_name}', True, self.text_color)
        state_rect = state_text.get_rect(topleft=(10, 40))
        
        bg_surface = pygame.Surface((state_rect.width + 20, state_rect.height + 10), 
                                    pygame.SRCALPHA)
        bg_surface.fill(self.bg_color)
        screen.blit(bg_surface, (state_rect.x - 10, state_rect.y - 5))
        screen.blit(state_text, state_rect)
        
        # Подсказки управления
        if show_help:
            help_lines = [
                'Управление:',
                '1 - Спокойствие',
                '2 - Слушает',
                '3 - Думает',
                '4 - Говорит',
                'H - Скрыть/показать подсказки',]
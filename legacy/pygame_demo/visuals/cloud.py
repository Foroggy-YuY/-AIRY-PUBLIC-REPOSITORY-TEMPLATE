import pygame
import numpy as np
import math
from typing import Tuple, List
from .palette import EmotionPalette, EmotionState, palette, StateType

class Particle:
    """Класс частицы облака"""
    
    def __init__(self, x: float, y: float, base_radius: float):
        self.x = x
        self.y = y
        self.base_x = x  # начальная позиция для дрейфа
        self.base_y = y
        self.base_radius = base_radius
        self.radius = base_radius
        self.phase = np.random.random() * 2 * math.pi  # фаза для анимации
        self.drift_phase_x = np.random.random() * 2 * math.pi
        self.drift_phase_y = np.random.random() * 2 * math.pi
        
    def update(self, time: float, breath_speed: float, breath_amplitude: float,
               drift_speed: float, scale: float):
        """Обновление состояния частицы"""
        # Дыхание - изменение размера
        breath = 1.0 + math.sin(time * breath_speed + self.phase) * breath_amplitude
        self.radius = self.base_radius * breath * scale
        
        # Дрейф - плавное движение
        drift_x = math.sin(time * drift_speed * 0.5 + self.drift_phase_x) * 2
        drift_y = math.cos(time * drift_speed * 0.3 + self.drift_phase_y) * 2
        
        self.x = self.base_x + drift_x
        self.y = self.base_y + drift_y


class AiryCloud:
    """Облако Айри - визуализация с системой частиц"""
    
    def __init__(self, width: int = 1000, height: int = 700):
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        
        # Текущее и целевое состояние
        self.current_state = 'calm'
        self.target_state = 'calm'
        self.transition_progress = 1.0  # 0-1, 1 = завершен переход
        self.transition_speed = 0.02  # скорость перехода
        
        # Параметры облака
        self.cloud_radius = 150  # базовый радиус облака
        self.num_particles = 120  # количество частиц
        
        #

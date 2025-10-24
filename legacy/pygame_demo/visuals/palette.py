# palette.py
# Палитры эмоциональных состояний облака Айри

from typing import Dict, Tuple
import math

class EmotionPalette:
    """Палитра состояний для облака Айри"""

    # Определение состояний и их параметров
    STATES = {
        'calm': {
            'name': 'Спокойствие',
            'base_color': (180, 200, 220),  # светло-голубой
            'glow_color': (220, 230, 240),  # бело-голубой
            'breath_speed': 0.5,  # медленное дыхание
            'breath_amplitude': 0.08,  # ±8% масштаба
            'drift_speed': 0.3,  # минимальный дрейф
            'particle_density': 1.0,  # базовая плотность
            'glow_intensity': 0.3,  # мягкое свечение
        },
        'listening': {
            'name': 'Слушает',
            'base_color': (190, 210, 235),  # голубовато-белый
            'glow_color': (230, 240, 250),  # яркий белый
            'breath_speed': 0.8,  # чуть активнее
            'breath_amplitude': 0.12,  # ±12% масштаба
            'drift_speed': 0.5,  # легкое дрожание
            'particle_density': 1.1,  
            'glow_intensity': 0.4,
        },
        'thinking': {
            'name': 'Думает',
            'base_color': (160, 180, 220),  # фиолетово-голубой
            'glow_color': (200, 210, 240),  # холодное свечение
            'breath_speed': 0.4,  # замедленное дыхание
            'breath_amplitude': 0.15,  # ±15% масштаба
            'drift_speed': 0.4,  # медленный дрейф
            'particle_density': 1.2,
            'glow_intensity': 0.5,  # заметное свечение
        },
        'speaking': {
            'name': 'Говорит',
            'base_color': (230, 220, 200),  # тёплое бело-оранжевое
            'glow_color': (250, 240, 220),  # теплое свечение
            'breath_speed': 1.2,  # активное дыхание
            'breath_amplitude': 0.18,  # ±18% масштаба
            'drift_speed': 0.8,  # активные волны
            'particle_density': 1.3,
            'glow_intensity': 0.6,  # яркое свечение
        }
    }
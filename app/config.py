"""
Конфигурация приложения Airy
"""

# Настройки окна
WINDOW_CONFIG = {
    'width': 420,
    'height': 420,
    'resizable': False,
    'frameless': False,      # True для плавающего окна без рамки
    'easy_drag': True,       # Перетаскивание окна
    'transparent': False,    # Прозрачный фон (experimental)
    'on_top': False,        # Поверх всех окон
    'confirm_close': False,
    'background_color': '#FFFFFF',
    'text_select': False,
    'min_size': (300, 300),
}

# Состояния ассистента
STATES = {
    'IDLE': 'idle',
    'LISTENING': 'listening',
    'THINKING': 'thinking',
    'SPEAKING': 'speaking'
}

# Пути
PATHS = {
    'ui': 'ui/',
    'plugins': 'plugins/',
    'assets': 'ui/assets/'
}

# Версия
VERSION = '0.1.0'
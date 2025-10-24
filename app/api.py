from app.config import STATES, VERSION


class AiryAPI:
    """
    Публичный API для взаимодействия JavaScript ↔ Python
    """
    
    def __init__(self):
        self.state = STATES['IDLE']
        self.core_connected = False
        self.window = None
    
    # === Базовые методы ===
    
    def ping(self):
        """
        Проверка связи с API
        
        Returns:
            dict: Статус соединения
        """
        return {
            'ok': True,
            'core': self.core_connected,
            'version': VERSION
        }
    
    def get_state(self):
        """
        Получить текущее состояние
        
        Returns:
            dict: Текущее состояние
        """
        return {'state': self.state}
    
    def set_state(self, state: str):
        """
        Установить состояние визуала
        
        Args:
            state: Одно из состояний: idle, listening, thinking, speaking
            
        Returns:
            dict: Результат операции
        """
        if state in STATES.values():
            self.state = state
            return {
                'state': self.state,
                'changed': True,
                'timestamp': self._get_timestamp()
            }
        return {
            'error': 'Invalid state',
            'valid_states': list(STATES.values())
        }
    
    def get_config(self):
        """
        Получить конфигурацию приложения
        
        Returns:
            dict: Конфигурация
        """
        return {
            'version': VERSION,
            'theme': 'default',
            'language': 'ru',
            'core_connected': self.core_connected
        }
    
    # === Методы для будущего Core (загл) ===
    
    def send_command(self, text: str):
        """
        Отправить текстовую команду в Core
        
        Args:
            text: Текст команды
            
        Returns:
            dict: Ответ от Core (заглушка)
        """
        if not self.core_connected:
            return {
                'received': text,
                'response': None,
                'error': 'Core not connected'
            }
        
        # Здесь будет вызов реального Core
        return {
            'received': text,
            'response': f'Echo: {text}',
            'mock': True
        }
    
    def start_listening(self):
        """
        Начать прослушивание голоса
        
        Returns:
            dict: Результат
        """
        self.set_state(STATES['LISTENING'])
        return {'listening': True}
    
    def stop_listening(self):
        """
        Остановить прослушивание
        
        Returns:
            dict: Результат
        """
        self.set_state(STATES['IDLE'])
        return {'listening': False}
    
    # === Вспомогательные методы ===
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()
    
    def log(self, message: str, level: str = 'info'):
        """
        Логирование из JavaScript
        
        Args:
            message: Сообщение для лога
            level: Уровень (info, warning, error)
        """
        print(f'[{level.upper()}] {message}')
        return {'logged': True}
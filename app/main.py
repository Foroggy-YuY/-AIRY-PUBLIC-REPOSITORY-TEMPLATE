"""
Airy Public Edition - Main Entry Point
Визуальная оболочка офлайн-ассистента
"""

import webview
import sys
import os

# Получаем абсолютный путь к корню проекта
if getattr(sys, 'frozen', False):
    # Если запущено из .exe
    application_path = os.path.dirname(sys.executable)
else:
    # Если запущено из исходников
    application_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Добавляем в sys.path
if application_path not in sys.path:
    sys.path.insert(0, application_path)

from app.api import AiryAPI
from app.config import WINDOW_CONFIG


def main():
    """Запуск приложения"""
    
    # Создание экземпляра API
    api = AiryAPI()
    
    # Получаем полный путь к index.html
    ui_path = os.path.join(application_path, 'ui', 'index.html')
    
    # Проверяем существование файла
    if not os.path.exists(ui_path):
        print(f"ERROR: UI file not found at: {ui_path}")
        print(f"Current directory: {os.getcwd()}")
        print(f"Application path: {application_path}")
        return
    
    print(f"Loading UI from: {ui_path}")
    
    # Создание окна приложения
    window = webview.create_window(
        title='Airy',
        url=ui_path,
        js_api=api,
        **WINDOW_CONFIG
    )
    
    # Сохранение ссылки на окно в API
    api.window = window
    
    # Запуск GUI цикла
    webview.start(debug=False)


if __name__ == '__main__':
    main()

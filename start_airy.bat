# Создайте файл start_airy.bat в корне проекта
@"
@echo off
title Airy - Запуск...

echo ========================================
echo    AIRY - Offline Voice Assistant
echo ========================================
echo.

REM Получаем путь к папке скрипта
set SCRIPT_DIR=%~dp0

REM Переходим в папку проекта
cd /d "%SCRIPT_DIR%"

echo [1/3] Проверка виртуального окружения...

REM Проверяем существование venv
if not exist "%SCRIPT_DIR%venv\" (
    echo [!] Виртуальное окружение не найдено!
    echo [*] Создаём виртуальное окружение...
    python -m venv venv
    
    echo [*] Устанавливаем зависимости...
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    call venv\Scripts\deactivate.bat
)

echo [2/3] Активация виртуального окружения...
call venv\Scripts\activate.bat

echo [3/3] Запуск Airy UI...
echo.
python app\main.py

REM При закрытии приложения деактивируем окружение
call venv\Scripts\deactivate.bat

echo.
echo Airy остановлен. Нажмите любую клавишу для выхода...
pause >nul
"@ | Out-File -FilePath "start_airy.bat" -Encoding ASCII

Write-Host "✅ Создан файл start_airy.bat" -ForegroundColor Green

@"
# 🌥️ Инструкция по установке и запуску Airy

## Системные требования

- **Операционная система**: Windows 10/11
- **Python**: версия 3.10 или выше
- **Свободное место**: ~100 МБ
- **Интернет**: только для первой установки

---

## 📥 Установка

### Шаг 1: Установите Python (если ещё не установлен)

1. Скачайте Python с официального сайта: https://www.python.org/downloads/
2. Запустите установщик
3. ✅ **ВАЖНО**: Поставьте галочку "Add Python to PATH"
4. Нажмите "Install Now"

### Шаг 2: Скачайте проект

**Вариант A: Через Git**
git clone https://github.com/Foroggy-YuY/AIRY-PUBLIC.git
cd AIRY-PUBLIC

text

**Вариант B: Через ZIP**
1. Откройте: https://github.com/Foroggy-YuY/AIRY-PUBLIC
2. Нажмите зелёную кнопку **Code** → **Download ZIP**
3. Распакуйте архив в любую папку

---

## 🚀 Запуск

### Способ 1: Двойной клик (самый простой)

1. Откройте папку **AIRY-PUBLIC**
2. Найдите файл **start_airy.bat**
3. **Дважды кликните** по нему

При первом запуске:
- Автоматически создастся виртуальное окружение
- Установятся все необходимые библиотеки
- Откроется окно Airy

При следующих запусках просто кликайте по **start_airy.bat**!

### Способ 2: Ярлык на рабочем столе

1. В папке проекта найдите файл **create_desktop_shortcut.ps1**
2. Кликните по нему **правой кнопкой мыши**
3. Выберите **"Выполнить с помощью PowerShell"**
4. На рабочем столе появится ярлык **"Запустить Airy"**
5. Теперь запускайте Airy двойным кликом по ярлыку!

### Способ 3: Через командную строку

Откройте PowerShell в папке проекта и выполните:
.\start_airy.bat

text

---

## 🎮 Управление

После запуска откроется окно с анимированным облаком.

### Клавиатура:

- **ПРОБЕЛ** — переключить idle ↔ listening
- **1** — состояние idle (покой)
- **2** — состояние listening (слушает)
- **3** — состояние thinking (думает)
- **4** — состояние speaking (говорит)
- **→ ←** — переключение между состояниями

### Мышь:

- **Клик по облаку** — переключить idle ↔ listening

---

## ❓ Решение проблем

### Проблема: "python не распознан"

**Решение**:
1. Переустановите Python с галочкой "Add Python to PATH"
2. Или используйте команду `py` вместо `python`:
   - Откройте **start_airy.bat** блокнотом
   - Замените `python` на `py`

### Проблема: Окно открывается и сразу закрывается

**Решение**:
1. Откройте PowerShell в папке проекта
2. Выполните вручную:
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py

text
3. Посмотрите, какая ошибка появится

### Проблема: "execution policy"

**Решение**:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

text

---

## 📁 Структура проекта

AIRY-PUBLIC/
├── start_airy.bat ← ЗАПУСКАТЬ ЭТОТ ФАЙЛ
├── run.py ← Основной скрипт запуска
├── app/ ← Python код
├── ui/ ← Интерфейс (HTML/CSS/JS)
├── venv/ ← Виртуальное окружение (создаётся автоматически)
└── requirements.txt ← Список зависимостей

text

---

## 💡 Советы

- **Первый запуск** занимает ~1-2 минуты (установка библиотек)
- **Последующие запуски** — мгновенные
- Не удаляйте папку **venv/** после первого запуска
- Можно переместить проект в другую папку — всё будет работать

---

## 🆘 Поддержка

Если что-то не работает:

1. Проверьте, что Python установлен: откройте cmd и введите `python --version`
2. Прочитайте раздел "Решение проблем" выше
3. Создайте Issue на GitHub: https://github.com/Foroggy-YuY/AIRY-PUBLIC/issues

---

## ✨ Готово!

Теперь запускайте Airy двойным кликом по **start_airy.bat**!

Приятного использования! 🌥️
"@ | Out-File -FilePath "INSTALL_RU.md" -Encoding UTF8

Write-Host "✅ Создан файл INSTALL_RU.md" -ForegroundColor Green
```

***

## 🎯 Финальная команда для создания всех файлов

Скопируйте и выполните в PowerShell:

```powershell
# Создание start_airy.bat
@"
@echo off
title Airy - Запуск...
echo ========================================
echo    AIRY - Offline Voice Assistant
echo ========================================
echo.
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
echo [1/3] Проверка виртуального окружения...
if not exist "%SCRIPT_DIR%venv\" (
    echo [*] Создаём виртуальное окружение...
    python -m venv venv
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)
echo [2/3] Активация окружения...
echo [3/3] Запуск Airy UI...
echo.
python run.py
call venv\Scripts\deactivate.bat
echo.
echo Airy остановлен.
pause
"@ | Out-File -FilePath "start_airy.bat" -Encoding ASCII

Write-Host "✅ Все файлы созданы!" -ForegroundColor Green
Write-Host ""
Write-Host "Теперь просто дважды кликните по start_airy.bat для запуска!" -ForegroundColor Cyan
```

***

## ✅ Что получилось

После выполнения команд у вас появятся:

1. **start_airy.bat** — главный файл для запуска (двойной клик)
2. **INSTALL_RU.md** — инструкция на русском для пользователей
3. **create_desktop_shortcut.ps1** — для создания ярлыка на рабочем столе

Теперь просто **дважды кликайте по start_airy.bat** — и Airy запустится автоматически!  🚀[2][3][4][1]
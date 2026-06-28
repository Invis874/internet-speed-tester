# 🌐 Internet Speed Tester

Простой скрипт для замера скорости интернета путем скачивания файла по указанному URL.

## 📋 Требования

- Python 3.6+
- Библиотека requests

## 🚀 Установка

```bash
# Клонируем репозиторий
git clone https://github.com/Invis874/internet-speed-tester.git
cd internet-speed-tester

# Виртуальное окружение
python -m venv venv

.\venv\Scripts\Activate.ps1 # Для Windows (PowerShell)
venv\Scripts\activate       # Windows (cmd)
source venv/bin/activate    # macOS / Linux

# Устанавливаем зависимости
pip install -r requirements.txt
```

## 💻 Использование

```bash
python speed_test.py <URL> [количество_запросов]
```

### Примеры:

```bash
# Тест с 10 запросами (по умолчанию)
python speed_test.py https://avatars.mds.yandex.net/get-yapic/0/0-0/islands-retina-middle

# Тест с 5 запросами
python speed_test.py https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png 5
```

## 📊 Что выводится

- Для каждого запроса: время, размер, скорость
- Итоговые результаты: общий объем, среднее время, средняя скорость

## 🧪 Где взять файлы для теста
### Картинки для теста:
- https://fonwall.ru/wallpaper/wallpaper-battlefield-1-world-war-1-aviation/1366x768/

- https://fonwall.ru/wallpaper/nature-winter-squirrel-branch/1366x768/
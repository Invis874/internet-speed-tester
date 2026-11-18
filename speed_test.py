import time
import requests
import sys


def measure_speed(url: str, requests_count: int = 10):
    """
    Замеряет скорость интернета, скачивая файл по указанному URL
    """
    times = []
    total_bytes = 0
    
    # Добавляем заголовки как у браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    print(f"🔄 Начинаю тестирование скорости...")
    print(f"📍 URL: {url}")
    print(f"📊 Количество запросов: {requests_count}")
    print("-" * 50)
    
    for i in range(requests_count):
        try:
            start_time = time.time()
            
            # Добавляем заголовки и таймаут
            response = requests.get(url, headers=headers, stream=True, timeout=30)
            response.raise_for_status()
            
            content_length = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    content_length += len(chunk)
            
            end_time = time.time()
            elapsed = end_time - start_time
            times.append(elapsed)
            total_bytes += content_length
            
            speed_mbps = (content_length * 8) / (elapsed * 1024 * 1024)
            
            print(f"  ✅ Запрос {i+1}/{requests_count}: "
                  f"⏱ {elapsed:.2f}с, "
                  f"📦 {content_length / (1024*1024):.2f} МБ, "
                  f"🚀 {speed_mbps:.2f} Мбит/с")
            
        except requests.exceptions.RequestException as e:
            print(f"  ❌ Ошибка запроса {i+1}: {e}")
            continue
        except Exception as e:
            print(f"  ❌ Неожиданная ошибка: {e}")
            continue
    
    if not times:
        raise RuntimeError("❌ Все запросы завершились ошибкой")
    
    avg_time = sum(times) / len(times)
    total_mb = total_bytes / (1024 * 1024)
    avg_speed_mbps = (total_bytes * 8) / (sum(times) * 1024 * 1024)
    
    return avg_speed_mbps, avg_time, total_mb


def main():
    if len(sys.argv) < 2:
        print("❌ Использование: python speed_test.py <URL> [количество_запросов]")
        print("📌 Примеры:")
        print("  python speed_test.py https://speedtest.tele2.net/10MB.zip 10")
        print("  python speed_test.py https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.6.tar.gz 5")
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        requests_count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    except ValueError:
        print(f"❌ Количество запросов должно быть целым числом, получено: {sys.argv[2]!r}")
        sys.exit(1)

    if requests_count < 1:
        print("❌ Количество запросов должно быть >= 1")
        sys.exit(1)
    
    try:
        avg_speed, avg_time, total_mb = measure_speed(url, requests_count)
        
        print("-" * 50)
        print("📊 РЕЗУЛЬТАТЫ:")
        print(f"  📦 Общий объем скачанных данных: {total_mb:.2f} МБ")
        print(f"  ⏱ Среднее время запроса: {avg_time:.2f} сек")
        print(f"  🚀 Средняя скорость: {avg_speed:.2f} Мбит/с")
        print(f"  🚀 Средняя скорость: {avg_speed / 8:.2f} МБ/с")
        
    except KeyboardInterrupt:
        print("\n⏹ Тест прерван пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
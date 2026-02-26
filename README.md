# Rent Car API

Современное REST API для онлайн-бронирования автомобилей. Проект реализован на Django REST Framework с использованием PostgreSQL, Docker и Nginx.

## Особенности

- **Гибкое ценообразование** - тарифные планы с учетом сезонов, скидок и дополнительных услуг
- **Интеллектуальное бронирование** - автоматическая валидация доступности и пересечения дат
- **Оптимизированная производительность** - использование select_related и prefetch_related для минимизации SQL-запросов
- **Профессиональная админка** - кастомный интерфейс на Jazzmin с иконками и удобной навигацией
- **Полная документация** - Swagger/OpenAPI для всех endpoint'ов

## Технологический стек

- **Backend**: Python 3.11, Django 4.2, Django REST Framework
- **База данных**: PostgreSQL
- **Контейнеризация**: Docker, Docker Compose
- **Веб-сервер**: Nginx
- **Админка**: Jazzmin
- **Документация**: drf-yasg (Swagger)

## Архитектура

### Модули

- **Car** - управление автопарком, бронирование, изображения автомобилей
- **Location** - локации проката, характеристики, галерея
- **Price** - тарифные планы, сезоны, дополнительные услуги
- **Main** - баннеры, отзывы клиентов

### API Endpoints

- `/cars/` - список и детали автомобилей с фильтрацией
- `/locations/` - локации и их характеристики
- `/price/` - тарифные планы и сезоны
- `/main/` - баннеры и отзывы
- `/swagger/` - интерактивная документация API

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Nurbol47/rent_car.git
   cd rent_car
   ```

2. Настройте переменные окружения:
   ```bash
   cp backend_api/.env.example backend_api/.env
   # Заполните .env файл своими значениями
   ```

3. Запустите с помощью Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Выполните миграции:
   ```bash
   docker-compose exec backend python manage.py migrate
   ```

5. Создайте суперпользователя:
   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

## Использование

- **API**: `http://localhost:8000/`
- **Админка**: `http://localhost:8000/admin/`
- **Документация**: `http://localhost:8000/swagger/`

## Лицензия

MIT License
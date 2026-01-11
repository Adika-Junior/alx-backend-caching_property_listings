# Django Property Listings with Redis Caching

A Django-based property listing application with Redis caching at multiple levels, demonstrating various caching strategies including view-level caching, low-level queryset caching, and proper cache invalidation techniques.

## Features

- **Multi-level Caching**: View-level caching with `@cache_page` decorator and low-level queryset caching
- **Cache Invalidation**: Automatic cache invalidation using Django signals
- **Cache Metrics**: Redis cache hit/miss metrics analysis
- **Dockerized Services**: PostgreSQL and Redis running in Docker containers

## Project Structure

```
alx-backend-caching_property_listings/
├── alx_backend_caching_property_listings/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── properties/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│   ├── signals.py
│   └── admin.py
├── docker-compose.yml
├── manage.py
└── requirements.txt
```

## Setup Instructions

### 1. Install Dependencies

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python packages
pip install -r requirements.txt
```

### 2. Start Docker Services

```bash
# Start PostgreSQL and Redis containers
docker-compose up -d

# Verify containers are running
docker-compose ps
```

### 3. Run Migrations

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 4. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## API Endpoints

- **GET /properties/**: List all properties (cached for 15 minutes at view level)

## Caching Implementation

### 1. View-Level Caching
- Uses `@cache_page(60 * 15)` decorator to cache entire view response for 15 minutes
- Implemented in `properties/views.py`

### 2. Low-Level Caching
- Caches Property queryset in Redis for 1 hour (3600 seconds)
- Implemented in `properties/utils.py` with `get_all_properties()` function

### 3. Cache Invalidation
- Automatically invalidates cache on Property create/update/delete
- Implemented using Django signals in `properties/signals.py`

### 4. Cache Metrics
- Retrieves Redis cache statistics (hits, misses, hit ratio)
- Implemented in `properties/utils.py` with `get_redis_cache_metrics()` function

## Docker Services

- **PostgreSQL**: Database service on port 5432
- **Redis**: Cache service on port 6379

## Environment Variables

The application uses the following environment variables (with defaults):

- `POSTGRES_DB`: Database name (default: `property_db`)
- `POSTGRES_USER`: Database user (default: `property_user`)
- `POSTGRES_PASSWORD`: Database password (default: `property_pass`)
- `POSTGRES_HOST`: Database host (default: `postgres`)
- `POSTGRES_PORT`: Database port (default: `5432`)
- `REDIS_URL`: Redis connection URL (default: `redis://redis:6379/1`)

## Testing Cache Functionality

1. Access `/properties/` endpoint multiple times - first request hits database, subsequent requests use cache
2. Create/update/delete a property via admin panel - cache will be invalidated
3. Check logs for cache hit/miss messages
4. Use `get_redis_cache_metrics()` function to analyze cache performance

## Notes

- For local development without Docker, update `settings.py` to use `localhost` instead of `postgres` and `redis` for HOST values
- Cache keys are prefixed automatically by django-redis
- View-level cache respects HTTP methods and user authentication by default

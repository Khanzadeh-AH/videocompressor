### prerequisites:
    - Redis must be running
    - postgreSQL must be running

### Run:
    python3 manage.py runserver && celery -A compressor worker -l INFO

### Run with docker:
    Docker run -d -p 8080:8080 -e DB_NAME=<db-name> -e DB_USER=<db-user> -e DB_PASSWORD=<db-pw> -e DB_HOST=<db-host> -e DB_PORT=<db-port> -e REDIS_HOST=<redis-host> -e REDIS_PORT=<redis-port> <built image>
    
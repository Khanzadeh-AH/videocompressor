### prerequisites:
    - Redis must be available on 127.0.0.1:6379

### Run:
    python3 manage.py runserver && celery -A compressor worker -l INFO

### Run with docker:
    Docker run -d -p 8080:8080 <built image>
    
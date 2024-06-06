### NFX Seller Backend Documentation

#### Getting Started

Project Setup [Installation Steps]

Install virtual environment

```

pip install virtualenv

```

create and activate the virtual env

```

python3 -m venv "venv_name"

source venv/bin/activate

```

Install requirements 

```
pip install -r requirements.txt
```

Migrate 

```

python manage.py migrate

```

Run Server

```

python manage.py runserver

```

Celery Setup Steps

```
Asynchronous tasks using CELERY and REDIS as a broker

1. Module used
    a. django-celery-results: to store celery tasks result
    b. django-celery-beat: to schedule periodic task

2. Run Redis
    A.Install Redis on Linux/Mac
        a. sudo apt-get update
        b. sudo apt-get install redis-server
        c. Reference: https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04
    
    B. Install Redis On Windows
        a. Download Redis-x64-3.2.100 and Run redis-server.exe

3. Run Celery
    A. open a new terminal and run celery
        Linux:
            1. celery -A nfx_seller worker --beat -S django -l info
        Windows:
            1. celery -A nfx_seller worker -l info --pool=solo
            2. celery -A nfx_seller beat -l info -S django
            Run these comands In different terminals (Windows)

4. TESTING
    API URL: {{ _.url }}/celery  GET REQUEST
    
    this will return a response
    
    {
      "success": true,
      "code": 200,
      "data": {
        "message": "Success"
      }
    }
    and then check Task model in admin panel, there is a entry
```

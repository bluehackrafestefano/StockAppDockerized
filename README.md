# StockApp - Yet Another Dockerized Django REST Project

This is a Django REST Framework project. I created it for experimentation and learning purposes. Then, I dockerized it to continue with CI and DevOps tools in the near future.


## Motivation

Keeping the transactions up-to-date of a commercial app is a common challenge. A complete project template may be beneficial for future use cases.


## Method and results

Using Django for the backend is one of the best solution for apps. Django has concise base classes. We can do things with little code.

In this project:
  - TokenAuthentication for authentication,
  - dj_rest_auth for login/logout and token creation,
  - swagger for testing and visualization of the project,
  - logger (file and console) for loggging,
  - redoc for documentation,
  - django_filters for filtering,
  - search,
  - nested serializers to show products under one brand etc.,
  - signals for token creation and updating different models at the same time,
  - DjangoModelPermissions to define granular permissions to different groups,
  - Viewset for logic,
  - DefaultRouter for url mapping,
are used.

And as best practices:
  - python-decouple is used to seperate sensitive data,
  - dev and prod environments are seperated,
  - project URLconf simply includes URLconfs from the applications,
  - abstract base class is used on models in order to implement DRY principle,
  - virtual environment is used while developing this project locally,
  - an updated requirements.txt file is used for collaborating properly with other developers,
  - plural related names are used to specify the reverse relation from the parent model back to the child model.


## Repository overview

The tree of this project is like:

```
StockAppDockerized
├─ .dockerignore
├─ .gitignore
├─ docker-compose.yml
├─ Dockerfile
├─ main
│  ├─ asgi.py
│  ├─ settings
│  │  ├─ base.py
│  │  ├─ dev.py
│  │  ├─ prod.py
│  │  └─ __init__.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
├─ README.md
├─ requirements.txt
├─ stock
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ signals.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
└─ users
   ├─ admin.py
   ├─ apps.py
   ├─ migrations
   │  └─ __init__.py
   ├─ models.py
   ├─ serializers.py
   ├─ signals.py
   ├─ tests.py
   ├─ urls.py
   ├─ views.py
   └─ __init__.py
```

## Running instructions

Project requirements to run:
  - Python 3
  - pip
  - virtual environment
  - .env file
  - git
  - Docker (up and running)

Steps to spin up this project:

1. Clone this repository:
```git
git clone https://github.com/bluehackrafestefano/StockAppDockerized.git
```

2. Open StockAppDockerized folder with your IDE.

3. (Optional for local development) Create virtual environment as a best practice:
```py
python3 -m venv env # for Windows or
python -m venv env # for Windows
virtualenv env # for Mac/Linux or;
virtualenv env -p python3 # for Mac/Linux
```

4. (Optional for local development) Activate virtual environment:
```bash
.\env\Scripts\activate  # for Windows
source env/bin/activate  # for MAC/Linux
```

5. (Optional for local development) Install dependencies:
```bash
pip install -r requirements.txt
```

6. Create `.env` file with variables:
```
SECRET_KEY=somedjangosecretkeyfromsecretkeygenerators
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
ENV_NAME=PROD
DJANGO_LOG_LEVEL=INFO
```

7. Build the project:
```docker
docker-compose up
```

8. Apply the db tables by migrating models to postgres inside the container:
```docker
docker-compose exec web python manage.py migrate
```

9. Test the endpoint `http://localhost:8000/stock/`.

10. Usually the db is not ready immediately. And this cause problems to reach the app. Solution:
  - Restart the web or;
  - press Ctrl+C and stop db and web, then restart with `docker-compose up` command.

## Next Steps

To improve this project;

  - Add a frontend React project to serve web app,
  - Add an Nginx server to the stack,
  - Create a Jenkins pipeline to add CI capability,
  - Define AWS resources with Terraform,
  - Configure servers with Ansible,
  - Add K8s to orchestrate the stack,
  - Add monitoring tools to see app health.


## About

This project is initially created for Clarusway students to teach Docker implementation to Backend projects.
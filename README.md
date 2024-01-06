# test-task-forager-ai

This is a test task for Junior Python Developer position

## Tech stack

1. `Python 3.11>`
2. `Django`
3. `Django REST Framework`
4. `Poetry`
5. `Docker`
6. `PostgreSQL`
7. `djoser`
8. `isort`
9. `black`
10. `wemake-python-styleguide linter`

## Description

This is a music service client API. You can create, serve and update `music albums`, `songs`, `artists` and `music labels`.
Authentication was implemented using `djoser` package with `email verification`, `password reset`, etc.

### Endpoints

1. `admin/` - `Django Admin` panel
2. `api/v1/` - Health check, Allowed methods - `GET`.
3. `api/v1/songs/` - `Song` model CRUD, Allowed methods - `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
4. `api/v1/albums/` - `Album` model CRUD, Allowed methods - `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
5. `api/v1/authors/` - `Author` model CRUD, Allowed methods - `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
6. `api/v1/music-labels/` - `MusicLabel` model CRUD, Allowed methods - `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
7. `api/v1/storage/` - API route for service that takes some value and stores it in local variable, Allowed methods - `GET`, `POST`.
8. `api/v1/users/` - `User` model CRUD, Allowed methods - `GET`, `PUT`, `PATCH`. Deleting account is implemented using `djoser` package.
9. `api/v1/users/unverified-users/` - Get users that are not verified(email is not activated), Allowed methods - `GET`
10. `api/v1/auth/` - Auth route implemented by `djoser` package. Project uses `JWT` authentication. For more details about this route check [`djoser documentation`](https://djoser.readthedocs.io/en/latest/getting_started.html)

## Run the project

> [!WARNING]  
> Create `.env` file and set all necessary variables(check `.env.example` file)

### Using `Docker`

1. Build docker image from `Dockerfile`:

   ```bash
   docker build -t test-task-forager-ai .
   ```

2. Run `docker-compose.yml`:

   ```bash
   docker-compose up --build
   ```

3. Go to the `http://localhost:8000` in the browser

### Using `Poetry`

1. Install all dependencies:

   ```bash
   poetry install
   ```

2. Activate virtual environment:

   ```bash
   poetry shell
   ```

3. Run `Django` server:

   ```bash
   python manage.py runserver
   ```

4. Go to the `http://127.0.0.1:8000` in the browser

### Using `pip`

> [!WARNING]  
> It's recommended to use `Poetry` as the packet manager. It's easier to run projects and manage their dependencies

1. Create virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate it:

   > Windows

   ```bash
   venv\Scripts\activate
   ```

   > Linux and MacOS

   ```bash
   source venv/bin/activate
   ```

3. Install all dependencies:

   ```bash
   pip install -f requirements.txt
   ```

4. Run Django server:

   ```bash
   python manage.py runserver
   ```

5. Go to the `http://127.0.0.1:8000` in the browser

## Linting

To check linting run `flake8`:

```bash
flake8 .
```

To format code run `black`:

```bash
black --skip-string-normalization .
```

To sort imports run `isort`:

```bash
isort .
```

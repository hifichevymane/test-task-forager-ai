# test-task-forager-ai

This is a test task for Junior Python Developer position

## Setup the project

> [!WARNING]  
> Set all necessary variables in `.env` (check `.env.example` file)

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

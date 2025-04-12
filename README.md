# Healthcare Backend API

Hey there! This is a RESTful API I built for a healthcare system to manage patients, doctors, and their assignments. It uses Django and JWT authentication to keep things secure and organized. I’m really proud of how it turned out, and I hope you find it easy to set up and explore!

## Installation and Setup

Here’s how to get it running on your machine. I’ve kept it simple—just follow these steps! I’ve also kept all the sensitive data in a `.env` file, so tweak it as needed to match your setup.

### 1. Set Up a Virtual Environment

I recommend a virtual environment to keep dependencies clean:

```bash
python -m venv venv
```

Activate it:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### 2. Install Dependencies

Install everything from `requirements.txt`:

```bash
pip install -r requirements.txt
```

If it doesn't work, just run the following command and you will be all good.

```bash
pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt
```

### 3. Set Up PostgreSQL

You’ll need a PostgreSQL database running:

- Create one:
  ```bash
  createdb healthcare_db
  ```
- Check `settings.py` and the `.env` file for DB config (defaults to `localhost`, user `postgres`, no password). Update the `.env` file with your own database details if necessary.

### 4. Run Migrations

Set up the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

For admin access:

```bash
python manage.py createsuperuser
```

### 6. Start the Server

Launch the API:

```bash
python manage.py runserver
```

It’ll be live at `http://127.0.0.1:8000/`. Test it with Postman or your browser!

## Thank you.

# ECOM

A basic Django e-commerce website.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RAR2025/ECOM.git
   cd ECOM
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. Navigate to the project directory:
   ```bash
   cd ec
   ```

2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and visit: http://127.0.0.1:8000/

## Local Admin Account

The local development superuser uses:

- Username: `testUser`
- Email: `test@gmail.com`

Set or reset the password locally with:

```bash
python manage.py shell -c "from django.contrib.auth import get_user_model; u=get_user_model().objects.get(username='testUser'); u.set_password('your-local-password'); u.save()"
```

Do not commit passwords or other credentials to the repository.
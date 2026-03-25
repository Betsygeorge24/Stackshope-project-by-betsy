# StackShop - Django E-commerce Platform

## Setup Instructions

### 1. Environment Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your actual configuration values:
   - `SECRET_KEY`: Generate a new secret key for production
   - `DEBUG`: Set to `False` for production
   - `ALLOWED_HOSTS`: Add your domain names for production
   - `RAZORPAY_KEY_ID` & `RAZORPAY_KEY_SECRET`: Your Razorpay credentials
   - `EMAIL_HOST_USER` & `EMAIL_HOST_PASSWORD`: Your email credentials

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Enable/disable debug mode | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `""` |
| `RAZORPAY_KEY_ID` | Razorpay API key ID | Required |
| `RAZORPAY_KEY_SECRET` | Razorpay API key secret | Required |
| `EMAIL_HOST_USER` | SMTP email username | Required |
| `EMAIL_HOST_PASSWORD` | SMTP email password | Required |
| `PAGINATE_BY` | Items per page | `12` |

## Security Notes

- Never commit the `.env` file to version control
- Use strong, unique passwords for all services
- Generate a new `SECRET_KEY` for production
- Set `DEBUG=False` in production
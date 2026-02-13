import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'wave_cafe.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'wavecafe2024')

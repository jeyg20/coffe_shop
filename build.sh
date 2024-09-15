set -o errexit

pip install -r backend/requirements.txt

cd backend/coffee_shop

python manage.py collectstatic --no-input

python manage.py migrate

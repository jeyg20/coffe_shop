set -o errexit

pip install -r backend/requirements.txt

python manage.py backend/coffee_shop/collectstatic --no-input

python manage.py backend/coffee_shop/migrate

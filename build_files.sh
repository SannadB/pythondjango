echo "Build Start"
python -m pip install django
python manage.py collectstatic --noinput --clear
echo "Build End"
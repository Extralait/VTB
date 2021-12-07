# VTB_k0b1x

### Project run
```
docker build -t web-image Back
docker-compose up -d
```
### Project update
```
docker-compose up -d --build
```
### Collect static
```
docker-compose exec web python manage.py collectstatic
```

### Create admin
```
docker-compose exec web python manage.py createsuperuser
```



# Склады и товары


## Для запуска проекта необходимо:


Скачать проект:

```bash
$ docker pull crud
```

Добавить переменные окружения:

```bash
$ export ALLOWED_HOSTS=localhost
```

Собрать образ:
```bash
$ docker build -t my-image .
```

Запустить сервер в интерактивном режиме:

```bash
$ docker run -it --rm --name my-running-app my-image
```

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
EXPOSE 8000

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD [ "python3", "./manage.py", "runserver"]
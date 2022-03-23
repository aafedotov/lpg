FROM python:3.7-slim

WORKDIR /app

COPY gaz/requirements.txt .

RUN pip3 install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir

COPY gaz/ .

CMD ["gunicorn", "gaz.wsgi:application", "--bind", "0:8000" ]
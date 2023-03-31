FROM docker.devopshobbieslearning.com/utils/python:3.10.7-slim-buster
ENV HOME=/app
ENV APP_HOME=/app/backend
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


RUN mkdir -p /app && \
   groupadd -r appuser && useradd --no-log-init -r -g appuser appuser && \
    python -m pip install --upgrade pip && \
    mkdir ${APP_HOME} ${APP_HOME}/logs 

WORKDIR ${APP_HOME}
EXPOSE 8000


# Install pip requirements
COPY requirements.txt .
COPY . ${APP_HOME}


RUN python -m pip install -r requirements.txt && pip install ipython==8.2.0 && pip install gunicorn==20.1.0 

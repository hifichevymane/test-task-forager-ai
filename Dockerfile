FROM python:3.12.1-alpine

ENV PYTHONBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=music_service.settings

WORKDIR /api

# Install poetry packet manager
RUN pip install poetry

COPY pyproject.toml poetry.lock /api/

# Install all dependencies
RUN poetry install

COPY . /api/

COPY start.sh .

# Give permission to run a .sh file
RUN chmod +x start.sh

EXPOSE 8000

CMD ./start.sh
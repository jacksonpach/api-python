FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./pyproject.toml /

RUN apt-get update -y && apt-get install netcat gcc curl openssh-server -y \
&& curl -sSL https://install.python-poetry.org | python3 - \
&& poetry config virtualenvs.create false \
&& poetry install \
&& mkdir /var/run/sshd

RUN python -m pip install --upgrade pip
RUN pip install pydevd-pycharm~=232.9559.58
RUN pip install trio~=0.22.2

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test

RUN echo 'test:test' | chpasswd

COPY ./app /app
WORKDIR /app

# Copiar e tornar o script entrypoint executável
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3"]
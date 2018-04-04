FROM python:3
WORKDIR /usr/src/app
ADD Pipfile /usr/src/app
ADD Pipfile.lock /usr/src/app
RUN pip install pipenv
RUN pipenv install --dev
ADD . /usr/src/app

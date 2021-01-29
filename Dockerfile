FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /NewsArticle
COPY requirements.txt /NewsArticle/
RUN pip list --outdated
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY . /NewsArticle/
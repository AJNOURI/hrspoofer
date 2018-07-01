FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD genip.py /genip.py
ADD hrspoofer.py /hrspoofer.py
RUN apt-get update && apt-get -y install vim nano apache2-utils
COPY genip.py genip.py
COPY hrspoofer.py hrspoofer.py
RUN chmod +x *.py
RUN git clone https://github.com/google/ipaddr-py
WORKDIR ipaddr-py
RUN python setup.py install
WORKDIR / 

FROM ubuntu:18.04

RUN  apt-get update && apt-get install -y python3 python3-pip python3-dev \
		libasound2 libatk1.0-0 libc6 libcairo2 \
		libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 \
		libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 \
		libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 \
		libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 \
		libxdamage1 libxext6 libxfixes3 libxi6 \
		libxrandr2 libxrender1 libxss1 libxtst6 \
		libappindicator1 libnss3 lsb-release

RUN apt-get clean autoclean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/aws_workshop
WORKDIR /opt/aws_workshop

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache
COPY chromium.py /opt/aws_workshop/
RUN python3 chromium.py

COPY script.py /opt/aws_workshop/
COPY tag.json /opt/aws_workshop/

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["python3", "script.py"]
FROM python:3

ADD mangadomnload.py /home
RUN pip install requests
RUN pip install BeautifulSoup4
WORKDIR /home



CMD [ "python   mangadomnload.py" ] > ../home

VOLUME ../home
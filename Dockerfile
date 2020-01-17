FROM python:3
ADD mangadomnload.py /
RUN pip install requests
RUN pip install BeautifulSoup4



CMD [ "python", "mangadomnload.py","titre","1","1"]  
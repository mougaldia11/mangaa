#!/usr/bin/env python3


import sys
import requests
from bs4 import BeautifulSoup
import os
import sys

homepage = "http://www.mangapanda.com/"

#titre du manga
manga = sys.argv[1] 

if len(sys.argv)>2 : 
    try :

        if sys.argv[3] == '-':
            #Enter your your starting and ending chapter here
            min_chapter = sys.argv[2]
            max_chapter = sys.argv[4]
            min_chapter = int(min_chapter)
            max_chapter = int(max_chapter)

            filepath = "./" + manga + "/"

            #create subfolder for images
            if not os.path.exists(filepath):
                os.makedirs(filepath)

            for chap in (range(min_chapter, max_chapter + 1)):

                #check for length of chapter
                contents = BeautifulSoup(requests.get(homepage + manga + "/" + str(chap)).content, 'html.parser')
                pages = len(contents.find_all("option"))

                if pages == 0: 
                    print(manga + " chapter " + str(chap) + " not found, skipping..")

                for page in range(1, pages + 1):
                    #neat progress bar
                    sys.stdout.write('\r')
                    sys.stdout.write("Downloading chapter %s of %d  page %d/%d" % (str(chap).zfill(len(str(max_chapter))), max_chapter, page, pages))
                    sys.stdout.flush()

                    #get image url
                    contents = BeautifulSoup(requests.get(homepage + manga + "/" + str(chap) + "/" + str(page)).content, 'html.parser')
                    imgurl = contents.find(id="imgholder").find("img").get("src")

                    #save to file
                    f = open(filepath + manga + "-" + str(chap).zfill(4) + "-" + str(page).zfill(len(str(pages))) + ".jpg", 'wb')
                    f.write(requests.get(imgurl).content)
                    f.close()
                sys.stdout.write('\n')


    except IndexError :
        filepath = "./" + manga + "/"
        #creer un dossier pour y mettre les images
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        for chap in range(2, len(sys.argv) ):
            c=sys.argv[chap]
            #check for length of chapter
            contents = BeautifulSoup(requests.get(homepage + manga + "/" + str(c)).content, 'html.parser')
            pages = len(contents.find_all("option"))
            if pages == 0: 
                print(manga + " chapter " + str(c) + " not found, skipping..")
            for page in range(1, pages + 1):
                #neat progress bar
                sys.stdout.write('\r')
                sys.stdout.write("Downloading chapter %s  page %d/%d" % (str(c) , page, pages))
                sys.stdout.flush()
                #get image url
                contents = BeautifulSoup(requests.get(homepage + manga + "/" + str(c) + "/" + str(page)).content, 'html.parser')
                imgurl = contents.find(id="imgholder").find("img").get("src")
                #save to file
                f = open(filepath + manga + "-" + str(c).zfill(4) + "-" + str(page).zfill(len(str(pages))) + ".jpg", 'wb')
                f.write(requests.get(imgurl).content)
                f.close()
            sys.stdout.write('\n')
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Category:Computing"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

wikis = soup.find_all("div", attrs={"class":"CategoryTreeItem"})

while (1) :


for wiki in wikis:
    title = wiki.get_text()
    link = "https://en.wikipedia.org/"+wiki.a["href"]

    p_wiki = title + " [1] " + link + "\n"

    with open('computing.csv', 'a', -1, 'utf-8') as f:
        f.write(p_wiki)
    print(p_wiki)
    url2 = link
    res2 = requests.get(url2)
    res2.raise_for_status()

    soup2 = BeautifulSoup(res2.text, "lxml")

    wikis2 = soup2.find_all("div", attrs={"class": "CategoryTreeItem"})

    for wiki2 in wikis2:

        title2 = wiki2.get_text()
        link2 = "https://en.wikipedia.org/"+wiki2.a["href"]
       # print(title2 + " [2] " + link2 + "\n")
        p_wiki2 = title2 + " [2] " + link2 + "\n"
        print(p_wiki2)

        with open('computing.csv', 'a', -1, 'utf-8') as f:
            f.write(p_wiki2)

        url3 = link2
        res3 = requests.get(url3)
        res3.raise_for_status()

        soup3 = BeautifulSoup(res3.text, "lxml")

        wikis3 = soup3.find_all("div", attrs={"class": "CategoryTreeItem"})

        for wiki3 in wikis3:
            title3 = wiki3.get_text()
            link3 = "https://en.wikipedia.org/" + wiki3.a["href"]
         #   print(title3 + " [3] " + link3 + "\n")

            p_wiki3 = title3 + " [3] " + link3 + "\n"
            #    print(title, " <#1> ", link)
            print(p_wiki3)
            with open('computing.csv', 'a', -1, 'utf-8') as f:
                f.write(p_wiki3)

            url4 = link3
            res4 = requests.get(url4)
            res4.raise_for_status()

            soup4 = BeautifulSoup(res4.text, "lxml")

            wikis4 = soup4.find_all("div", attrs={"class": "CategoryTreeItem"})

            for wiki4 in wikis4:
                title4 = wiki4.get_text()
                link4 = "https://en.wikipedia.org/" + wiki4.a["href"]

                p_wiki4 = title4 + " [4] " + link4 + "\n"
                #    print(title, " <#1> ", link)
                print(p_wiki4)
                with open('computing.csv', 'a', -1, 'utf-8') as f:
                    f.write(p_wiki4)
 #               print(title4,  " <#4> ", link4)


                url5 = link4
                res5 = requests.get(url5)
                res5.raise_for_status()

                soup5 = BeautifulSoup(res5.text, "lxml")

                wikis5 = soup5.find_all("div", attrs={"class": "CategoryTreeItem"})

                for wiki5 in wikis5:
                    title5 = wiki5.get_text()
                    link5 = "https://en.wikipedia.org/" + wiki5.a["href"]

                    p_wiki5 = title5 + " [5] " + link5 + "\n"
                    #    print(title, " <#1> ", link)
                    print(p_wiki5)
                    with open('computing.csv', 'a', -1, 'utf-8') as f:
                        f.write(p_wiki5)
                 #   print(title5,  " <#5> ", link5)

                    url6 = link5
                    res6 = requests.get(url6)
                    res6.raise_for_status()

                    soup6 = BeautifulSoup(res6.text, "lxml")

                    wikis6 = soup6.find_all("div", attrs={"class": "CategoryTreeItem"})

                    for wiki6 in wikis6:
                        title6 = wiki6.get_text()
                        link6 = "https://en.wikipedia.org/" + wiki6.a["href"]

                        p_wiki6 = title6 + " [6] " + link6 + "\n"
                        #    print(title, " <#1> ", link)
                        print(p_wiki6)
                        with open('computing.csv', 'a', -1, 'utf-8') as f:
                            f.write(p_wiki6)
                   #     print(title6,  " [#6] ", link6)
                      #  title6.to_csv('test.csv', encoding='cp949')


                        url7 = link6
                        res7 = requests.get(url7)
                        res7.raise_for_status()

                        soup7 = BeautifulSoup(res7.text, "lxml")

                        wikis7 = soup7.find_all("div", attrs={"class": "CategoryTreeItem"})

                        for wiki7 in wikis7:
                            title7 = wiki7.get_text()
                            link7 = "https://en.wikipedia.org/" + wiki7.a["href"]

                       #     print(title7,  " [#7] ", link7)

                            p_wiki7 = title7 + " [7] " + link7 + "\n"
                        #    print(title, " <#1> ", link)
                            print(p_wiki7)
                            with open('computing.csv', 'a', -1, 'utf-8') as f:
                                f.write(p_wiki7)

                                url8 = link7
                                res8 = requests.get(url8)
                                res8.raise_for_status()

                                soup8 = BeautifulSoup(res8.text, "lxml")

                                wikis8 = soup8.find_all("div", attrs={"class": "CategoryTreeItem"})

                                for wiki8 in wikis8:
                                    title8 = wiki8.get_text()
                                    link8 = "https://en.wikipedia.org/" + wiki8.a["href"]

                                    #     print(title7,  " [#7] ", link7)

                                    p_wiki8 = title8 + " [8] " + link8 + "\n"
                                    #    print(title, " <#1> ", link)
                                    print(p_wiki8)
                                    with open('computing.csv', 'a', -1, 'utf-8') as f:
                                        f.write(p_wiki8)
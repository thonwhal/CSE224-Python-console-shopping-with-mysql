import urllib.request as urllib2
from bs4 import BeautifulSoup as b

x = 0


def shopSearch(request, page):
    b_url = "https://www.n11.com/arama?q="
    url_sep = "&pg="
    url = b_url + request + url_sep + page
    html = urllib2.urlopen(url).read()
    soup = b(html, "html.parser")
    for post in soup.findAll("li", {"class": "column"}):
        try:
            item = post.findAll("a", {"class": "plink"})[0]
            title = item['title']
            price = post.findAll("ins")[0].text.replace(" ", "").replace("\n", "")
            link = item['href']
            sellerName = post.findAll("span", {"class": "sallerName"})[0].text.replace(" ", "").replace("\n", "")
            sellerPoint = post.findAll("span", {"class": "point"})[0].text.replace(" ", "").replace("\n", "")
            print(title)
            print(price + "\t Seller Name: " + sellerName + "\t Rating: " + sellerPoint)
            print(link + "\n")
        except:
            pass


def cheapest(request, page):
    x = []
    b_url = "https://www.cimri.com/arama?"
    url_sep = "page="
    seps2 = "&q="
    url = b_url + url_sep + page + seps2 + request
    html = urllib2.urlopen(url).read()
    soup = b(html, "html.parser")
    for post in soup.findAll("div", {"id": "cimri-product"}):
        try:

            item = post.findAll("h2", {"class": "product-title"})[0].text
            link = post.findAll("a")[0]['href']
            for markets in post.findAll("div", {"class": "tag"}):
                market = markets.text
            for prices in post.findAll("a", {"class": "s14oa9nh-0 gwkxYt"}):
                x.append(prices.text.replace("com", "com : ").replace(".tr", ""))
            print(item)
            print(x[0])
            print(x[1])
            print("https://www.cimri.com/" + link + "\n")
            x = []
        except:
            pass


print("Welcome!\nPlease make a choice.")
while 1:
    page = "1"
    choice = int(input(
        "\n1)I want a quick search from n11.com.\n2)I want cheapest search from cimri.com.\n3)Show me fav products of "
        "today.\n4)Exit.\n"))
    if choice == 1:
        request = input("\nStart search:\n").replace(" ", "+")
        shopSearch(request, page)
        pcho = int(input("\nDo you wanna continue to next page ? 1)Yes, 2)No.\n"))
        if pcho == 1:
            page = str(int(page) + 1)
            shopSearch(request, page)
        elif pcho == 2:
            print("")
        else:
            print("\ninvalid choice")
    elif choice == 2:
        request = input("\nStart search:\n").replace(" ", "+")
        cheapest(request, page)
        ccho = int(input("\nDo you wanna continue to next page ? 1)Yes, 2)No.\n"))
        if ccho == 1:
            page = str(int(page) + 1)
            cheapest(request, page)
        elif ccho == 2:
            print("")
    elif choice == 3:
        request = "0"
        cheapest(request, page)
    elif choice == 4:
        break
    else:
        print("\ninvalid choice")

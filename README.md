# URL-Hashing

[URL Hashing](https://en.wikipedia.org/wiki/URL_Hashing) is a technique on the World Wide Web in which a Uniform Resource Locator (URL) may be made substantially shorter and still direct to the required page. This is achieved by using a redirect which links to the web page that has a long URL.

### Clone the Repository
```
https://github.com/addyp1911/URL_Hasher
```
### Install Dependencies
The project uses following tech stack:
* Python 3.8.3
* Django 3.0.8
* django-crispy-forms==1.9.1


To install dependencies, run
```
pip install -r requirements.txt
```

### Navigate to the Directory
Navigate to the  Directory by following this command
```
cd url_hasher
```

### Run the Docker Application
```
docker-compose up -d
```
### To rebuild the Docker Application
```
docker-compose build
docker-compose up -d
```

### Open the WebApp in Browser
Open [http://host:port/home](http://host:port/home)
The home page will be displayed which will show a form to enter the url, along with

### Shorten URL
Enter a URL in the text box
In the form that appears, fill in the URL, Campaign, Source, and Medium fields. If you'd like to add source and medium, you can do so in the bottom two fields of this form.
After submitting the form, the shortened URL will be generated which can be used in your marketing campaign.

### Sources
https://blog.hubspot.com/marketing/what-are-utm-tracking-codes-ht

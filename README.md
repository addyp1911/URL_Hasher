# Creating URL-Hasher
This is a mini project to give an idea of how a url can be hashed for encryption and it can be used to return results matching the title of the URL.

### Clone the Repository
```
https://github.com/addyp1911/URL_Hasher
```
### Install Dependencies
The project uses following tech stack:
* Python 3.8.3
* Django 3.0.8


To install dependencies, run
```
pip install -r requirements.txt
```

### Navigate to the Directory
Navigate to the  Directory by following this command
```
cd URL_Hasher
```


### Open the WebApp in Browser
Open [http://localhost:port/home]

The home page will be displayed which will show a form to register yourself and log in .

### Enter the URL
Enter the URL with its optional utm source,medium and campaign fields and get the hashed version of the url which id stored in postgresql db 
to be retrieved when clicked on the link, that redirects to the desired website, also search option requests you to enter a keyword and a url, and it return all the related pages corresponding to the keyword in that site.



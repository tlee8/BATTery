
# :battery: Team BATTery :battery:

## :zap: Thomas Lee (PM), Tim Marder, Britni Canale, Ahnaf Kazi :zap:


### *:page_with_curl: Summary :page_with_curl:*

Our site, The Daily Devo, will provide information on what's going on for that day. Some included features will be:
- News
- Word of the day
- Date fact
- Weather
- Extra fun miscellaneous APIs

The website will include a login system, saving feature, and social media functionality such as liking, commenting, and sharing.

### How to install and run Daily Devo ###

1. First, clone Daily Devo. Use <a href ="https://help.github.com/articles/cloning-a-repository/">this</a> guide to learn how.
2. Make sure that you have python3 downloaded onto your machine. Additionally, make sure you have a virtual environment installed (learn how <a href = "https://docs.python.org/3/library/venv.html">here</a>). Activate your virtual environment using the following commands:
```
foo@bar:~$ cd venv
foo@bar:~/venv$ source bin/activate
```
3. Install flask using the following command:
```
(venv)foo@bar:~$ pip install flask
```
4. Inside of BATTery, the directory you cloned, run ```app.py``` as shown:
```
(venv)foo@bar:~$ cd BATTery
(venv)foo@bar:~/BATTery$ python app.py
```
5. In your preferred browser, open the link to the Daily Devo. This will be available at your machine's local IP address. It will appear as a link in the terminal where Daily Devo is running. It can also be typed manually as http://127.0.0.1:5000 or http://localhost:5000
6. For instructions on how to use Daily Devo, read the "How to use Daily Devo" section below.
7. To quit the application, open your terminal and type ```CTRL-C```

### What is Daily Devo? ###
The Daily Devo is an interactive portal with the purpose of providing users with information that is helpful for them going throughout their day. Some of the information available includes but is not limited to: recent news articles, current weather, word of the day, and transit information. Users will be able to like, comment on and share articles with other users. Users will also be able to customize their feeds.

### How to use Daily Devo ###
#### Login & Register ####
All users must be logged in to use Daily Devo. Users will immediately be directed to the login page unless they are already logged in, in which case they will be directed to the home page. If a user does not have an account, they may create one by clicking on the link to the register page. After they successfully create an account, they will be prompted to log in again.

#### Home Page ####
On the home page, all available information will be shown by default. The heading contains links to other pages on the site, such as the Popular Posts, My Articles and Preferences pages. There is also always a logout button shown so users can logout at any point. On the main portion of the website, recent article headings and previews are shown. These will contain a link that will direct the user to a page specifically for that article, where the whole article may be viewed. On the right side, there is a sidebar containing snippets of information, such as weather.

#### Articles ####
When viewing a specific article, users will have many options. There will be a link to the source of the article, so users can view from the original website. Users will also be able to like and comment on articles, as well as share them with other users.

#### Popular Posts ####
This page will contain the headings and descriptions of the articles that have been liked and commented on the most by users. Similarly to the home page, users will be able to click on the heading and be directed to a page containing the whole article.

#### My Articles ####
Here, users will be able to view any articles they have commented on or liked, and any articles they have shared or that have been shared with them. Again, it will only display headings and descriptions, but links will be available to view the article in its entirety.

### Preferences ####
On this page, users will be able to customize the information that is displayed on their home page. Users can indicate a preferred news source, as well as whether or not they want the other daily information to be displayed on the side bar.

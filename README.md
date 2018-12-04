
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
'''
foo@bar:~$ cd venv
foo@bar:~/venv$ source bin/activate
'''
3. Install flask using the following command:
'''
(venv)foo@bar:~$ pip install flask
'''
4. Inside of BATTery, the directory you cloned, run '''app.py''' as shown:
'''
(venv)foo@bar:~$ cd BATTery
(venv)foo@bar:~/BATTery$ python app.py
'''
5. In your preferred browser, open the link to the Daily Devo. This will be available at your machine's local IP address. It will appear as a link in the terminal where Daily Devo is running. It can also be typed manually as http://127.0.0.1:5000 or http://localhost:5000
6. For instructions on how to use Daily Devo, read the "How to use Daily Devo" section below.
7. To quit the application, open your terminal and type '''CTRL-C'''

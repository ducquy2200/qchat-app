# QCHAT APP
QChat is a group chat app with multiple sockets, developed mainly with <b>Python's Flask</b> and backend modules as well as pure <b>JavaScript</b> and a responsive <b>Bootstrap</b> design on the frontend (Edit: Bootstrap links were corrupted (or maybe I am just bad) which causes the message to disappear to no message animation. Therefore, the temporary solution to the problem is to display messages in plain text and will fix later on)


## Link to heroku live app

https://qchat-application.herokuapp.com


## Configuration

Then make sure all the required modules listed in requirements.txt file are installed on your machine.

For manual installation enter the following command.
```
$ pip3 install moduleName
```
Make sure that you have install virtual environment, if not use the following command
```
$ pip3 install virtualenv
```
On your project folder enter the following commands in order to create a virtual environment.

```bash
virtualenv venv
```

Next, activate your virtual environment using the following command.

```bash
source venv/Scripts/activate  
```
Note: This only works for Linux. For Windows and Macs, replace ```Scripts```with ```bin```

Install the requirements using the following command.

```bash
pip install -r requirements.txt
```

Make a few adjustment on the code at application.py file:

1- Change the database secret key and url according to their comments above of them (can be found from line 10 to 17 on application.py)


```python
# Secret key
app.secret_key = 'secret'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ywbnoztyucofwo:f770a5fb7b4ebc3df8f2b59d682c2f87f409142b36bd8248b36a07c046b03808@ec2-54-164-22-242.compute-1.amazonaws.com:5432/d1mp446fh6pe2b'
```

2- Change the last line of code on application.py according to the guide below.
```python
# remove the code below and use "socketio.run(app, debug=True)" if running on a local system
app.run()
```

## Running (for people who want to run the program locally)

To run your project enter the following command.

```
python application.py
```

Then copy the local address into a web browser (Chrome is recommended but you can also use Vivaldi). Here is an example:

```
http://127.0.0.1:5000/
```

You will be directed to a registration page first.

![Registration Page](/visuals/sign-up.png)


After completing the registration you will be required to login with your credentials.

![Login Page](/visuals/login.png)


Upon logging in, you will be able to use different chat rooms to talk with the online users.

![Chat Room](/visuals/chat.png)


## Future Improvements

1- Fix visual and animation problem from Bootstrap

2- I don't know, maybe I might make it into Tinder #2 but with video call

## License

[MIT](https://choosealicense.com/licenses/mit/)

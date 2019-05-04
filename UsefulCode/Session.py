# -*- coding: utf-8 -*-
__author__ = 'xzq'

user_list = [{'username':'John','password':'123'}, {'username':'Jerris','password':'456'}]
current_user = {'username':None, 'login':False}

import functools
def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if current_user['login'] == True:
            return func(*args, **kwargs)
        name = input('username:').strip()
        password = input('password:').strip()

        for user in user_list:
            if name == user['username'] and password == user['password']:
                current_user['username'] = name
                current_user['login'] = True
                return func(*args, **kwargs)
        print('Wrong username or password')
    return wrapper

@authenticate
def home():
    print('Welcome')

@authenticate
def Index(name):
    print('Hello {0}'.format(name))



if __name__ == "__main__":
   home()
   Index('xzq')



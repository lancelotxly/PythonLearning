# -*- coding: utf-8 -*-
__author__ = 'xzq'

user = {
    'Xzq':'123',
    'Jerris':'456',
    'Cindy':'789'
}
current_user = {'username':None, 'status':None}

def authenticate(times):
    def decorate(func):
        def wrapper(*args, **kwargs):
            if current_user['status'] == 'LOGIN':
                return func(*args, **kwargs)

            if current_user['status'] == 'LOCKED':
                print('User <{0}> has been locked. Please contact us soon.'.format(current_user['username']))

            while True:
                name = input('Username:')
                if name not in user:
                    print('User <%s> not exist' % name)
                    continue
                else:
                    current_user['username'] = name

                with open('Black_User_List.txt','r',encoding='utf-8') as f:
                    locked_users = f.read().strip()
                    if name in locked_users:
                        current_user['status'] = 'LOCKED'
                        print('User <{0}> has been locked. Please contact us soon.'.format(current_user['username']))
                        break

                print('You have 3 times chances to input password.')
                for i in range(times):
                    password = input('Password:')
                    if password == user[name]:
                        current_user['status'] = 'LOGIN'
                        with open('Current_User_List.txt','a',encoding='utf-8') as f:
                            f.write('%s|' % name)
                        return func(*args, **kwargs)

                print('User <{0}> has been locked. Please contact us soon.'.format(current_user['username']))
                current_user['status'] = 'LOCKED'
                with open('Black_User_List.txt','a',encoding='utf-8') as f:
                    f.write('%s|' % name)
                break

        return wrapper
    return decorate

@authenticate(3)
def home():
    print('Welcome <%s>' % current_user['username'])

@authenticate(3)
def run_cmd():
    while True:
        cmd = input('>>:')
        if not cmd:
            continue
        elif cmd.lower() == 'quit':
            with open('Current_User_List.txt','w+',encoding='utf-8') as f:
                users = f.read().strip()
                users = users.replace('{0}|'.format(current_user['username']),'')
                f.write(users)
            print('Bye')
            break

if __name__ == "__main__":
    home()
    run_cmd()


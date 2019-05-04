import configparser

config = configparser.ConfigParser()
config["DEFAULT"]
config['yuan'] ={
    'Password':'123',
    'Quotation':'100'
}
config['root']={
    'Password':'root',
    'Quotation':100
}
with open('D:\\PythonWorkspace\\PythonLearning\\Network\\FTP_Server\\config\\accounts.cfg','w') as f:
    config.write(f)

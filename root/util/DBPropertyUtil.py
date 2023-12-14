import configparser

class DBConnUtil:
    @staticmethod
    def get_property_strig():
        config = configparser.configParser()
        config.read('root/util/prop_file')
        hostname = config.get('DATABASE', 'hostname')
        dbname = config.get('DATABASE', 'dbname')
        username = config.get('DATABASE', 'username')
        password = config.get('DATABASE', 'password')
        port = config.get('DATABASE', 'port')

        connection_String= f'host={hostname} dbname={dbname} user={username} password={password} port={port}'

        return connection_String
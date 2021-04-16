'''
This module has classes to parse a configuration file using configparser and
set attributes using the keys provided in file.
'''
import json
import configparser

class ConfigurationKeys:
    '''
    This class represents all keys with the values of a config file session.
    '''
    def __init__(self, **kwargs):
        # Iterate over kwargs items
        for k,v in kwargs.items():
            try:
                if isinstance(v, str):
                    # Removing single and double quotes
                    v = v.replace('\'','').replace('"','')
                    # Trying to convert into boolean type
                    if 'true' == v.lower():
                        v = True
                    elif 'false' == v.lower():
                        v = False

                    # Trying to convert into float or int type
                    v = float(v) if '.' in v else int(v)
            except:
                pass
            finally:
                # Set the attribute
                setattr(self, k.lower(), v)
    
    def __str__(self):
        '''
        Return a str in json format.
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class ConfigurationReader:
    '''
    This class represents a session from the configuration file.
    '''
    def __init__(self, path=None):
        # Reading the config file
        config = configparser.ConfigParser()
        config.read(path, encoding='utf-8')

        # Iterating over the sessions
        for section in config.sections():
            config_keys = ConfigurationKeys(**dict(item for item in config[section].items()))
            setattr(self, section.lower(), config_keys)

    def __str__(self):
        '''
        Return a str in json format.
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

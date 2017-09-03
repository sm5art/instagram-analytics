import configparser
from insta.utils.directory import get_current_directory

CONFIG = "credentials.cfg"


def get_token():
    config = configparser.ConfigParser()
    config_location = get_current_directory(__file__) + CONFIG
    config.read(config_location)
    api = config.get('instagram', 'ACCESS_TOKEN')
    return api


def get_endpoint():
    config = configparser.ConfigParser()
    config_location = get_current_directory(__file__) + CONFIG
    config.read(config_location)
    endpoint = config.get('instagram', 'BASE_ENDPOINT')
    return endpoint

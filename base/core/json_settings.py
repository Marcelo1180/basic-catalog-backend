import json
import os
__BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def get_settings():
    """
    Reading json config file
    :return:
    """
    with open("{0}/{1}".format(__BASE_DIR, "../settings.json")) as data_file:
        data = json.load(data_file)
    return data

import logging
import logging.config
import yaml


def configure_logger(name, log_path):
    f = open('.\configs\logging.yaml', 'r')
    d = yaml.safe_load(f)
    d['handlers']['file']['filename'] = log_path

    # print(d['handlers']['file'])

    logging.config.dictConfig(d)

    return logging.getLogger(name)

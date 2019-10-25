import logging, yaml, os, time
from logging.config import dictConfig
from config.custom_formatter import LogstashFormatter


# Locating the logging configuration file.
logging_config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'log.cfg.yml')

# Loading the configuration to logging module.
with open(logging_config_file, 'r') as log_config:
    dictConfig(yaml.full_load(log_config))

# Updating LogFactory in order to add custom information to LogRecords.
# https://stackoverflow.com/questions/17558552/how-do-i-add-custom-field-to-python-log-format-string

actual_factory = logging.getLogRecordFactory()

def log_record_factory(*args, **kwargs):
    '''
    Adding custom information to all LogRecords.
    '''
    record = actual_factory(*args, **kwargs)
    record.timezone = 'GMT %s' % time.tzname[0] # Adding machine TimeZone info.
    record.host = os.uname()[1] # Adding machine host name info.
    return record

logging.setLogRecordFactory(log_record_factory) # From now, all LogRecords will have timezone and host information to be used in the LogFormatters.
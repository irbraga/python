import logging, datetime, json
from logging import Formatter


class LogstashFormatter(Formatter):
    '''
    Custom Formatter to log in JSON format.
    '''
    def format(self, record):

        data = {'@timestamp': super().formatTime(record, self.datefmt),
        'timezone': record.timezone, # Added custom information modifying the LogFactory in the __init__.py script.
        'source_host': record.host, # Added custom information modifying the LogFactory in the __init__.py script.
        'module': record.module,
        'filename': record.filename,
        'method': record.funcName,
        'level': record.levelname,
        'line': record.lineno,
        'thread_name': record.threadName,
        '@version': logging.__version__,
        'logger_name': record.name,
        'message': record.msg}

        # If the LogRecord has some info about an exception, format and add it.
        if record.exc_info:
            data['exception'] = super().formatException(record.exc_info)

        # If the LogRecord has some stacktrace about an exception, format and add it.
        if record.stack_info:
            data['stacktrace'] = super().formatStack(record.stack_info)

        # Return the message in Json format.
        return json.dumps(data)
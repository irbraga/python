#!/usr/bin/env python
import logging
import config # The __init__.py script has some logging configuration.


def method_with_debug_logged_message():
    logging.getLogger().debug('You will see this message in the logs if the log level is DEBUG or higher.')

def method_with_info_logged_message():
    logging.getLogger().info('You will see this message in the logs if the log level is INFO or higher.')

def method_with_warning_logged_message():
    logging.getLogger().warning('You will see this message in the logs if the log level is WARNING or higher.')

def method_with_error_logged_message():
    logging.getLogger().error('You will see this message in the logs if the log level is CRITICAL or higher.')

def method_with_critical_logged_message():
    logging.getLogger().critical('You will see this message in the logs if the log level is CRITICAL or higher.')

def method_with_error_logging_exception_message():
    try:
        raise AttributeError('Something unexpected happened here!!!')
    except AttributeError:
        logging.getLogger().error("Okay, got the problem. Now let's log the exception.", exc_info=True)
    
def method_with_error_logging_exception_and_stacktrace_message():
    try:
        raise AttributeError('Something unexpected happened here!!!')
    except AttributeError:
        logging.getLogger().error("Okay, got the problem. Now let's log the exception and the stacktrace.", exc_info=True, stack_info=True)
        
if __name__ == "__main__":
    '''
    The logging LEVEl can be changed in the confg/log.cfg.yaml file.

    Debug levels:
        CRITICAL
        ERROR
        WARNING
        INFO
        DEBUG
        NOTSET
    '''
    method_with_debug_logged_message()
    method_with_info_logged_message()
    method_with_warning_logged_message()
    method_with_error_logged_message()
    method_with_critical_logged_message()
    method_with_error_logging_exception_message()
    method_with_error_logging_exception_and_stacktrace_message()

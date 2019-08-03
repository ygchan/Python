# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# If you have used print() to output some variable's value while your program
# is running. You have already done a form of logging.

# Python's logging module makes it easy to create a record of custom
# messages that you write.

# Missing log message indicates a part of the code was skipped.

import logging
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.error('Error!!! Get into the chopper!')

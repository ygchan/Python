# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# If you have used print() to output some variable's value while your program
# is running. You have already done a form of logging.

# Python's logging module makes it easy to create a record of custom
# messages that you write.

# Missing log message indicates a part of the code was skipped.

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

# When Python logs an event, it creates a LogRecord object that holds
# information about that event. 

# Factorial of 4 is 1 X 2 X 3 X 4 or 24.

logging.debug('Start of program.')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))

    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of a program.')

##================ RESTART: /Users/Study/Python/038_Logging.py ================
## 2019-08-02 21:26:43,266 - DEBUG- Start of program
## 2019-08-02 21:26:43,328 - DEBUG- Start of program.
## 2019-08-02 21:26:43,368 - DEBUG- Start of factorial(5)
## 2019-08-02 21:26:43,420 - DEBUG- i is 1, total is 1
## 2019-08-02 21:26:43,470 - DEBUG- i is 2, total is 2
## 2019-08-02 21:26:43,520 - DEBUG- i is 3, total is 6
## 2019-08-02 21:26:43,570 - DEBUG- i is 4, total is 24
## 2019-08-02 21:26:43,620 - DEBUG- i is 5, total is 120
## 2019-08-02 21:26:43,670 - DEBUG- End of factorial(5)
##120
## 2019-08-02 21:26:43,770 - DEBUG- End of a program.

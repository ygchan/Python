# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# Traceback
import traceback

try:
    # This line raise the Exception right away
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    # traceback.format_exc()
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to the errorInfo.txt')

# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# Trace back contains the error message, the line number
# and the sequence of function that led to the error.

def spam():
    bacon()
def bacon():
    raise Exception('This is a random error message.')

# spam()

# We see from the trace back, error happened in line 10.
# and you can also obtain it as a string by calling traceback.format_exc()
# This is used when you want the except statement to handle the exception
# gracefully, while still getting the traceback.

# Best of both word using traceback.format_exc()

# Practing the traceback
def Load_file():
    Convert_Member_ID()
def Convert_Member_ID():
    raise Exception('The member ID is invalid or missing.')

Convert_Member_ID()

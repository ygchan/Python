# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

market_2nd = {'ns': 'green', 'ew': 'red'}
missing_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    '''Takes an intersection dictionary as an arugment and switch the light'''

    # If you want to make sure (assert) one of the light is always red
    assert 'red' in stoplight.values(), 'Neight light is red!' + str(stoplight)

    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] == 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] == 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

switchLights(market_2nd)

# AssertionError: << Something bad happened.

# Assertions are for development, not for final product
# See Appendix B for details about how to launch your probably not insane
# program with the -o option.

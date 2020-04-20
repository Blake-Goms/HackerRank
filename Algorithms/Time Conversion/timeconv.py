def timeConversion(s):
    #
    # Write your code here.
    #
    # Check to see if last is AM and start is 12 to handle edge case 1
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    # if not 12 but AM then remove AM, should be solved by else but 2 tests failed without this
    elif s[-2:] == "AM":
        return s[:-2]
    # check to see if last is PM and start is 12 to handle edge case 2
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    # Otherwise just add 12 to hour position
    else:
        return str(int(s[:2]) + 12) + s[2:8]
    
    
timeConversion("07:05:45PM")
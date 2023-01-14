import re
def validate_usr(username):
    if(re.search("^[\da-z_]{4,16}$", username)):
        return True
    return False
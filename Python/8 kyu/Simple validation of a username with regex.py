import re
def validate_usr(username):
    if(re.search("^([\d,a-z,1-9,_]){4,16}$", username)):
        return True
    return False
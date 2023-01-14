def find_slope(points):
    if(points[0] - points[2] == 0):
        return 'undefined'
    else:
        return str(int((points[1] - points[3])/(points[0] - points[2])))
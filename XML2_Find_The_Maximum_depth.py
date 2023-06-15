maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if(len(elem.findall(".//"))>0):
        level = level + 1
        if(level >= maxdepth):
            maxdepth=level+1
        for i in elem:
            depth(i, level)


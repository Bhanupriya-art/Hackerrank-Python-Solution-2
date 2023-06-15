def get_attr_number(node):
    # your code goes here
    count = 0
    for tag in node:
        count = count + get_attr_number(tag)
    return count + len(node.attrib)


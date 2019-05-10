# def add_tags(tag, content):
#     return "<" + tag + ">" + content + "</" + tag + ">"


def add_tags(tag, content):
    return "<%s>%s</%s>" % (tag, content, tag)


if __name__ == '__main__':
    print(add_tags("i", "Python"))
    print(add_tags("b", "Python Tutorial"))

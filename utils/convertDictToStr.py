import collections


def convertDictToStr(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convertDictToStr, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convertDictToStr, data))
    else:
        return data
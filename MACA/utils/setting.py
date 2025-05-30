import os

import yaml


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state


def dict2obj(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    d = Dict()
    for k, v in dictObj.items():
        d[k] = dict2obj(v)
    return d


def get_args(map_name = None):
    """返回参数
    """
    if map_name is None:
        f = open(os.path.split(os.path.realpath(__file__))[0] + '/param.yaml', 'r', encoding='UTF-8')
    else:
        f = open(os.path.split(os.path.realpath(__file__))[0] + '/' + map_name + '.yaml', 'r', encoding='UTF-8')
    file_data = f.read()
    f.close()

    return dict2obj(yaml.load(file_data, Loader=yaml.FullLoader))

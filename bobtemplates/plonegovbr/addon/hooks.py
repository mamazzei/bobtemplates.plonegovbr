# -*- coding:utf-8 -*-

def split_items_by_pipe(configurator, question, answer):
    import ipdb
    ipdb.set_trace()
    configurator.variables['author.fullname'] =
        configurator.variables['author.firstname'] + ' ' +
        answer
    return answer

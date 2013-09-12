# -*- coding:utf-8 -*-

def split_items_by_pipe(configurator, question, answer):
    configurator.variables[question.name] = answer.split('|')
    return answer

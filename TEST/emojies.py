# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:28:59 2022

@author: ibrah
"""
import emoji
emojis_iter = map(lambda y: y, emoji.UNICODE_EMOJI['en'].keys())
import re

regex_set = re.compile('|'.join(re.escape(em) for em in emojis_iter))

lista = ['😂']
new_lista = regex_set.findall(lista[0])


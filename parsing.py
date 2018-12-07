# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from pyparsing import *

rus_alphas = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
rus_alphas_upper='ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
# описываем грамматику
#data=Word(nums+".",exact=10) #19.10.2018
#time=Word(nums+":",exact=8)   #12:34:59
#status=Literal("|").suppress()+Word(alphas)+Literal("|").suppress() #|OkUnload|
#nomer=Literal("|").suppress()+Word(alphanums+"_#")+Literal(";").suppress() #F405_#1
grz=Literal(";").suppress()+Word(rus_alphas_upper+nums)+Literal(";").suppress()
pattern =grz

# читаем файл: lines -- список, каждый элемент которого содержит отдельную строку файла  
lines = file('protocol-Kris-2018-10-19.log','r').readlines()
text =  ''.join(lines)
#text = re.sub(r'\$.?\n', '', text)
# проверяем каждую строку на соответствие шаблону
for tokens in pattern.searchString(text):
	print (repr(tokens))

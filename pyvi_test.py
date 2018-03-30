# -*- coding: utf8 -*-
import codecs
import sys

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

sys.stdin = codecs.getreader('utf_8')(sys.stdin)
import pyvi
from pyvi.pyvi import ViTokenizer, ViPosTagger

# print(ViTokenizer.tokenize(u"Tôi ăn xôi xéo"))

output = ViPosTagger.postagging(ViTokenizer.tokenize(u"Tôi ăn rất nhiều cơm"))
print(output[0][0])

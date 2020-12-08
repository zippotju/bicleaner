
from toolwrapper import ToolWrapper
from sacremoses import MosesTokenizer

try:
    from .util import no_escaping
except (SystemError, ImportError):
    from util import  no_escaping

import jieba
import mecab


class Tokenizer:
    def __init__(self, command=None,  l="en"):
        self.l = l
        if self.l == "en":
            self.tokenizer = MosesTokenizer(lang=self.l)
        elif self.l == "zh":
            self.tokenizer = jieba.dt
        elif self.l == "ko":
            self.tokenizer = mecab.MeCab()
        else:
            raise RuntimeError("language code is either zh or en or ko") 

    def tokenize(self, text):
        if self.l == 'en':
            return self.tokenizer.tokenize(text, escape=False)
        elif self.l == 'zh':
            return list(self.tokenizer.cut(text))
        elif self.l == 'ko':
            return self.tokenizer.morphs(text)
        else:
            raise RuntimeError("language code is either zh or en or ko") 

    def detokenize(self, text):
        return ' '.join(text)

    def close(self):
        pass

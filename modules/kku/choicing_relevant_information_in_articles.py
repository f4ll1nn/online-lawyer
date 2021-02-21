""" Module of realisation choice relevant information in articles """
import langdetect
import openpyxl
import pandas as pd
import modules.pytextrank.pytextrank.pytextrank as pyt
from nltk.corpus import wordnet

from modules.kku.trans.mtranslate.mtranslate import translate


class Article:
    """ Class of articles """

    def __init__(self, number: int, name: str, punkt1=None, punkt2=None,
                 punkt3=None, punkt4=None, punkt5=None, punkt6=None,
                 punkt7=None, punkt8=None) -> None:
        """ Creates article """
        self.number = number
        self.name = name
        self.punkt1 = punkt1
        self.punkt2 = punkt2
        self.punkt3 = punkt3
        self.punkt4 = punkt4
        self.punkt5 = punkt5
        self.punkt6 = punkt6
        self.punkt7 = punkt7
        self.punkt8 = punkt8
        self.translated_name = None
        self.translated_punkt1 = None
        self.translated_punkt2 = None
        self.translated_punkt3 = None
        self.translated_punkt4 = None
        self.translated_punkt5 = None
        self.translated_punkt6 = None
        self.translated_punkt7 = None
        self.translated_punkt8 = None
        self.relevant_words = []

    def transalte_name(self) -> None:
        """ Translates name into english in order to use later Natural language
        Google Api. This information will be in self.translated_name """
        translated = translate(self.name, "en")
        self.translated_name = translated

    def translate_punkts(self) -> None:
        """ Translates punkt into english in order to use later Natural
        language Google Api."""
        punkts = [self.punkt1, self.punkt2, self.punkt3, self.punkt4,
                  self.punkt5, self.punkt6, self.punkt7, self.punkt8]
        for i in range(8):
            try:
                translated = translate(punkts[i], "en")
                if i == 0:
                    self.translated_punkt1 = translated
                if i == 1:
                    self.translated_punkt2 = translated
                if i == 2:
                    self.translated_punkt3 = translated
                if i == 3:
                    self.translated_punkt4 = translated
                if i == 4:
                    self.translated_punkt5 = translated
                if i == 5:
                    self.translated_punkt6 = translated
                if i == 6:
                    self.translated_punkt7 = translated
                if i == 7:
                    self.translated_punkt8 = translated
            except TypeError:
                pass

    def relevant_information_in_name(self) -> list:
        """ Choising relevant information in name of articles
        This words will be in self.relevant_name """
        text = self.name
        sentence, keywords = pyt.top_keywords_sentences(text, phrase_limit=15,
                                                        sent_word_limit=150)
        for i in self.translated_name.split():
            self.relevant_words.append(i)
        return self.relevant_words

    def relevant_information_in_punkts(self) -> list:
        """ Choising relevant indormation in each punkts of articles
         This words will be in self.relevant_point(number)"""
        for i in range(8):
            if i == 0:
                if self.translated_punkt1 is not None:
                    text = self.translated_punkt1
                else:
                    text = ""
            if i == 1:
                if self.translated_punkt2 is not None:
                    text = self.translated_punkt2
                else:
                    text = ""
            if i == 2:
                if self.translated_punkt3 is not None:
                    text = self.translated_punkt3
                else:
                    text = ""
            if i == 3:
                if self.translated_punkt4 is not None:
                    text = self.translated_punkt4
                else:
                    text = ""
            if i == 4:
                if self.translated_punkt5 is not None:
                    text = self.translated_punkt5
                else:
                    text = ""
            if i == 5:
                if self.translated_punkt6 is not None:
                    text = self.translated_punkt6
                else:
                    text = ""
            if i == 6:
                if self.translated_punkt7 is not None:
                    text = self.translated_punkt7
                else:
                    text = ""
            if i == 7:
                if self.translated_punkt8 is not None:
                    text = self.translated_punkt8
                else:
                    text = ""
            sentence, keywords = pyt.top_keywords_sentences(text,
                                                        phrase_limit=5000,
                                                        sent_word_limit=5000)
            if keywords.split() != []:
                for k in keywords.split():
                    self.relevant_words.append(k)
        return self.relevant_words

    def find_synonyms(self, relevant_words_list) -> set:
        """ Returns list of synonyms and this words, that can be relevant
        to each article """
        synonyms = []
        for word in relevant_words_list:
            try:
                for syn in wordnet.synsets(word):
                    for k in syn.lemmas():
                        translated = translate(k.name(), "uk")
                        synonyms.append(translated)
            except AttributeError:
                pass
        return set(self.synonyms_check(synonyms))

    def synonyms_check(self, set_syn) -> list:
        """ Check are all word in synonyms set ukrainian """
        for word in set_syn:
            try:
                if langdetect.detect(word) == "uk":
                    pass
                else:
                    set_syn.remove(word)
            except langdetect.lang_detect_exception.LangDetectException:
                set_syn.remove(word)
        return set_syn


if __name__ == "__main__":
    RESULT = pd.read_excel("articles_with_punkts.xlsx")
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    FINAL = [1, 2]
    for i in RESULT.index:
        try:
            ARTICLE = RESULT.loc[[i]]
            INDEX = int(ARTICLE["Рядки"].str.find("."))
            NUMBER = int(ARTICLE["Рядки"].str[6:INDEX].str.strip())
            NAME = ARTICLE["Рядки"].str[INDEX + 1:].str.strip().to_string()[3:].strip()
            PUNKTS = []
            for k in ARTICLE:
                if ARTICLE[k].to_string().find("NaN") == -1:
                    if k != "Рядки":
                        PUNKTS.append(k)
            ARTICLE_CL = Article(NUMBER, NAME)
            try:
                ARTICLE_CL.punkt1 = ARTICLE[PUNKTS[0]].to_string()[3:].strip()
                ARTICLE_CL.punkt2 = ARTICLE[PUNKTS[1]].to_string()[3:].strip()
                ARTICLE_CL.punkt3 = ARTICLE[PUNKTS[2]].to_string()[3:].strip()
                ARTICLE_CL.punkt4 = ARTICLE[PUNKTS[3]].to_string()[3:].strip()
                ARTICLE_CL.punkt5 = ARTICLE[PUNKTS[4]].to_string()[3:].strip()
                ARTICLE_CL.punkt6 = ARTICLE[PUNKTS[5]].to_string()[3:].strip()
                ARTICLE_CL.punkt7 = ARTICLE[PUNKTS[6]].to_string()[3:].strip()
                ARTICLE_CL.punkt8 = ARTICLE[PUNKTS[7]].to_string()[3:].strip()
            except IndexError:
                pass
            ARTICLE_CL.transalte_name()
            ARTICLE_CL.translate_punkts()
            ARTICLE_CL.relevant_information_in_name()
            WORDS = ARTICLE_CL.relevant_information_in_punkts()
            UKR_WORDS = ARTICLE_CL.find_synonyms(WORDS)
            print(UKR_WORDS)
            FINAL.append(UKR_WORDS)
        except ValueError:
            pass
    workbook = openpyxl.load_workbook("articles_with_punkts.xlsx")
    worksheet = workbook.active
    worksheet["J"] = FINAL
    workbook.save("articles_with_punkts.xlsx")

"""Module-sample of using Article ADT"""
import pandas as pd
from modules.kku.choicing_relevant_information_in_articles import Article

RESULT = pd.read_excel("articles_with_punkts.xlsx")
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
ARTICLE = RESULT.loc[[0]]
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
TASK = ARTICLE_CL.translated_punkt2.split()
print(ARTICLE_CL.find_synonyms(TASK))

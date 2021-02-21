""" Module-example of using KKU ADT"""
from modules.kku.creating_fie_for_articles_with_punkts import KKU

FILE = "kku.csv"
KKU_UK = KKU(FILE)
KKU_UK.reading_kku()
INDEXES = KKU_UK.choising_relevant_rows(param="index")
DF_STAT = KKU_UK.choising_relevant_rows(param="df")
DF_OLD = KKU_UK.choising_relevant_rows(param="df_old")
DF_NEW = KKU_UK.creating_df_for_result(DF_STAT)
LIST_PUNKTS = KKU_UK.choising_punkts(INDEXES, DF_OLD)
DF_NEW = KKU_UK.creating_result_df(DF_NEW, LIST_PUNKTS)
KKU_UK.creating_exel()

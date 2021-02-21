"""Module-example of using SAMPLES ADT"""
from modules.samples_reading.samples import Samples

FILE_NAME = "2.csv"
BOOK = Samples(FILE_NAME)
BOOK.situation_sample_read()
DF_STAT = BOOK.choising_relevant_rows(param="df")
INDEXES = BOOK.choising_relevant_rows(param="index")
DF_OLD = BOOK.choising_relevant_rows(param="df_old")
DF_NEW = BOOK.creating_df_for_result(DF_STAT)
LIST_PUNKTS = BOOK.choising_sentences(INDEXES, DF_OLD)
DF_NEW = BOOK.creating_samples_df(DF_NEW, LIST_PUNKTS)
BOOK.save_samples()

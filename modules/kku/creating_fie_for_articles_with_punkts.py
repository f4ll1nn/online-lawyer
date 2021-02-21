"""Module for creating exel file with articles and punkts to each articles"""
import csv

import pandas as pd


class KKU:
    """ Class of KKU """

    def __init__(self, file):
        """ Creates KKU"""
        self.file = file
        self.capasity = []
        self.result = None

    def reading_kku(self) -> list:
        """ Read file of kku in format csv and create list with all rows
        of this file. Returns list of rows """
        with open(self.file, newline='', encoding='utf-8') as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                self.capasity.append(row)
        return self.capasity

    def choising_relevant_rows(self, param: str) -> pd.DataFrame:
        """ Choices needed rows from file and write that indexes in list
        Returns list of indexes """
        df_start = pd.DataFrame(self.capasity)
        df_start.rename(columns={0: "Рядки"}, inplace=True)
        df_articles = df_start[df_start["Рядки"].str.startswith("Стаття")]
        index_list = list(df_articles.index)
        if param == "index":
            return index_list
        if param == "df":
            return df_articles
        if param == "df_old":
            return df_start
        return "Uncorrect param"

    def creating_df_for_result(self, df_for_using: pd.DataFrame) -> pd.DataFrame:
        """ Creates dataframe for result and returns it """
        df_new_creat = df_for_using.set_index("Рядки")
        return df_new_creat

    def choising_punkts(self, indexes_list: list, df_for_using: str) -> list:
        """ Choices punkts for articles and returns list of strings of
        punkts to each articles """
        first_list_punkts = []
        for k in range(len(indexes_list)):
            punkts_string = ""
            if k != len(indexes_list) - 1:
                result = df_for_using.iloc[
                         indexes_list[k] + 1: indexes_list[k + 1]]
                result = result.loc[result["Рядки"] != "", ["Рядки"]]
                for i in result["Рядки"]:
                    if i.endswith("."):
                        punkts_string += (i + "/")
                    else:
                        punkts_string += i
            first_list_punkts.append(punkts_string)
        return first_list_punkts

    def creating_result_df(self, df_user: pd.DataFrame, punkts: list) -> pd.DataFrame:
        """ Creates dataframe where each articles has all its punkts """
        df_user["Пункти"] = punkts
        df_new_result = df_user["Пункти"].str.split("/", n=7, expand=True)
        df_new_result.rename(
            columns={0: "Пункт 1", 1: "Пункт 2", 2: "Пункт 3",
                     3: "Пункт 4", 4: "Пункт 5", 5: "Пункт 6", 6: "Пункт 7",
                     7: "Пункт 8"}, inplace=True)
        self.result = df_new_result
        return df_new_result

    def creating_exel(self) -> None:
        """ Creates exel file with result """
        writer = pd.ExcelWriter("articles_with_punkts.xlsx",
                                engine="xlsxwriter")
        self.result.to_excel(writer, sheet_name="Sheet1")
        writer.save()


if __name__ == "__main__":
    FILE = "kku.csv"
    KKU_UA = KKU(FILE)
    KKU_UA.reading_kku()
    INDEXES = KKU_UA.choising_relevant_rows(param="index")
    DF_STAT = KKU_UA.choising_relevant_rows(param="df")
    DF_OLD = KKU_UA.choising_relevant_rows(param="df_old")
    DF_NEW = KKU_UA.creating_df_for_result(DF_STAT)
    LIST_PUNKTS = KKU_UA.choising_punkts(INDEXES, DF_OLD)
    DF_NEW = KKU_UA.creating_result_df(DF_NEW, LIST_PUNKTS)
    KKU_UA.creating_exel()

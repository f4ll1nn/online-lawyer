""" Module of reading tasks in 1.csv"""
import csv
import pandas as pd

class Samples:
    """ Class of Book """

    def __init__(self, file_name: str) -> None:
        """ Creates book """
        self.file_name = file_name
        self.lines = []
        self.result = None

    def situation_sample_read(self) -> list:
        """ Reads all rws from book. Returns list of rows """
        with open(self.file_name, newline='', encoding='utf-8') as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                self.lines.append(row)
        return self.lines

    def choising_relevant_rows(self, param: str) -> pd.DataFrame:
        """ Choices needed rows from file and write that indexes in list
        Returns list of indexes """
        df_start = pd.DataFrame(self.lines)
        df_start.rename(columns={0: "Рядки"}, inplace=True)
        for col in df_start.columns:
            if col != "Рядки":
                del df_start[col]
        df_tasks = df_start[df_start["Рядки"].str.startswith("Задача")]
        index_list = list(df_tasks.index)
        if param == "index":
            return index_list
        if param == "df":
            return df_tasks
        if param == "df_old":
            return df_start
        return "Uncorrect param"

    def creating_df_for_result(self, df_for_using: str) -> pd.DataFrame:
        """ Creates dataframe for result and returns it """
        df_new_creat = df_for_using.set_index("Рядки")
        return df_new_creat

    def choising_sentences(self, indexes_list: list, df_for_using: str) -> list:
        """ Choices sentences to task and returns list of strings of
        sentences to each tasks """
        first_list_punkts = []
        for k in range(len(indexes_list)):
            punkts_string = ""
            if k != len(indexes_list) - 1:
                result = df_for_using.iloc[
                         indexes_list[k] + 1: indexes_list[k + 1]]
                result = result.loc[result["Рядки"] != "", ["Рядки"]]
                for i in result["Рядки"]:
                    if i.endswith("."):
                        punkts_string += i
                    else:
                        punkts_string += i
            first_list_punkts.append(punkts_string)
        return first_list_punkts

    def creating_samples_df(self, df_user: str, punkts: list) -> pd.DataFrame:
        """ Creates dataframe where each task has all its sentences """
        df_user["Задачі"] = punkts
        df_new_result = df_user["Задачі"]
        self.result = df_new_result
        return df_new_result

    def save_samples(self) -> None:
        """ Creates exel file with result """
        writer = pd.ExcelWriter("samples_3.xlsx",
                                engine="xlsxwriter")
        self.result.to_excel(writer, sheet_name="Sheet1")
        writer.save()


if __name__ == "__main__":
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

# import pandas as pd
# import numpy as np
# import math
import xlsxwriter


# class ExcelValidation:
#     def __init__(self, file):
#         self.file = file
#
#     def read_file(self):
#         df = pd.read_excel(self.file)
#         print(df.columns)
#         df.columns = ["a", "b", "c", "d", "e", "f", "g"]
#         # df = pd.concat(df, ignore_index=True)
#         print("hi")
#         print(df.columns[0])
#         print("================")
#         print(df["a"][0])
#         print("====================")
#         print(df["a"][2])
#         print(df["e"][2])
#         # df_split = np.array_split(df, 2)
#         df_split = np.array(df)
#         print(df_split)
#         print(df_split[0])
#         print(df_split[1])
#         print(df_split[2])
#         df_split2 = np.array_split(df, 2)
#         print(df_split2[0])
#         print(df_split2[1])
#         print(df_split2)
#         # if math.isnan(df["e"][2]):
#         #     print("hello world")
#         # else:
#         #     print("bye world")
#         # print(df["e"][2])
#
#     def parse_row(self):
#         pass
#
#     def parallelize_dataframe(self, df, func, n_cores=4):
#         # df_split = np.array_split(df, n_cores)
#         # pool = Pool(n_cores)
#         # df = pd.concat(pool.map(func, df_split))
#         # pool.close()
#         # pool.join()
#         # return df
#         pass
#
#     def create_dataframe(self):
#         pass
#
#     # def loop(file_number):
#     #     pass
#     #     # return pd.read_pickle(f”Dummy {file_number}.pickle”)
#
#     # print(“Pickle//:”, end — start)


class WriteExcel:
    def __init__(self, file_name=None, sheet_name=None):
        self.workbook = None
        self.worksheet = None
        self.current_col = 0
        self.current_row = 0
        if file_name is not None and sheet_name is not None:
            self.create_file(file_name, sheet_name)

    def __del__(self):
        try:
            self.workbook.close()
        except Exception as e:
            print(e)

    def create_file(self, file_name, sheet_name):
        self.workbook = xlsxwriter.Workbook(file_name)
        self.add_worksheet(sheet_name)

    def add_worksheet(self, sheet_name):
        self.current_row = 0
        self.current_col = 0
        self.worksheet = self.workbook.add_worksheet(sheet_name)

    # NOTE: There's no real point in having separate add_cell and write_cell methods, seems super redundant
    def add_cell(self, data):
        self.worksheet.write(self.current_row, self.current_col, data)
        self.current_col += 1

    # NOTE: DOES NOT ACTUALLY ADD ROW
    # simply increments self.current_row, but we are keep the function name the same as java
    def add_row(self):
        self.current_row += 1


def test():
    write_excel = WriteExcel()
    write_excel.create_file("MyFile.xlsx", "oooga booga")
    write_excel.add_cell("Hi")
    write_excel.add_cell("Hi2")
    write_excel.add_cell("Hi3")
    write_excel.add_cell("Hi4")
    write_excel.add_cell("Hi5")
    write_excel.add_cell("Hi6")
    write_excel.add_cell("Hi7")


if __name__ == "__main__":
    test()

# import pandas as pd
# import numpy as np
# import math
import xlsxwriter


class WriteExcel2:
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

    def add_cell(self, data):
        # cell_format = cell_format()
        self.worksheet.write(self.current_row, self.current_col, data)
        self.current_col += 1

    # def cell_format(self):
    #     cell_format = workbook.add_format({"bold": True, "font_color": "red"})
    #     return cell_format

    def add_row(self, data_array):
        self.worksheet.write_row(self.current_row, self.current_col, data_array)
        self.current_row += 1
        self.current_col = 0

    def add_dataframe(self, dataframe):
        pass


def test():
    write_excel = WriteExcel2()
    write_excel.create_file("excel_stuff/MyFile.xlsx", "oooga booga")
    write_excel.add_cell("Hi")
    write_excel.add_row(["ab", "cd", "ef", "g", "h"])
    write_excel.add_row(["a", "b", "c", "d", "e"])
    for i in range(100):
        write_excel.add_row(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])


if __name__ == "__main__":
    test()

# import libraries
# from utilities.excel_utilities import Xlutils
import pandas as pd


class DataProviders:
    # file_path = "../testdata/test_data.xlsx"
    # xl = Xlutils(file_path)

    # for more than one rows
    # def get_test_data(self, sheet) -> list[dict[Any, Any]]:
    #     rows = self.xl.get_row_count(sheet)
    #     cols = self.xl.get_column_count(sheet)
    #     final_list = []
    #     for row in range(2, rows+1):
    #         data_dict = {}
    #         for col in range(1, cols+1):
    #             colnames = self.xl.get_data(1, col, sheet)
    #             data = self.xl.get_data(row, col, sheet)
    #             data_dict[colnames] = data
    #         final_list.append(data_dict)
    #     return final_list

    # return dictionary just for single row
    # def get_test_data(self, sheet):
    #     rows = self.xl.get_row_count(sheet)
    #     cols = self.xl.get_column_count(sheet)
    #     data_dict = {}
    #     for row in range(2, rows + 1):
    #         for col in range(1, cols + 1):
    #             colnames = self.xl.get_data(1, col, sheet)
    #             data = self.xl.get_data(row, col, sheet)
    #             data_dict[colnames] = data
    #     return data_dict

    # @staticmethod
    # def get_test_data(file_path, sheet):
    #     xl = Xlutils(file_path)
    #     rows = xl.get_row_count(sheet)
    #     cols = xl.get_column_count(sheet)
    #     data_dict = {}
    #     for row in range(2, rows + 1):
    #         for col in range(1, cols + 1):
    #             colnames = xl.get_data(1, col, sheet)
    #             data = xl.get_data(row, col, sheet)
    #             data_dict[colnames] = data
    #     return data_dict

    @staticmethod
    def get_test_data(file_path) -> dict:
        df = pd.read_csv(file_path)
        data_dict = {}
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                data_dict[df.columns[col]] = df.values[row][col]
        return data_dict

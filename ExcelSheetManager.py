import pandas as pd
import os

class DealingWithExcel:
    def __init__(self, file_path):
        self.__WindowsSet = set()
        self.__file_path = file_path

    def addNewWindow(self, title):
        self.__WindowsSet.add(title)

    def writeOnExcel(self, column_name="Used Windows"):
        df = pd.DataFrame(sorted(self.__WindowsSet), columns=[column_name])

        # Check if the directory exists
        directory = os.path.dirname(self.__file_path)
        if not os.path.exists(directory):
            print("The specified directory does not exist.")
            return

        try:
            df.to_excel(self.__file_path, index=False)
            print(f"{self.__file_path} has been written.")
        except Exception as e:
            print(f"An error occurred while writing to Excel: {e}")

# Example usage
if __name__ == "__main__":
    excel_handler = DealingWithExcel()
    excel_handler.addNewWindow("Google Chrome")
    excel_handler.addNewWindow("Visual Studio Code")
    excel_handler.addNewWindow("Microsoft Word")
    excel_handler.writeOnExcel()

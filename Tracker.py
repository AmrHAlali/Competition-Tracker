import pygetwindow as gw
import time
from Time import TimeManager
from ExcelSheetManager import DealingWithExcel
from pathlib import Path

def get_active_window_title():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            return active_window.title
        else:
            return None
    except Exception as e:
        print(f"Error getting active window: {e}")
        return None

def track_active_window(interval=0.1):
    last_window_title = None
    timeManager = TimeManager()
    timeManager.timeManager()

    current_directory = Path(__file__).parent
    excel_file = current_directory / 'Desktop' / f'{timeManager.name} - Used Windows During Competition.xlsx'
    excelManager = DealingWithExcel(str(excel_file))

    while True:
        if not timeManager.isAvailable():
            excelManager.writeOnExcel()
            print("Competition time is over, finalizing data...")
            break

        current_window_title = get_active_window_title()
        if current_window_title and current_window_title != last_window_title:
            print(f"Active window changed: {current_window_title}")
            excelManager.addNewWindow(current_window_title)
            last_window_title = current_window_title

        time.sleep(interval)

if __name__ == "__main__":
    track_active_window()

from datetime import datetime, timedelta

class TimeManager:
    def __init__(self):
        self.__endTime = None

    def timeManager(self):
        # timeToBegin = input("Start Time (HH:MM): ")

        timeFormat = "%H:%M"
        startTime = datetime.now()
        print("Welcome to Competition Tracker Program!")
        print("Note: This Program Can Record All Programs And Tabs That Used During The Competition!")
        self.name = input("Enter Your Full Name: ")
        durationMinutes = int(input("Enter The Duration Of The Competition (Minutes): "))

        endTime = startTime + timedelta(minutes=durationMinutes)

        start_time_only = startTime.time()
        self.__endTime = endTime.time()
        print(f"The Competition Will End in: {self.__endTime}")


    def isAvailable(self):
        return datetime.now().time() < self.__endTime
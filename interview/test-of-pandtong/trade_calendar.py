import csv


class Calendar:
    def __init__(self, csvFile="./data/calendar.csv"):
        self.csvFile = csvFile
        self.data_dict = {}
        with open(csvFile, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data_dict[row['date']] = bool(int(row['isTrading']))

    def isTrading(self, calendar_date):
        """
        isTrading return if calendar date is trading date or not
        :param calendar_date: YYYY-MM-DD format date e.g. "2011-01-03"
        :return: true or false
        """
        return self.data_dict.get(calendar_date, None)

    def getPrevTradingDate(self, calendar_date):
        """
        getPrevTradingDate return the previous trading date before calendar_date
        :param calendar_date: YYYY-MM-DD format date e.g. "2011-01-03"
        :return: previous trading date,YYYY-MM-DD format
        """
        rst_date = ''
        message = f"can't find the PrevTradingDate of {calendar_date} in {self.csvFile} file. "
        for date, is_trading in self.data_dict.items():
            if is_trading:
                rst_date = date
            if date == calendar_date:
                break
        else:
            return message
        return rst_date if rst_date else message

    def getNextTradingDate(self, calendar_date):
        """
        getNextTradingDate return the next trading date after calendar_date
        :param calendar_date: YYYY-MM-DD format date e.g. "2011-01-03"
        :return: next trading date,YYYY-MM-DD format
        """
        rst_date = ''
        message = f"can't find the NextTradingDate of {calendar_date} in {self.csvFile} file. "
        flag = False
        for date, is_trading in self.data_dict.items():
            if date == calendar_date:
                flag = True
            if flag and is_trading:
                return date
        else:
            return message


if __name__ == "__main__":
    calendar = Calendar("/tmp/calendar.csv")
    print(calendar.isTrading("2011-01-03"))
    print(calendar.getPrevTradingDate("2011-01-08"))
    print(calendar.getNextTradingDate("2011-01-04"))

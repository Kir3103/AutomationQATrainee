from DateUtils import DateUtils
from LogerUtils import Logger


class LeapYearUtils:

    @staticmethod
    def get_sum_days():
        year = int(DateUtils.get_current_date().replace('/', ' ').split()[2])
        day = int(DateUtils.get_current_date().replace('/', ' ').split()[1])
        month = DateUtils.get_current_date().replace('/', ' ').split()[0]
        month_to_compare = ''
        if month[0] == '0':
            month_to_compare += month[1:]
        else:
            month_to_compare += month

        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        Logger.info('Get the sum of the number of days in the year on the current date')
        return sum(month_days[:(int(month_to_compare) - 1)]) + day

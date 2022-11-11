from datetime import datetime
from LogerUtils import Logger
from Models.DateModel import DateModel


class DateUtils:

    @staticmethod
    def get_current_date_time_month():
        Logger.info('Get month, day, year, hours and minutes from module "datetime" '
                    'and convert to compare view')
        current_datetime = datetime.now()

        month = current_datetime.strftime('%B')
        day = str(current_datetime.day)
        year = current_datetime.strftime('%Y')
        hours = current_datetime.time().strftime('%I')
        hours_to_compare = ''
        if hours[0] == '0':
            hours_to_compare += hours[1:]
        else:
            hours_to_compare += hours
        minutes = current_datetime.time().strftime('%M')
        hours_minutes = hours_to_compare + ':' + minutes
        pm_or_am = current_datetime.strftime('%p')
        Logger.info('Get all values from "datetime" after convert to DateModel')
        current_value_to_model = DateModel(month, day, year, hours_minutes, pm_or_am)
        return current_value_to_model

    @staticmethod
    def get_current_date():
        Logger.info('Get month, day and year from module "datetime"')
        current_datetime = datetime.today().strftime("%m/%d/%Y")
        return current_datetime

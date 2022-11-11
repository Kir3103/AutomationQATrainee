class DateModel:

    def __init__(self, month, day, year, hours_minutes, pm_or_am):
        self.__month = month
        self.__day = day
        self.__year = year
        self.__hours_minutes = hours_minutes
        self.__pm_or_am = pm_or_am

    def __eq__(self, other):
        return (self.__month, self.__day, self.__year, self.__hours_minutes, self.__pm_or_am) == \
               (other.__month, other.__day, other.__year, other.__hours_minutes, other.__pm_or_am)

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, another_month):
        self.__month = another_month

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, another_day):
        self.__day = another_day

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, another_year):
        self.__year = another_year

    @property
    def hours_minutes(self):
        return self.__hours_minutes

    @hours_minutes.setter
    def hours_minutes(self, another_hours_minutes):
        self.__hours_minutes = another_hours_minutes

    @property
    def pm_or_am(self):
        return self.__pm_or_am

    @pm_or_am.setter
    def pm_or_am(self, another_pm_or_am):
        self.__pm_or_am = another_pm_or_am

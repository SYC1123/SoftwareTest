def predate(date):
    '''
    计算前一天
    :param date: （string）日期
    :return:
    '''
    bigmonth = (1, 3, 5, 7, 8, 10, 12)
    smallmonth = (4, 6, 9, 11)
    monthlist = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    isleapyear = False
    before = None
    if len(date) != 8:
        print('您的日期格式输入不合法')
    else:
        year = date[0:4]
        month = date[4:6]
        day = date[6:]
        if year.isdigit() and month.isdigit() and day.isdigit():
            year = int(year)
            month = int(month)
            day = int(day)
            if 1000 <= year <= 2019:
                if 1 <= month <= 12:
                    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):  # 闰年
                        isleapyear = True
                        monthlist[2] = 29
                    if 1 <= day <= monthlist[month]:
                        if day > 1:  # 不是1号
                            before = str(year) + str(month).zfill(2) + str(day - 1)
                            print(before)
                        else:  # 是1号 换月份
                            if month > 1:  # 不是1月
                                month = month - 1
                                if month in bigmonth:  # 大月
                                    before = str(year) + str(month).zfill(2) + '31'
                                    print(before)
                                elif month in smallmonth:  # 小月
                                    before = str(year) + str(month).zfill(2) + '30'
                                    print(before)
                                else:  # 2月
                                    if isleapyear:  # 闰年
                                        before = str(year) + '02' + '29'
                                        print(before)
                                    else:
                                        before = str(year) + '02' + '28'
                                        print(before)
                            else:  # 是1月 换年份
                                before = str(year - 1) + '12' + '31'
                                print(before)
                    else:
                        print('请输入合理的天数')
                else:
                    print('请输入在1月到12月之间的月份')
            else:
                print('请输入在1000年到2019年之间的年份')
        else:
            print('请输入正确的数字日期')


if __name__ == '__main__':
    date = input('请输入输入1000年到2019年之间的某个日期')
    predate(date)

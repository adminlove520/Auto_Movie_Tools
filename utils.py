from datetime import datetime, timedelta

def getDayHowWeek():
    """
    获取当前日期是第几周
    :return:
    """
    begin = datetime.now().replace(day=1).strftime("%W")
    end = datetime.now().strftime("%W")

    return int(end) - int(begin) + 1

def getNextMonday():
    today = datetime.now()
    days_until_next_monday = (7 - today.weekday()) % 7
    nextMonday = today + timedelta(days=days_until_next_monday)
    return nextMonday

def isInNextWeek(text_date):
    if text_date[-1] != "日":
        text_date += '1日'
    date = datetime.strptime(text_date, '%m月%d日')
    now = datetime.now()
    if date.month >= now.month:
        date = date.replace(year=now.year)
    else:
        date = date.replace(year=now.year + 1)

    next_monday = getNextMonday()
    days_until_date = (date - next_monday).days
    return 0 <= days_until_date < 7

def isNextMonth(text_date):
    if text_date[-1] != "日":
        text_date += '1日'
    try:
        date = datetime.strptime(text_date, '%Y年%m月%d日')
    except ValueError:
        date = datetime.strptime(text_date, '%m月%d日')
    now = datetime.now()
    next_month = now.month + 1
    if next_month > 12:
        next_month = 1
    return date.month == next_month and date.year == now.year

# # 测试代码
# print(getDayHowWeek())
# print(isInNextWeek('12月31日'))
# print(isNextMonth('12月31日'))
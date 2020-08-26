from datetime import date, timedelta
import corona_data

now = date.today()
now_str = now.strftime("%Y%m%d")
print(now_str)
#print(now.strftime("%Y%m%d"))

data = corona_data.get_corona_data(now_str,now_str)
# print(data)
if data == False:
    yesterday = now - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    print(yesterday_str)
    data = corona_data.get_corona_data(yesterday_str, now_str)
    print(data)
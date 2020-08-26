from flask import Flask, render_template
import corona_data
from datetime import date, time
from datetime import date, timedelta


#앱 생성
app = Flask(__name__)

#url 라우터
@app.route('/')
def index():

    ### data 불러오기
    now = date.today()
    now_str = now.strftime("%Y%m%d")
    #print(now_str)
    #print(now.strftime("%Y%m%d"))
    # Today data
    data = corona_data.get_corona_data(now_str,now_str)
    # print(data)
    # If today data doesn't exist
    # get yesterday data
    if data == False:
        yesterday = now - timedelta(days=1)
        yesterday_str = yesterday.strftime("%Y%m%d")
        #print(yesterday_str)
        data = corona_data.get_corona_data(yesterday_str, now_str)
        #print(data)

    #area_data = corona_data.get_corona_data()
    
    return render_template('index.html', data = data[1:-1], timedata = [now_str, now_str])

if __name__ == "__main__":
    app.run(debug=True)
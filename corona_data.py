import requests
import xmltodict
import json
from pprint import pprint

def get_corona_data(startCreateDt, endCreateDt):
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params = {
        'serviceKey':'1Ro51Bxc4safzDwOJnMYOySA535kHJ3kPZq3e/amuRVWmC682LZNpFQLMt+ms/tNINZeYdRD/ZhyE9IDn8Fc1g==',
        'pageNo':'1',
        'numOfRows':'10',
        'startCreateDt': startCreateDt, #'20200410',
        'endCreateDt': endCreateDt, #'20200410',
    }

    res = requests.get(url, params=params)
    #print(res.url)
    #print(res.text)
    dict_data = xmltodict.parse(res.text)
    #print(data)

    #dict to json
    json_data = json.dumps(dict_data)
    #print(json_data)

    #json to dict
    dict_data = json.loads(json_data)

    #print(dict_data)
    #print(dict_data['response']['header']['resultCode'])
    #print(dict_data['response']['body']['items']['item'])

    # totalCount로 제대로 데이터가 가져와졌는지 확인하기
    totalCount = dict_data['response']['body']['totalCount']
    #print("totalCount", totalCount)
    if totalCount == '0':
       #print("return")
        return False

    area_data = dict_data['response']['body']['items']['item']
    area_data.reverse()
    # for a in area_data:
    #     print(a)
    #print(area_data)
    #pprint(area_data)
    return area_data

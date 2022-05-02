import jwt   # PyJWT 
import uuid
import apiKey as KEY
import requests
import pandas as pd

payload = {
    'access_key': KEY.access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, KEY.secret_key)
authorization_token = 'Bearer {}'.format(jwt_token)


url = "https://api.upbit.com/v1/candles/minutes/15"

# 가져올 날짜의 수
num = 200 #최대

querystring = {"count" : num,  # 지정한 개수의 데이터
                 "market" : "KRW-BTC",   # 비트코인 한화 가격
                 "to" : "2022-04-05 07:45:00"}    # 언제까지의 데이터를 가져오겠다
                 

response = requests.request("GET", url, params=querystring)

# 데이터를 저장할 CSV 파일
csv_file = open("chart_data.csv", "a", newline="")
#csv_file = open("chart_data_rare.csv", "a", newline="")

df = pd.read_json(response.text)

df1 = df.rename(columns={'candle_date_time_kst':'time', 'opening_price':'open', 'high_price':'high', 'low_price':'low', 'trade_price':'close', 'candle_acc_trade_volume':'volume'})
df2 = df1.loc[:, ['time', 'open', 'high', 'low', 'close', 'volume']]
df2.to_csv(csv_file, sep = ',', na_rep = 'NaN')
"""
df.to_csv(csv_file, sep = ',', na_rep = 'NaN')
"""
import json
import pymysql

json_data= open("stock_market_data.json").read()
json_obj = json.loads(json_data)
con= pymysql.connect(host="localhost",user="root",password="",db="json")

cursor = con.cursor()

for item in json_obj:
    date = item.get("date")
    trade_code = item.get("trade_code")
    high = item.get("high")
    low = item.get("low")
    openn = item.get("open")
    close = item.get("close")
    volume = item.get("volume")
    cursor.execute("insert into demofrontend_value(date,trade_code,high,low,openn,close,volume) value(%s,%s,%s,%s,%s,%s,%s)",(date,trade_code,high,low,openn,close,volume))
    
con.commit()
   
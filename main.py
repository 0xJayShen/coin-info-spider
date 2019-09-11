# -*- coding: utf8 -*-
# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup


def get_coin_info(coin_name, start_date, end_date):
    response = requests.get(
        url="https://coinmarketcap.com/zh/currencies/{}/historical-data/?start={}&end={}".format(coin_name, start_date,
                                                                                                 end_date))
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.table.tbody.find_all('tr')
    for i in body:
        temp = i.find_all("td")
        date = temp[0].text
        start_price = temp[1].text
        max_price = temp[2].text
        min_price = temp[3].text
        close_price = temp[4].text
        trading_volume = temp[5].text
        market_value = temp[6].text
        print('币种:{} 日期:{} 开盘价:{} 最高价:{} 最低价:{} 收盘价:{} 成交量:{} 市值:{}'.format(
            coin_name, date, start_price, max_price,
            min_price, close_price, trading_volume, market_value))

# example:
get_coin_info("bitcoin", "20190905", "20190909")

from bs4 import BeautifulSoup
import requests


api_url = 'https://www.time.ir/'

def get_date():
    response = requests.get(api_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #----------------------------------------------------------------------------------------------------------------
    varShowTodayFull = soup.find(id='ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsiNumeral').text
    """
    ۱۴۰۱/۰۱/۰۷
    """
    #----------------------------------------------------------------------------------------------------------------
    varShowTodayFullCar = soup.find(id='ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsi').text
    """
    یکشنبه - ۷ فروردین ۱۴۰۱
    """
    #----------------------------------------------------------------------------------------------------------------
    varShowDateInt = varShowTodayFull.split('/')
    """
    "۱۴۰۱",
    "۰۱",
    "۰۷"
    """
    #----------------------------------------------------------------------------------------------------------------
    date_splited = varShowTodayFullCar.split(' ')
    """
     "یکشنبه",
    "-",
    "۷",
    "فروردین",
    "۱۴۰۱"
    """
    #----------------------------------------------------------------------------------------------------------------
    m = int(varShowDateInt[1])
    d = int(varShowDateInt[2])


    left = 1
    if (m<=4) and (d<10):
        left += (31*(3-m)) + 10 + (31-d)
    else:
        left += (31*3) + 10
        if((6-m)>=0):
            left += (6-m)*31 + 5 * 30 + 29 + (31-d)
        else:
            if(m == 12):
                left += (29-d)
            else:
                left += (11-m) * 30 + 29 + (30-d)
    #----------------------------------------------------------------------------------------------------------------
    left_days = left
    left_week = (left // 7)
    date = {
    'today' : varShowTodayFullCar,
    'day' : left_days,
    'week' : left_week,

    }

    return date

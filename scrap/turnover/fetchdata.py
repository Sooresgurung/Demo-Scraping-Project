from selenium import webdriver
from django.http import JsonResponse
from .models import ScrapData

def get_data_url():

    try:
      
        driver = webdriver.Chrome()
        driver.get("https://merolagani.com/MarketSummary.aspx?type=turnovers")
        
        symbol_list = []
        turnover_list = []
        ltp_list = []
        change_list = []
        high_list =[] 
        low_list=[]
        open_list=[] 
        qty_list =[]

        symbol = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[1]')
        for name in symbol:
            symbol_list.append(name.text)

        turnover = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[2]')
        for name in turnover:
            turnover_list.append(name.text)

        ltp = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[3]')
        for name in ltp:
            ltp_list.append(name.text)

        change = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[4]')
        for name in change:
            change_list.append(name.text)

        high = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[5]')
        for name in high:
            high_list.append(name.text)

        low = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[6]')
        for name in low:
            low_list.append(name.text)

        open = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[7]')
        for name in open:
            open_list.append(name.text)

        qty = driver.find_elements('xpath','//table[@class="table table-striped table-hover table-index"]/tbody/tr/td[8]')
        for name in qty:
            qty_list.append(name.text)
        
        for symbol, turnover, ltp, change, high, low, open, qty in zip(symbol_list, turnover_list, ltp_list, change_list, high_list, low_list, open_list, qty_list):
                
                ScrapData.objects.get_or_create(
                    symbol = symbol,
                    turnover = turnover,
                    ltp = ltp,
                    change = change,
                    high = high,
                    low = low,
                    open = open,
                    qty = qty
                )      
    except Exception as error:
        print(error)
        return JsonResponse({"error":error})
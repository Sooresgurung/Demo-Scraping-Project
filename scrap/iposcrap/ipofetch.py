from django.http import JsonResponse
from .models import ScrapIpo
from selenium import webdriver

def get_data_ipo():
    try:
        driver = webdriver.Chrome()

        driver.get("https://www.sharesansar.com/upcoming-issue")
       
        data_dict = {
            "symbol_list" : [],
            "company_list" : [],
            "sector_list" : [],
            "units_list" : [],
            "amount_list" : [],
            "application_date_list" : [],
            "date_of_sebon_list" : [],
            "issue_manager_list" : [],
            "remark_list" : [],

        }

        symbol = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[2]')
        for name in symbol:
            data_dict['symbol_list'].append(name.text)

        company = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[3]')
        for name in company:
            data_dict['company_list'].append(name.text)

        sector = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[4]')
        for name in sector:
            data_dict['sector_list'].append(name.text)

        units = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[5]')
        for name in units:
            data_dict['units_list'].append(name.text)

        amount = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[6]')
        for name in amount:
            data_dict['amount_list'].append(name.text)

        application_date = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[7]')
        for name in application_date:
            data_dict['application_date_list'].append(name.text)

        date_of_sebon = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[8]')
        for name in date_of_sebon:
            data_dict['date_of_sebon_list'].append(name.text)

        issue_manager = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[9]')
        for name in issue_manager:
            data_dict['issue_manager_list'].append(name.text)

        remark = driver.find_elements('xpath','//table[@class="table table-hover table-striped table-bordered compact dataTable no-footer"]/tbody/tr/td[10]')
        for name in remark:
            data_dict['remark_list'].append(name.text)


        # for symbol in data_dict["symbol_list"]:
        #     print(symbol)

        for symbol, company, sectors, units, amount, application_date, date_of_sebon, issuse_manager,remark in zip(data_dict["symbol_list"], data_dict["company_list"], data_dict["sector_list"],data_dict["units_list"],data_dict["amount_list"],data_dict["application_date_list"],data_dict["date_of_sebon_list"],data_dict["issue_manager_list"],data_dict["remark_list"]):
                
                ScrapIpo.objects.get_or_create(
                    symbol = symbol,
                    company = company,
                    sectors = sectors,
                    units = units,
                    amount  = amount,
                    application_date = application_date,
                    date_of_sebon = date_of_sebon,
                    issue_manager = issuse_manager,
                    remark = remark
                )       
    except Exception as error:
        print(error)
        return JsonResponse({"error":error})
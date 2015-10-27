from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BeautifulSoup import BeautifulSoup
from dateutil import rrule, parser


def get_last_element(row, sep=","):
    for td in row.findAll('td'):
        text = td.find(text=True).strip()
        if len(text) > 0:
            last_item = text
    return last_item.replace(',', '') + sep


def parse_one_day(a_date, a_file, soup):
    table_data = soup.find(id="AllContent_ContentMain_ucMktStatCtl_tblMktStatsFirstSummary")
    if table_data is None:
        return
    a_file.write('\n')
    data_str = a_date + ","
    sum_all_product = table_data.find("a", attrs={'name': 'SUM OF ALL PRODUCTS'})
    row = sum_all_product.parent.parent.findNext('tr').findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr').findNext('tr').findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr').findNext('tr').findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr').findNext('tr').findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr').findNext('tr').findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr').findNext('tr').findNext('tr')
    last_item = get_last_element(row)
    data_str += last_item
    row = row.findNext('tr')
    last_item = get_last_element(row, '')
    data_str += last_item
    a_file.write(data_str)


def scrape_one_day(date, a_driver, output_file):
    #find the element CBOE market date input box.
    input_element = a_driver.find_element_by_id("AllContent_ContentMain_ucMktStatCtl_txtDate")

    # type in the search
    input_element.clear()
    input_element.send_keys(date)

    # submit the form
    input_element.submit()

    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(a_driver, 10).until(EC.title_contains("Daily Market Statistics"))

    html = a_driver.page_source
    soup = BeautifulSoup(html)

    parse_one_day(date, output_file, soup)


def get_all_dates_string_list(start_date, end_date):
    dates = list(rrule.rrule(rrule.DAILY,
                             dtstart=parser.parse(start_date),
                             until=parser.parse(end_date)))
    return map(lambda date: date.strftime('%m/%d/%Y'), dates)


def scrape_cboe_daily_volume(start_date, end_date, output_file):
    f = open(output_file, 'w')
    head_str = "Date," \
               "Sum_of_All_Products_Volume," \
               "Sum_of_All_Products_Open_Interest," \
               "Index_Options_Volume," \
               "Exchange_Traded_Products_Volume," \
               "Equity_Options_Volume," \
               "Equity_LEAPS_Volume," \
               "Equity_LEAPS_Open_Interest," \
               "Weeklys_Options_Volume," \
               "Weeklys_Options_Open_Interest"
    f.write(head_str)

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # go to the web page
    driver.get("http://www.cboe.com/data/mktstat.aspx")

    try:
        dates_cboe_formate = get_all_dates_string_list(start_date, end_date)

        for a_day in dates_cboe_formate:
            scrape_one_day(a_day, driver, f)

    finally:
        f.close()
        driver.quit()


scrape_cboe_daily_volume('7/1/2014', '9/30/2014', 'cboe_volume_2014q3.csv')
scrape_cboe_daily_volume('4/1/2014', '6/30/2014', 'cboe_volume_2014q2.csv')
scrape_cboe_daily_volume('1/1/2014', '3/31/2014', 'cboe_volume_2014q1.csv')

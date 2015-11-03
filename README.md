# scraper
Perry's Python Scraper for CBOE daily trading volume.

This program let you define a range of start and end date, use selenium to send each date into the page to get that day's
trading volume data, and then use BeautifulSoup to parse the data and write to a csv file.

In order to extract web data with Python, 2 steps need to be performed:

    Step 1: Get the html page that contains the data.
    Step 2: Parse the html page and extract the data you are interested in.

In this program, A Python library named Selenium is used to do step 1, and BeautifulSoup Library is used to do step 2.

More documentation can be found at these 2 sites:

    http://docs.seleniumhq.org/
    http://www.crummy.com/software/BeautifulSoup/bs4/doc/

Here is a brief discussion how the job is done.

(1) The data source Page:
    CBOE, The Chicago Board Option Exchange, provides its Market Statistics Summary Data through the following page.
        http://www.cboe.com/data/mktstat.aspx
    By default, this page provide the last trading day's market Statistics Summary Data; It also provide a input field that
    let you Select any date in the past to get that date's historical data, you must enter the date in the the format of
    mm/dd/yyyy.

    Apparently, if I want to get Q3 2015 trading data, from 07/01/2015 to 09/30/2015, entering the date one 
    by one manually is a tedious job.  That's why I wanted to write this Python program to do the job
    automatically.

(2) Pre-requirements to run the program:

    Python 2.7.3
    Selenium: Use command "pip install selenium" to install.
    BeautifulSoup: Use command "pip install beautifulsoup4" to install.

    I am also assuming that you have Firefox installed on the computer, Selenium can also control other popular
    browsers, like Google Chrome.  But in this program, only Firefox control code is implemented.

(3) Selenium is so easy to use that you only need the following 2 lines to start a Firefox browser and go to the CBOE page.

      driver = webdriver.Firefox()
      driver.get("http://www.cboe.com/data/mktstat.aspx")

Once the page is opened, use view page source in Firefox to find out that the date input box has Id
"AllContent_ContentMain_ucMktStatCtl_txtDate"

The following 4 line of code let you find the input field, clear it, and set a date.  After submit() is called, the page will refresh with data for that date.  This is how Selenium control the browser to automate the boring hand input.

    input_element = driver.find_element_by_id("AllContent_ContentMain_ucMktStatCtl_txtDate")
    input_element.clear()
    input_element.send_keys(date)
    input_element.submit()

(4) Now that you have the html page in the driver, you just need to pass it to BeautifulSoup parser.
    html = driver.page_source
    soup = BeautifulSoup(html)

    detailed parsing is in the parse_one_day() method.

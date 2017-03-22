Scraping assignment
===================

Your assignment is to finish building a scraper to pull down precinct-level results from the Chicago mayor's race in 2015. This is a real scraper we used for several projects at the Times!

You'll have several tasks:

  - Ensure your virtual environment is set up properly, with BeautifulSoup installed. You'll also have to install a library called requests, which you can do (from within your virtual environment) by typing `pip install requests`

  - Using the included `chicago_scraper.py` file, implement the `get_html()` function, which will get the HTML for [this page](http://www.chicagoelections.com/en/pctlevel3.asp?Ward=1&elec_code=9&race_number=10). Note that the function takes an argument, `ward`. You'll want to pass that along to the URL in the correct spot.

  - Next, implement the `get_table()` function. You'll want to bring the html into BeautifulSoup, then return the table that contains the result.

We'll discuss questions on Friday.

**Due**: Friday, April 7
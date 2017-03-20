import urllib2, csv
from bs4 import BeautifulSoup

########## CSV SETUP ##########

output_file = open('accidents.csv', 'w')
writer = csv.writer(output_file)

########## GET PAGE FROM INTERNET ##########

# The site we're scraping. This is represented as a string.
url = 'https://www.mshp.dps.missouri.gov/HP68/search.jsp'

# Now we're going to use a tool called urllib2 to retrieve the HTML for the site
html = urllib2.urlopen(url).read()

########## START SCRAPING WEBSITE ##########

soup = BeautifulSoup(html, "html.parser")

# Find the main table using the "class" attribute, represented as a dictionary
targeting_attributes = {'class': 'accidentOutput'}
accident_table = soup.find('table', targeting_attributes)

# Grab the rows from the table, represented as a list
row_list = accident_table.find_all('tr')

# Loop over each of the rows
for row in row_list:

    cell_list = row.find_all('td')

    data = [cell.text for cell in cell_list]

    writer.writerow(data)



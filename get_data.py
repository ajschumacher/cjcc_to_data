from bs4 import BeautifulSoup
import re
import HTMLParser
import codecs
import glob


def scraper(html_doc):
    # geolocator = Nominatim(country_bias="USA")
    soup = BeautifulSoup(html_doc)
    agency = soup.find(id="FacilityNameTextBox")['value']
    entry = {}
    final = {}
    classes = {}

    item = soup.find(id='FormView2')
    address = item.find(id='FormView2_AddressLabel').get_text()
    address = address.encode('ascii','ignore')
    phone = re.findall('<b>Phone No:</b>(.+?.)<br />',html_doc)
    if phone:
    	phone = phone[0].encode('ascii','ignore')
    else:
    	phone = ''
    fax = re.findall('<b>Fax No:</b>(.+?.)<br />',html_doc)
    if fax:
    	fax = fax[0].encode('ascii','ignore')
    else:
    	fax = ''
    website = re.findall('<b>Website: </b>(.+?.)<br />',html_doc)
    if website:
    	website = website[0].encode('ascii','ignore')
    else:
    	website = ''
    hours = item.find(id='FormView2_Hours_Of_ServicesLabel').get_text()
    hours = hours.encode('ascii','ignore')
    description = item.find(id='FormView2_Resource_DescriptionLabel').get_text()
    description = description.encode('ascii','ignore')
    #split these on commas
    parser = HTMLParser.HTMLParser()
    html_doc = parser.unescape(html_doc)
    lines = re.findall('<span id="FormView2_HTML_CodeLabel">(.+?.)</span>',html_doc)
    if lines:
        items = re.split("<br \> ",lines[0])
        for item in items:
            subfields = item.split('<b>')[1:]
            for sub in subfields:
                subfield = sub.split('</b>')
                name = subfield[0][0:-3].encode('ascii','ignore')
                things = subfield[1].rstrip('<br \>').encode('ascii','ignore').split(',')
                classes[name] = things
    else:
        classes = {'Category': '',
                   'Services': '',
                   'Program': '',
                   'Population': ''}

    # for field in item.find(id = 'FormView2_Special_Lng_ServiceLabel'):
    language = re.findall('<b>Special Language Services:</b>(.+?.)<br />',html_doc)
    if language: 
    	language = language[0].encode('ascii','ignore').split(', ')
    else: 
    	language = ''
    eligibility = re.findall('<b>Eligibility Criteria: </b>(.+?.)<br />',html_doc)
    if eligibility: 
    	eligibility = eligibility[0].encode('ascii','ignore')
    else: 
    	eligibility = ''
    docs = re.findall('<b>Documentation Needed: </b>(.+?.)<br />',html_doc)
    if docs: 
    	docs = docs[0].encode('ascii','ignore')
    else: 
    	docs = ''
    wheelchair = re.findall('<b>Wheel Chair Accessible</b> :(.+?.)<br />',html_doc)
    if wheelchair: 
    	wheelchair = wheelchair[0].encode('ascii','ignore')
    else: 
    	wheelchair = ''

    entry = {'Documentation Needed': docs, 'Eligibility': eligibility, 'Language': language, 'Wheelchair Access': wheelchair, 'Address': address, 'Phone': phone, 'Website': website, 'Hours': hours, 'Description' : description}
    final[agency] = dict(entry.items() + classes.items())
    return final

def org_from_filename(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        html_doc=f.read()
    return scraper(html_doc)

def reader_all():
    filenames=glob.glob('html/*')
    result=[]
    for index, filename in enumerate(filenames):
        print index, filename
        result.append(org_from_filename(filename))
    return result
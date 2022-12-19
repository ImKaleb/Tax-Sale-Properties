import requests
import csv

#############################################
# THESE ARE THE ONLY PARAMS YOU NEED TO SET #
#############################################
FILEPATH = 'C:\\tmp\\'                      #
FILENAME = 'results.csv'                    #
FULL_PATH = FILEPATH+FILENAME               #
#############################################


with requests.Session() as SESSION:
    print('\n\n-- SEARCHING FOR TAX SALE PROPERTIES --')
    URL = 'https://taxsales.lgbs.com/api/property_sales/?limit=10000'
    RESULTS = SESSION.get(URL)
    CONTENT = RESULTS.json()
    PROPERTY_LIST = CONTENT['results']
    print('\n\n-- PROPERTIES GATHERED --')
    print('\n\n-- WRITING RESULTS TO CSV FILE --')
    with open(FULL_PATH,'w')as FILE:
        WRITER = csv.writer(FILE)
        WRITER.writerow(PROPERTY_LIST[1].keys())
        for DICTIONARY in PROPERTY_LIST:
            WRITER.writerow(DICTIONARY.values())
        FILE.close()
    print(f'-- FINISHED WRITING "{FULL_PATH}" --')
    print('-- PROGRAM COMPLETE --')
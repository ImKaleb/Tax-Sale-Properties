import requests
import csv

#############################################
# THESE ARE THE ONLY PARAMS YOU NEED TO SET #
#############################################
FILEPATH = 'C:\\tmp\\'                      #
FILENAME = 'results.csv'                    #
FULL_PATH = FILEPATH + FILENAME             #
#############################################

def main():
    with requests.Session() as session:
        url = 'https://taxsales.lgbs.com/api/property_sales/?limit=10000'
        print('\n\n-- SEARCHING FOR TAX SALE PROPERTIES --')
        results = session.get(url)
        content = results.json()
        property_list = content['results']
        print('\n\n-- PROPERTIES GATHERED --')
        print('\n\n-- WRITING RESULTS TO CSV FILE --')
        write_to_csv(property_list, FULL_PATH)
        print(f'-- FINISHED WRITING "{FULL_PATH}" --')
        print('-- PROGRAM COMPLETE --')

def write_to_csv(property_list, full_path):
    with open(full_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(property_list[1].keys())
        for dictionary in property_list:
            writer.writerow(dictionary.values())

if __name__ == '__main__':
    main()

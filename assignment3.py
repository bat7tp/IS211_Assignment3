import argparse
import urllib.request
import re
import sys
import csv
# other imports go here


def downloadData(url):
    """Downloads the data"""
    #url = http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv--
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        print(data)
        return data

def check_for_image(data):
    total_counter = 0
    total_image_counter = 0
    for x in data.splitlines():
        total_counter += 1
        a = x.split(",")
        images = a[0]
        #print(images)
#use regex to identify image hits
        image_found = r'(jpeg|jpg|png|gif)$'
        if_image = re.search(image_found, a[0], re.IGNORECASE)
#keep track of how many hits are images
        if if_image:
            total_image_counter += 1
            #print(if_image)

    print(str(total_counter))
    print(str(total_image_counter))
#calculate how many (%) of total hits are images
    percentage = ((total_image_counter/total_counter)*100)
    print(str(percentage), "% of the results are image files.")

    return
#Use counters and regex to calculate how many hits there are for each browser
def popular_browser(data):
    internet_explorer_counter = 0
    safari_counter = 0
    chrome_counter = 0
    firefox_counter = 0
    alternate_counter = 0

    for x in data.splitlines():
        s_found = r'(safari)'
        if_safari = re.search(s_found, x, re.IGNORECASE)

        chrome_found = r'(chrome)'
        if_chrome = re.search(chrome_found, x, re.IGNORECASE)

        ie_found = r'(msie)'
        if_ie = re.search(ie_found, x, re.IGNORECASE)

        ff_found = r'(firefox)'
        if_ff = re.search(ff_found, x, re.IGNORECASE)

        if if_safari:
            safari_counter += 1
        elif if_chrome:
            chrome_counter += 1
        elif if_ie:
            internet_explorer_counter += 1
        elif if_ff:
            firefox_counter += 1
        else:
            alternate_counter += 1
#print out how many hits there were for each browser type
    print(str(safari_counter), "Safari hits")

    print(str(internet_explorer_counter), "Internet Explorer hits")

    print(str(chrome_counter), "Chrome hits")

    print(str(firefox_counter), "Firefox hits")

    print(str(alternate_counter), "All other hits")

    return


def main(url):
    print(f"Running main with URL = {url}...")
    web_info = downloadData(url)
    image_info = check_for_image(web_info)
    popular_browser(web_info)

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    

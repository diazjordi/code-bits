from bs4 import BeautifulSoup
import requests
import csv

yard_name = None
yard_address = None
yard_city = None
inv_url = None
prices_url = None
yard_code = None
yard_zipcode = None
yard_phone = None
yard_lat = None
yard_long = None

yards = [
    "https://locations.lkqpickyourpart.com/al/huntsville/6942-stringfield-rd-nw",
    "https://locations.lkqpickyourpart.com/ca/anaheim/1235-s.-beach-boulevard",
    "https://locations.lkqpickyourpart.com/ca/bakersfield/5311-s.-union-avenue",
    "https://locations.lkqpickyourpart.com/ca/bloomington/221-e.-santa-ana-avenue",
    "https://locations.lkqpickyourpart.com/ca/chula-vista/800-energy-way",
    "https://locations.lkqpickyourpart.com/ca/chula-vista/880-energy-way",
    "https://locations.lkqpickyourpart.com/ca/fontana/15228-boyle-avenue",
    "https://locations.lkqpickyourpart.com/ca/hesperia/11399-santa-fe-ave-east",
    "https://locations.lkqpickyourpart.com/ca/monrovia/3333-peck-road",
    "https://locations.lkqpickyourpart.com/ca/oceanside/2315-carpenter-road",
    "https://locations.lkqpickyourpart.com/ca/ontario/2025-s-milliken-ave",
    "https://locations.lkqpickyourpart.com/ca/riverside/3760-pyrite-street",
    "https://locations.lkqpickyourpart.com/ca/san-bernardino/434-e.-sixth-street",
    "https://locations.lkqpickyourpart.com/ca/santa-fe-springs/13780-imperial-highway",
    "https://locations.lkqpickyourpart.com/ca/stanton/8188-1/2-katella-avenue",
    "https://locations.lkqpickyourpart.com/ca/sun-valley/11201-pendleton-street",
    "https://locations.lkqpickyourpart.com/ca/thousand-palms/27600-sierra-del-sol",
    "https://locations.lkqpickyourpart.com/ca/victorville/17229-gas-line-road",
    "https://locations.lkqpickyourpart.com/ca/wilmington/1232-blinn-avenue",
    "https://locations.lkqpickyourpart.com/co/aurora/11602-e.-33rd-avenue",
    "https://locations.lkqpickyourpart.com/co/denver/6100-n.-federal-blvd",
    "https://locations.lkqpickyourpart.com/fl/bradenton/1880-63rd-avenue-east",
    "https://locations.lkqpickyourpart.com/fl/clearwater/12501-40th-street-north",
    "https://locations.lkqpickyourpart.com/fl/davie/4301-south-state-road-7",
    "https://locations.lkqpickyourpart.com/fl/daytona-beach/3157-w.-int'l-speedway-blvd.",
    "https://locations.lkqpickyourpart.com/fl/gainesville/8910-northwest-13th-street",
    "https://locations.lkqpickyourpart.com/fl/largo/11900-starkey-road",
    "https://locations.lkqpickyourpart.com/fl/orlando/9205-e.-colonial-drive",
    "https://locations.lkqpickyourpart.com/fl/tampa/5109-causeway-boulevard",
    "https://locations.lkqpickyourpart.com/fl/west-palm-beach/451-benoist-farms-road",
    "https://locations.lkqpickyourpart.com/ga/fayetteville/155-roberts-road",
    "https://locations.lkqpickyourpart.com/ga/savannah/1321-us-hwy-80-west",
    "https://locations.lkqpickyourpart.com/il/blue-island/2247-141st-street",
    "https://locations.lkqpickyourpart.com/il/chicago/3130-s.-st.-louis-ave.",
    "https://locations.lkqpickyourpart.com/il/chicago/4555-w.-north-avenue",
    "https://locations.lkqpickyourpart.com/il/chicago-heights/551-e.-lincoln-highway",
    "https://locations.lkqpickyourpart.com/il/rockford/601-harrison-avenue",
    "https://locations.lkqpickyourpart.com/il/washington-park/6111-bunkum-rd.",
    "https://locations.lkqpickyourpart.com/in/fort-wayne/4820-moeller-road",
    "https://locations.lkqpickyourpart.com/in/south-bend/1602-s.-lafayette-boulevard",
    "https://locations.lkqpickyourpart.com/ks/wichita/700-e.-21st-street-n.",
    "https://locations.lkqpickyourpart.com/md/baltimore/2801-hawkins-point-road",
    "https://locations.lkqpickyourpart.com/md/baltimore/6201-erdman-avenue",
    "https://locations.lkqpickyourpart.com/md/edgewood/1706-pulaski-highway",
    "https://locations.lkqpickyourpart.com/md/mount-airy/3923-twin-arch-road",
    "https://locations.lkqpickyourpart.com/mi/holland/11475-chicago-drive",
    "https://locations.lkqpickyourpart.com/mi/wayland/4676-division-ave-s",
    "https://locations.lkqpickyourpart.com/nc/charlotte/3900-chesapeake-drive",
    "https://locations.lkqpickyourpart.com/nc/clayton/2928-u.s.-70",
    "https://locations.lkqpickyourpart.com/nc/durham/1301-s.-miami-blvd.",
    "https://locations.lkqpickyourpart.com/nc/greensboro/100-ward-road",
    "https://locations.lkqpickyourpart.com/nc/greenville/4558-u.s.-13",
    "https://locations.lkqpickyourpart.com/oh/cincinnati/2040-east-kemper-road",
    "https://locations.lkqpickyourpart.com/oh/dayton/4283-n.-james-h.-mcgee-blvd",
    "https://locations.lkqpickyourpart.com/oh/toledo/6193-hagman-road",
    "https://locations.lkqpickyourpart.com/ok/oklahoma-city/900-s.-macarthur-blvd.",
    "https://locations.lkqpickyourpart.com/ok/tulsa/3112-n.-peoria-avenue",
    "https://locations.lkqpickyourpart.com/sc/greenville/1300-white-horse-road",
    "https://locations.lkqpickyourpart.com/sc/greer/13054-e.-wade-hampton-blvd.",
    "https://locations.lkqpickyourpart.com/sc/north-charleston/4646-rivers-avenue",
    "https://locations.lkqpickyourpart.com/tn/chattanooga/400-workman-road",
    "https://locations.lkqpickyourpart.com/tn/memphis/966-w.-mitchell-road",
    "https://locations.lkqpickyourpart.com/tn/nashville/2030-lucas-lane",
    "https://locations.lkqpickyourpart.com/tx/austin/7900-s.-congress-avenue",
    "https://locations.lkqpickyourpart.com/tx/houston/1100-northville-street",
    "https://locations.lkqpickyourpart.com/tx/houston/12575-hiram-clarke",
    "https://locations.lkqpickyourpart.com/tx/houston/9314-wallisville-road",
    "https://locations.lkqpickyourpart.com/wi/milwaukee/6102-s.-13th-street",
]

with open('yards.csv','w',newline='') as new_file:
    csv_writer = csv.writer(new_file, delimiter=',')
    csv_writer.writerow(["yard_name","yard_address","yard_city","yard_zipcode","yard_phone","yard_lat","yard_long","yard_code","inv_url","prices_url"])
    yard_info = []
    for yard in yards:
        # go to homepage
        page = requests.get(yard)
        soup = BeautifulSoup(page.content, "html.parser")

        # find inv & prices url
        inv_url = soup.find_all("a", class_='Product-link')[1]['href']
        prices_url = soup.find_all("a", class_='Product-link')[2]['href']

        # go to inv url and find yard info
        page = requests.get(inv_url)
        soup = BeautifulSoup(page.content, "html.parser")
        main_div = soup.find("div", class_="content-container content-container--location-feature")
        yard_name = main_div.findChild()['data-location-name']
        yard_address = main_div.findChild()['data-location-address']
        yard_city = main_div.findChild()['data-location-city']
        yard_zipcode = main_div.findChild()['data-location-zip']
        yard_phone = main_div.findChild()['data-location-phone']
        yard_lat = main_div.findChild()['data-location-lat']
        yard_long = main_div.findChild()['data-location-lng']
        yard_code = main_div.findChild()['data-location-code']


        """     print(yard_name)
            print(address)
            print(yard_city)
            print(zipcode)
            print(phone)
            print(lat)
            print(lng)
            print(yard_code) """
            
        yard_info = [yard_name, yard_address, yard_city, yard_zipcode, yard_phone, yard_lat, yard_long, yard_code,inv_url,prices_url]
        print(f"Current Yard: {yard_name}")
        csv_writer.writerow(yard_info)


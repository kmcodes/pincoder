# pip install geopy==2.2.0
import geopy
import csv

def get_pin_code(lat=None, longitude=None):
    geolocator = geopy.Nominatim(user_agent="check_1")
    location = geolocator.reverse((lat, longitude),timeout=None)
    try:
        postcodes =  (location.raw['address']['postcode'])
    except:
        print(None)
        postcodes = ""
    return postcodes

output_list = []
with open('output_csv.csv','w') as out_file:
    writer = csv.writer(out_file)
    with open('input_csv.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        line_count = 0
        row_output=[]
        for row in csv_reader:            
            print(line_count)
            line_output = []
            if line_count==0:
                pass
                line_count+=1
            else:
                a = get_pin_code(lat=row[0],longitude=row[1])
                line_count+=1
                line_output.append(row[0])
                line_output.append(row[1])
                line_output.append(a)
                row_output.append(line_output)
        writer.writerows(row_output)

                




import csv
import re

def import_from_csv(file_path):
    result_data = {}
    if re.match(r'.*\.csv', file_path):
        with open(file_path) as csv_file:
            next(csv_file, None)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if not row:
                    
                    continue
                else:
                    full_name = str(row[0])+' '+str(row[1])
                    if full_name in result_data:
                        result_data[full_name].append([row[2], row[3]])
                    else:
                        result_data.update({full_name: [[row[2], row[3]]]})
        return result_data
    else:

        print('Wrong file type')
        return ('Wrong file type')






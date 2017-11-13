import csv, math, re, datetime

#1. 

def transform_spec_data(fname):
    """
    Transforms and applies specifications to input file. 

    >>>transform_spec_data(example_input.txt)
    
    """ 

    with open(fname, 'rb') as input_file: #read from this file 
        data = csv.reader(input_file, delimiter=' ', quoting=csv.QUOTE_NONE) #get data from input file
        with open('output.csv', 'w') as output_file: #write to this output file
            mywriter = csv.writer(output_file, escapechar=' ', quoting=csv.QUOTE_NONE) #create writer object
            mywriter.writerow(['Account Number','Read Date','Address','Zipcode','Consumption']) #add header to output
            seen = set() #keep track of duplicates
            for row in data:
                if tuple(row) in seen:
                    continue #ignore duplicates 
                seen.add(tuple(row)) #turn row into hashable/immutable tuple, so can add to set
                row[0] = row[0].zfill(6) #pad with leading zero's to ensure 6 digit account numbers.
                if len(row[0]) > 6: #make sure account number data is isolated 
                    fix_account_num(row) #function call to fix format 
                row = [x for x in row if x != ''] #remove empty fields 
                f_row = [] #create new row to append correct data format 
                date = datetime.datetime.strptime(" ".join(row[1:4]), "%b %d %Y").strftime("%Y%m%d") #use datetime to format  
                
                if re.search('[a-zA-Z]', row[8]): #regex search for alpha text in next column
                    address = (" ".join(row[4:9])).replace(',', '') #grab rest of address text
                    if re.search('[0-9]', address[-1]): #regex search for numbers in text ending 
                        address = address[:-5] #dont grab the the 5 digit zipcode 
                else: 
                    address = (" ".join(row[4:7]))
            
                zipcode = re.sub('[^0-9]','', (row[-2].zfill(5))) #regex to limit to numbers only 
                consumption = re.sub('[^0-9]','', (row[-1])) #regex used for numbers only 

                f_row.append(row[0])
                f_row.append(date)
                f_row.append(address)
                f_row.append(zipcode)
                f_row.append(consumption)

                mywriter.writerow(f_row) #add data to output file

def fix_account_num(row):
    """
    fix format of Account Number when it is more than 6 characters

    >>>fix_account_num( ['571872Mar', '15', '2017', '', '', '', '20', 'Amherst', 'Street', '', '', '', '', '', '1003', '', '', '', '', '', '113', '', ''])
    ['571872','Mar','15','2017', '', '', '20', 'Amherst', 'Street', '', '', '', '', '', '1003', '', '', '', '', '', '113', '', '']

    """
    account_num = row[0]
    row[0] = account_num[:5].rsplit(' ', 1)[0]
    day = row[1]
    if row[3] == '':
        row[3] = row[2]
        row[2] = day
    row[1] = account_num[6:]
    return row 

# call function:
transform_spec_data('example_input.txt')

#2. 

def standard_deviation(number_list):

    average = sum(number_list) / float(len(number_list))
    sqrd_distances = 0 
    for value in number_list:
        sqrd_distances += ((average - value)**2)
    stdev = math.sqrt(sqrd_distances / float(len(number_list))) #get square root of variance
    
    return stdev

    # The single issue was the iteration in the for loop was supposed to be adding up the squared differences, not the attempted standard deviation. 
    # The previous formula was equaling standard deviation as a sum of each individual value's variance, when it is supposed to be a square root of the total variance. 
    # Variance is calculated by taking the sum of the square of every value's difference from the average, then averaging it with the n value. 

# call function:
print standard_deviation([1,2,3,4,5])

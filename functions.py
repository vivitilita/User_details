import csv

def open_file(file_name):
    ''''This function will open, read and then append \n
    all the rows of a given file to a new list'''
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file) # read the csv file
        new_list = [] # create an empty list
        for line in csv_reader:
            new_list.append(line) # append the file rows to new_list
        return new_list

def transform_file(file_name):
    '''This function will process and extract data \n
    from the list created by the "open_file"'''
    user_details = open_file(file_name) # read the file using "open_file"
    new_list = [] # create an empty list

    for i in range(len(user_details)): # loop through the file data
        # set conditions for the first row of the list
        if i == 0: 
            new_list.append(["firstName","lastName","email"])
        else:
            email = user_details[i][-1].split('@')[0] # split the email column data
            # append the transformed data to new_list
            new_list.append([user_details[i][1],user_details[i][2],email]) 
    return new_list

def write_new_file(old_file, new_file):
    '''This function will create/write a new file taking data from old file \n
    and transformed by the "transform_file" method'''
    transformed_data = transform_file(old_file) # assign the variable to the new transformed data
    with open(new_file, 'w') as file:
        writer = csv.writer(file) 
        writer.writerows(transformed_data) # write on csv file the transformed_data

# return the new and the old file 
write_new_file('user_details.csv', 'new_user_details.csv')
### User_details.csv file processing

This is a project that reads a csv file (user_details.csv), processes the data from the file and writes the processed data to a new file:
- [x] 'transformed_user_details.csv' from the class_version.py code
- [x] 'new_user_details.csv' from the functions.py code 


The code is divided into three functions:

> ***open_file***: This function takes a file name as input, opens the file and reads it using the csv.reader() method. It then appends each line of the file to a new list and returns the new list.

> ***transform_file***: This function takes the list returned by open_file() and iterates over the elements of the list. It then takes the firstname, lastname, and email address of each element, and appends it to a new list. It returns this new list.

> ***write_new_file***: This function takes the new_file name and the list returned by transform_file(), opens the new file in write mode, writes the new list to the new file using csv.writer() and then closes the file.





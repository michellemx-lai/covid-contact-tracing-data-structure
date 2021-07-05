########################################################
# Part 2 - Parse Contact Tracing Data
########################################################
import csv 

def parse_contacts(filename):
    """ (str) -> dict
    
    Reads the contents of the given CSV file. Each row in the data file lists an infected person,
    who they were infected by, and the date on which they were infected. 

    Returns a dictionary of the following format {id : Infected_person-object, ...}, where:
    - each key, id, is a string representing a person’s id
    - each value is an object of type Infected_person

    If the data file is empty (i.e., has no rows), returns an empty dictionary.
    """

    parsed_data = {}

    #open the file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        #skip headers
        header = next(reader) 

        #create a key for each person in the first (id) column by looping through each row
        for row in reader: 
            
            infected_id = row[0]
            date = row[2]

            infected_person_object = Infected_person(infected_id, date)
            
            parsed_data.update({infected_person_object.id: infected_person_object})
        
    #open the file again
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        #skip headers
        header = next(reader) 

        #create a key for each person in the second (infected_by) column if they are not already in parsed_data 
        for row in reader:

            spreader_id = row[1]

            if spreader_id not in parsed_data:
                infected_person_object = Infected_person(spreader_id)
            
                parsed_data.update({infected_person_object.id: infected_person_object})
                
    #open the file again
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        #skip headers
        header = next(reader) 
    
        for row in reader:
            infected_id = row[0]
            spreader_id = row[1]
            date = row[2]
            
            #loop through all the keys in parsed_data, call infects() method 
            for id in parsed_data:
                if id == spreader_id:
                    parsed_data[id].infects(infected_id)
    
    #delete keys-value pairs that have any empty keys or values from parsed_data
    parsed_data_copy = dict(parsed_data) 
    for id in parsed_data_copy:
        if id == None or id == '' or parsed_data[id] == None or parsed_data[id] == '':
            del parsed_data[id]

    return parsed_data
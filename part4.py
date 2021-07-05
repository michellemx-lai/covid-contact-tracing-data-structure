########################################################
# Part 4 - Find Superspreading Dates
########################################################
def find_superspreading_date(parsed_data):
    """ (dict) -> (list, int) 

    Takes in a dictionary and identifies the superspreading date(s) for direct infections, 
    and how many infections occured on the superspreading date(s).
    
    Returns a tuple of the form ([date1,...], max-infected) where:

    - [date1,...] is a list of strings representing all superspreading dates, with no duplicates.

    - max_infected is the number of direct infections on any of the superspreading dates

    If the input dictionary is empty, returns the tuple ([], 0)
    """
    #initialize variables
    superspreading_date = []
    all_infection_dates = []
    max_infected = 0
    
    #loop over the keys in parsed_data 
    for id in parsed_data:
        
        #access the corresponding value and call infected_on method to find the date
        infection_date = parsed_data[id].infected_on
        
        #append all infection dates to our list except the unknowns
        if infection_date != "unknown":
            all_infection_dates.append(infection_date)
        
    for date in all_infection_dates:
        if date not in superspreading_date: 

            #the number of times the date appears in an Infected_person object is the number of people infected on that date
            num_infected = all_infection_dates.count(date)
            
            #check if the number of infections is higher or equal to the current highest 
            if num_infected > max_infected: 
                superspreading_date.clear()
                superspreading_date.append(date)
                max_infected = num_infected
            
            elif num_infected == max_infected:
                superspreading_date.append(date)
        
    return (superspreading_date, max_infected)
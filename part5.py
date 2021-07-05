########################################################
# Part 5 - Identify Top Direct + Indirect Superspreaders
########################################################

####
# 5a
####
def get_all_infected(parsed_data, person_id):
    """ (dict, str) -> list
    
    Takes in a dictionary with format {id : Infected_person-object, ...} and a string that represents a person's id, 
    finds all persons within the dictionary who was directly or indirectly infected by the person of interest.

    Returns a list of the ids of all persons (directly + indirectly) infected by the person of interest. 

    If dictionary is empty or person_id is not in dictionary, returns none.
    """
    #check if person_id is in parsed_data dictionary. If so, access its corresponding value
    #in the dictionary, call the infected method, and copy the infected list
    if person_id in parsed_data:
        all_infected = list(parsed_data[person_id].infected) #all_infected now contains all directly infected people

        for id in all_infected:
            all_infected.extend(parsed_data[id].infected) #extend all_infected list to include all indirectly infected people

        return all_infected

    #only return an empty list if person_id is not in parsed_data
    else:
        return []
    
####
# 5b
####
def find_top_direct_plus_indirect_superspreader(parsed_data):
    """
    (dict) --> (list, int)

    Takes in a dictionary with format {id : Infected_person-object, ...}
    Returns a tuple of the form ([id1, id2, ...], max_infection_count) where:
    - ([id1, id2, ...] is a list of person id’s corresponding to the top (direct + indirect) superspreader(s), with no duplicates.
    
    If called with an empty dictionary as argument, returns the tuple ([], 0).

    """

    #initialize variables
    max_infection_count = 0
    top_overall_superspreader = []
    
    #loop over keys in parsed_data dictionary
    for id in parsed_data:
        #call get_all_infected function to get list of all directly and indirectly infected people
        all_infected = get_all_infected(parsed_data, id) 
        
        #find the number of directly and indirectly infected people using len() method
        num_infected = len(all_infected)
        
        #check if number of total infections due to this person is higher than current highest
        if num_infected > max_infection_count:
            top_overall_superspreader.clear() #clear list since this is a new top superspreader
            top_overall_superspreader.append(id)
            max_infection_count = num_infected 
        
        elif num_infected == max_infection_count: #there is a tie between the superspreaders
            top_overall_superspreader.append(id) 
    
    return (top_overall_superspreader, max_infection_count)


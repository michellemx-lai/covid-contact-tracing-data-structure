########################################################
# Part 3 - Identify Top Direct Superspreaders
########################################################

def find_top_direct_superspreader(parsed_data):
    """ (dict) -> list

    Takes in a dictionary with format {id : Infected_person-object, ...}, identifies the id corresponding
    to the person who has infected the most people in the dictionary.
    Returns a list of ids corresponding to the top direct superspreader(s), in the format [id1, id2, ...]

    If the input is an empty dictionary, returns an empty list.
    """
    #initialize variables
    highest_num = 0
    top_direct_superspreader = []
    
    #loop over keys in parsed_data dictionary
    for id in parsed_data:

        #access the corresponding value of id, and call infected() to find length of infected list 
        num_infected = len(parsed_data[id].infected)
        
        #check if num_infected is greater than highest_num. If so, they are a superspreader
        if num_infected > highest_num:
            top_direct_superspreader.clear()
            top_direct_superspreader.append(id) 
            highest_num = num_infected
        
        #check if num_infected is equal to highest_num. If so, they are a tied superspreader 
        elif num_infected == highest_num:
            top_direct_superspreader.append(id)

    return top_direct_superspreader
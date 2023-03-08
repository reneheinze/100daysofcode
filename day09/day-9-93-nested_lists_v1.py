# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


#Nesting a dictionary and a list inside a dictionary
#I want to keep track of how many visits I´ve made to these citys.
# This creates the nested dictionary France and the dictionary cities_visited

cities_visited = {"France": {"Paris": 3,
                            "Berlin": 2,
                            "Hamburg": 3},
               
                 "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


#print(cities_visited)
#print(cities_visited["France"]["Paris"])

#In the below program, cities_visited is a nested dictionary. 
# The internal dictionary france is assigned to travel_log.
# Here, the dictionary has the key cities_visited and value the list of the cities.

# Now we have a dictionary of travel_log of all the countries that I have been to
# And each country has a value that is a dictionary in itself and can store multiple pieces of data

#dictionary = travel_log
#                   dictionary = france 
travel_log = {"France": {"cities_visited": ["Paris", "Lille", "Dijon"],
                              "france_key": ["france_value1", "france_value2"],
                              "total_visits": 12 },
               
              "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#print(travel_log)
#print(travel_log["France"])
#print(travel_log["Germany"])
#print(travel_log["France"]["cities_visited"][0])
#print(travel_log["France"]["france_key"])
#print(travel_log["France"]["total_visits"])



#dictionary = travel_log
#             dictionary = france 
#Nesting Directorys in a List
renes_travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 14
    }
]

print(renes_travel_log)
print(renes_travel_log[0]["cities_visited"])
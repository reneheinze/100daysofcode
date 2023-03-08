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

#Nesting a Dictionary in a Dictionary
# It does not really descripe what city.

travel_log_dic = {
    "France": {"Paris": 1,"Lille": 3,"Dijon": 2},
    "Germany": {"Berlin": 1,"Hamburg": 3,"Stuttgart": 2}, 
}

#print(travel_log_dic["Germany"]["Berlin"])

#Nesting Dictionary in a list

travel_log_ar = [
    {"country": "france",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "france_key": ["france_value1", "france_value2"],
     "total_visits": 12 },
               
    {"country": "germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5 },
]

print(travel_log_ar[0]["country"])
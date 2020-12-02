"""
This takes temperature of cities in 5 different days and cost of five hotels
to find the highest average temperature of a trip to each city in the dictionary and
plans hotels to stay at along the way to maximize your budget in this example of $850.
"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}

def temp_func(route):
    """This function takes permutations of possible routes of the trip in the dictionary database
    and returns the average temperature of that route"""
    temp = 0
    for i in range(len(route)):
        temp += city_temps[route[i]][i]
    return temp/days

def cost_func(hotels):
    """This function takes combinations of possible hotels for the trip in the dictionary database and
    returns the total cost to stay at those hotels"""
    return sum([hotel_rates[i] for i in hotels])


if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())

    days = len(city_temps)
    HOTEL_BUDGET = 850

    perms = list(permutations(city_temps, days))
    best = max([(temp_func(p), p) for p in perms])
    print(f'Here is your best route: {best[1]}\nthe average of the daily max temp. is {best[0]} degrees F')

    combs = list(combinations_with_replacement(hotel_rates, days))
    best_option = min(combs, key=lambda t: HOTEL_BUDGET - cost_func(t) if HOTEL_BUDGET >= cost_func(t) else HOTEL_BUDGET)
    print(f'To max out your hotel budget, stay at these hotels: {best_option},\ntotaling ${cost_func(best_option)}')

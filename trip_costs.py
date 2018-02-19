
def hotel_costs(nights):
    """per night the hotel costs 140$ """
    total_exp = 140*nights
    return total_exp

def plane_ride_costs(city):
    if city == "Charlotte":
        round_trip = 183
        return round_trip
    elif city == "Tampa":
        round_trip = 220
        return round_trip
    elif city == "Pittsburgh":
        round_trip = 222
        return round_trip
    elif city == "Los Angeles":
        round_trip = 475
        return round_trip
    else:
        return print("Please enter a valid destination")

def rental_car_cost(days):
    """per day cost of the rental car is 40$"""
    total_cost = 40 * days
    if days >= 7:
        """apply 50$ discount of the total cost"""
        total_cost = total_cost - 50
        return total_cost
    elif days >= 3:
        """apply 20$ discount of the total cost"""
        total_cost = total_cost - 20
        return total_cost
    return total_cost


def trip_costs(nights, days, city):
    hotel = hotel_costs(nights)
    place_to_visit = plane_ride_costs(city)
    rental_car = rental_car_cost(days)
    total_costs = hotel+place_to_visit+rental_car
    return print(total_costs)


trip_costs(2,3,"Tampa")


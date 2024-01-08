import random

attractions = ["Ferris Wheel", "Roller Coaster", "Haunted House", "Bumper Cars", "Merry-Go-Round"]
attraction_details = {
    "Ferris Wheel": {"capacity": 20, "current_visitors": 0, "ticket_price": 10.0},
    "Roller Coaster": {"capacity": 30, "current_visitors": 5, "ticket_price": 15.0},
    "Haunted House": {"capacity": 15, "current_visitors": 8, "ticket_price": 8.0},
    "Bumper Cars": {"capacity": 10, "current_visitors": 10, "ticket_price": 7.0},
    "Merry-Go-Round": {"capacity": 12, "current_visitors": 11, "ticket_price": 5.0}
}
visitors = {
    "Adrish": {"wallet": 69},
    "Adrish_v1": {"wallet": 25},
    "Adrish_v2": {"wallet": 30},
    "Adrish_v3": {"wallet": 10},
    "Adrish_v4": {"wallet": 8}
}

def sell_ticket(attraction_name, visitor_name):
    if attraction_details[attraction_name]["capacity"] > attraction_details[attraction_name]["current_visitors"]:
        if visitors[visitor_name]["wallet"] >= attraction_details[attraction_name]["ticket_price"]:
            visitors[visitor_name]["wallet"] -= attraction_details[attraction_name]["ticket_price"]
            attraction_details[attraction_name]["current_visitors"] += 1
            print(f"{visitor_name} bought a ticket for the {attraction_name}! Remaining balance: {visitors[visitor_name]['wallet']}")

        else:
            print(f"Sorry, {visitor_name} doesn't have enough funds to purchase a ticket for {attraction_name}.\n")

    else:
        print(f"Sorry, {attraction_name} is full. Try another attraction, {visitor_name}.")

def display_carnival_info():
    print("**Carnival Attractions:**")
    for attraction, details in attraction_details.items():
        print(f"- {attraction}: {details['current_visitors']} visitors out of {details['capacity']} capacity.")
    print('\n')

display_carnival_info()

def visitor_experience(visitor_name):
    chosen_attractions = random.sample(attractions, 2)
    for attraction in chosen_attractions:
        sell_ticket(attraction, visitor_name)

for visitor in visitors:
    print(f"{visitor}'s initial balance: {visitors[visitor]['wallet']}")

    visitor_experience(visitor)

    print(f"{visitor}'s final balance: {visitors[visitor]['wallet']}\n")

display_carnival_info()

from datetime import datetime, timedelta
import random 

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []
    
    tickets = set()
    while len(tickets) < quantity:
        tickets.add(random.randint(min, max))
    return sorted(tickets)

ticket_numbers=get_numbers_ticket(1,1000,5)

print("Generated ticket numbers:", ticket_numbers)





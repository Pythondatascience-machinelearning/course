from datetime import datetime, timedelta
import random 

def get_numbers_ticket(min, max, quantity):

    if min<1 or max>1000 or quantity !=6:
        return []
    
    else:
        tickets = set()
    while len(tickets) < quantity:
        i = random.randint(min, max)
        tickets.add(i)
    return sorted(tickets)

ticket_numbers=get_numbers_ticket(1,1000,6)

print(ticket_numbers)





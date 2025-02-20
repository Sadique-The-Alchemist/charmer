FRIENDS = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']

def call(id): 
    return FRIENDS[id]

def wish(id): 
    return f"Hello {FRIENDS[id].title()}!"
def replace(bunch, index, value): 
    bunch[index] = value 

def gather(group, person): 
    group.append(person) 

def ament(group, id): 
    del group[id] 

def kick(group, id): 
    kicked = group.pop(id) 
    return f"Hello Mr {kicked}! you got kicked out" 

def punch(group, person):
    group.remove(person) 
def invite(group, event):
    return f"Welcome {', '.join(group)} to our tradditional {event}"
def add_and_invite(group, new_group, event): 
    group.extend(new_group)
    return invite(group, event)
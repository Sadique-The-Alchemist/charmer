FRIENDS = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']

def call(id): 
    return FRIENDS[id]

def wish(id): 
    return f"Hello {FRIENDS[id].title()}!"
print(f"Hello {FRIENDS[1].title()}!")

from grove import call, wish, replace, gather, ament, kick, punch, invite, add_and_invite


def test_call():
    assert call(0) == 'lorem'
    assert call(1) == 'ipsum'
    assert call(2) == 'dolor'
    assert call(3) == 'sit'
    assert call(4) == 'amet'

def test_wish(): 
    assert wish(0) == "Hello Lorem!"
    assert wish(1) == "Hello Ipsum!"
    assert wish(2) == "Hello Dolor!"
    assert wish(3) == "Hello Sit!"
    assert wish(4) == "Hello Amet!"

def test_replace(): 
    bunch = ['apple', 'orange', 'grape']
    replace(bunch, 1, 'banana')
    assert bunch == ['apple', 'banana', 'grape']

def test_gather(): 
    group = []
    gather(group, 'person1')
    gather(group, 'person2')
    assert group == ['person1', 'person2']

def test_ament(): 
    group = ['apple', 'orange', 'grape'] 
    ament(group, 0)
    assert group == ['orange', 'grape'] 
def test_kick(): 
    group = ['apple', 'orange', 'grape'] 
    dialogue = kick(group, 2)
    assert group == ['apple', 'orange']
    assert dialogue == "Hello Mr grape! you got kicked out"
def test_punch(): 
    group = ['apple', 'orange', 'grape']
    punch(group, 'apple') 
    assert group == ['orange', 'grape']
def test_invite(): 
    group  = ['kattapa', 'ravu', 'karu'] 
    message = invite(group, 'dinner') 
    group = ', '.join(group)
    assert message == f'Welcome {group} to our tradditional dinner' 
def test_add_and_invite(): 
    group = ['kattapa', 'ravu', 'karu']
    new_group = ['zak', 'pavi', 'anu']
    message = add_and_invite(group,new_group, 'lunch')
    group  = ', '.join(group)
    assert message == f'Welcome {group} to our tradditional lunch'
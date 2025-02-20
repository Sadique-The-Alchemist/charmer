from grove import call, wish 


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


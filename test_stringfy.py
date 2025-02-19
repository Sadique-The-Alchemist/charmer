from stringfy import to_title, to_lower, to_upper 


def test_to_title(): 
    assert to_title("test to title") == "Test To Title" 
def test_to_lower(): 
    assert to_lower("TEST TO LOWER") == "test to lower" 

def test_to_upper(): 
    assert to_upper("test to upper") == "TEST TO UPPER"
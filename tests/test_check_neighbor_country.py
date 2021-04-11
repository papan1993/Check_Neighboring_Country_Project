from Check_Neighboring_Country_Library.NeighboringCountry_module import Neighbor_Country_class

##### ALl 10 test cases are written here including few critical ones

def test_function_1():
    url_1 = "https://en.wikipedia.org/wiki/Indonesia"
    url_2 = "https://en.wikipedia.org/wiki/China"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == False


def test_function_2():
    url_1 = "https://en.wikipedia.org/wiki/India"
    url_2 = "https://en.wikipedia.org/wiki/China"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == True


def test_function_3():
    url_1 = "https://en.wikipedia.org/wiki/India"
    url_2 = "https://en.wikipedia.org/wiki/Sri_Lanka"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == True


def test_function_4():
    url_1 = "https://en.wikipedia.org/wiki/Russia"
    url_2 = "https://en.wikipedia.org/wiki/India"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == False


def test_function_5():
    url_1 = "https://en.wikipedia.org/wiki/Canada"
    url_2 = "https://en.wikipedia.org/wiki/Germany"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == False


def test_function_6():
    url_1 = "https://en.wikipedia.org/wiki/Canada"
    url_2 = "https://en.wikipedia.org/wiki/United_States"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == True


def test_function_7():
    url_1 = "https://en.wikipedia.org/wiki/United_States"
    url_2 = "https://en.wikipedia.org/wiki/Mexico"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == True


def test_function_8():
    url_1 = "https://en.wikipedia.org/wiki/United_States"
    url_2 = "https://en.wikipedia.org/wiki/Germany"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == False


def test_function_9():
    url_1 = "https://en.wikipedia.org/wiki/Brazil"
    url_2 = "https://en.wikipedia.org/wiki/Argentina"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == True


def test_function_10():
    url_1 = "https://en.wikipedia.org/wiki/Algeria"
    url_2 = "https://en.wikipedia.org/wiki/Morocco"
    class_object = Neighbor_Country_class()
    assert class_object.is_neighboring_country(url_1, url_2) == True


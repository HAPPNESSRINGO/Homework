from ex4 import sort_by_profit


def test_sort_by_profit_empty_lists():
    products = []
    prices = []
    costs = []
    sort_by_profit(products, prices, costs)
    assert products == []
    assert prices == []
    assert costs == []

def test_sort_by_profit_single_element():
    products = ["Product1"]
    prices = [10.0]
    costs = [5.0]
    sort_by_profit(products, prices, costs)
    assert products == ["Product1"]
    assert prices == [10.0]
    assert costs == [5.0]

def test_sort_by_profit_multiple_elements1():
    products = ["Product1", "Product2", "Product3"]
    prices = [10.0, 20.0, 15.0]
    costs = [5.0, 10.0, 12.0]
    sort_by_profit(products, prices, costs)
    assert products == ["Product3", "Product1", "Product2"]
    assert prices == [15.0, 10.0, 20.0]
    assert costs == [12.0, 5.0, 10.0]
    
def test_sort_by_profit_multiple_elements2():
    products = ["Product1", "Product2", "Product3", "Product4"]
    prices = [10.0, 20.0, 15.0, 5.0]
    costs = [5.0, 10.0, 12.0, 3.0]
    sort_by_profit(products, prices, costs)
    print(products, prices, costs)
    assert products == ['Product4', 'Product3', 'Product1', 'Product2']
    assert prices == [5.0, 15.0, 10.0, 20.0]
    assert costs == [3.0, 12.0, 5.0, 10.0]

def test_sort_by_profit_negative_profit():
    products = ["Product1", "Product2", "Product3"]
    prices = [10.0, 5.0, 15.0]
    costs = [12.0, 10.0, 10.0]
    sort_by_profit(products, prices, costs)
    assert products == ["Product2", "Product1", "Product3"]
    assert prices == [5.0, 10.0, 15.0]
    assert costs == [10.0, 12.0, 10.0]

def test_sort_by_profit_zero_profit():
    products = ["Product1", "Product2", "Product3"]
    prices = [10.0, 10.0, 10.0]
    costs = [10.0, 10.0, 10.0]
    sort_by_profit(products, prices, costs)
    assert products == ["Product1", "Product2", "Product3"]
    assert prices == [10.0, 10.0, 10.0]
    assert costs == [10.0, 10.0, 10.0]

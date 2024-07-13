import pytest
from products import Product


def test_create_product_object():
    product = Product("test_product", 5, 200)
    assert product is not None


def test_create_product_empty_name():
    with pytest.raises(ValueError):
        product = Product("", 5, 200)


def test_product_negative_price():
    with pytest.raises(ValueError):
        product = Product("test_product", -5, 200)


def test_product_is_inactive():
    product = Product("test_product", 5, 200)
    product.buy(200)
    assert product.is_active() == False


def test_product_purchase():
    product = Product("test_product", 5, 200)
    product.buy(2)
    assert product.quantity == 198


def test_product_overbuy():
    with pytest.raises(ValueError):
        product = Product("test_product", 5, 200)
        product.buy(500)


pytest.main()

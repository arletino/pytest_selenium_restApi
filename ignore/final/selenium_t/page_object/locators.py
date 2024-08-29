from conftest import data_locators
    
class TestSearchLocators:
    ...

for name, value in data_locators().items():
    setattr(TestSearchLocators, name, value)

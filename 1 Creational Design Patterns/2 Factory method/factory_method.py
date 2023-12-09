from abc import ABC, abstractmethod


class Country:
    pass


class USA(Country):
    pass


class Spain(Country):
    pass


class Japan(Country):
    pass


class CurrencyFactory(ABC): #Inherited from ABC
    @abstractmethod #Abstract Method
    def currency_factory(self, country) -> str: #We will return string from this defination.
        pass


class FiatCurrencyFactory(CurrencyFactory):
    def currency_factory(self, country) -> str:
        if country is USA:
            return "USD"
        elif country is Spain:
            return "EUR"
        else:
            return "JPY"


class VirtualCurrencyFactory(CurrencyFactory):
    def currency_factory(self, country) -> str:
        if country is USA:
            return "Bitcoin"
        elif country is Spain:
            return "Ethereum"
        else:
            return "Dogecoin"


#Client code - they dont know whats inside , we are simply creating objects and asking them to use.
if __name__ == '__main__':
    f1 = FiatCurrencyFactory()
    f2 = VirtualCurrencyFactory()

    print(f1.currency_factory(USA))
    print(f1.currency_factory(Spain))
    print(f1.currency_factory(Japan))

    print(f2.currency_factory(USA))
    print(f2.currency_factory(Spain))
    print(f2.currency_factory(Japan))





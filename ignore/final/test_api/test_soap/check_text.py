from zeep import Client, Settings

def check_text(text, wsdl):
    '''Checking text using yandex spell checker online with soap'''
    settings = Settings(strict=False)
    client =Client(wsdl=wsdl, settings=settings)
    response = client.service.checkText(text)
    return response[0]['s']

if __name__ == '__main__':
    print(check_text('Прювет', 'http://speller.yandex.net/services/spellservice?WSDL'))
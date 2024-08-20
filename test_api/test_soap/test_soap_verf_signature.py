import pytest
from zeep import Client


@pytest.mark.exc
def test_step1():
    wsdl = 'https://dss.cryptopro.ru/verify/service.svc?wsdl'
    sign = ''
    client = Client(wsdl=wsdl)
    assert client.service.VerifySignature('CMS', sign)


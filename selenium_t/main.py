import yaml
from module import Site, Chrome, Gecko, Edge

if __name__ == '__main__':
    with open('config.yaml') as f:
        testdata = yaml.safe_load(f)
    site = Site(testdata['address'])
    # site2 = Gecko(testdata['address'])
    # site3 = Edge(testdata['address'])

    css_selector ='span.mdc-text-field__ripple'
    xpath = '//*[@id="login"]/div[3]/button'
    print(site.get_element_property('css', css_selector, 'height'))
    print(site.get_element_property('xpath', xpath, 'color'))


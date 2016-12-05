import urllib
url = 'http://www.lagosschoolsonline.com/Schools'

base_url = 'http://www.lagosschoolsonline.com'

def next_page(i, type=None):
    if type != None:
        new_url = url + "?page=" + str(i) + "&type=" + urllib.quote_plus(type)
        return new_url
    else:
        new_url = url + "?page=" + str(i)
        return new_url


school_types = [('Nursery/Primary', 281),
                ('Secondary', 172),
                ('Special Schools', 2),
                ('Technical colleges', 2),
                ('Handcrafts/Home Econs./Computer Centres', 13),
                ('Vocational/Remedial', 4),
                ]

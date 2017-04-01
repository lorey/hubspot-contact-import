import os
from os import listdir

from os.path import isfile, join

import vobject


def get_contacts():
    contacts = []

    mypath = os.path.dirname(os.path.realpath(__file__)) + '/out/vcards'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for file_name in onlyfiles:
        with open(join(mypath, file_name), encoding='ISO-8859-1') as vcard_file:
            v = vobject.readOne(vcard_file.read())

            if hasattr(v, 'email'):
                address = v.adr.value
                contact = {
                    'title': v.title.value,
                    'org': v.org.value[0],
                    'name': v.fn.value,
                    'firstname': v.n.value.family,
                    'lastname': v.n.value.given,
                    'email': v.email.value,
                    'street': address.street,
                    'city': address.city,
                    'country': address.country,
                    'state': address.region,
                    'zip': address.code or None,
                    'phone': None,
                }

                if 'tel' in v.contents:
                    contact['phone'] = v.contents['tel'][0].value

                contacts.append(contact)

    return contacts

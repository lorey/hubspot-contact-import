import logging

import hubspot
import xing


def main():
    for xing_contact in xing.get_contacts():
        hubspot_contact = hubspot.find_contact_by_email(xing_contact['email'])

        if hubspot_contact is not None:
            # contact has been found, don't do anything
            logging.info('skipped %s' % xing_contact['name'])
        else:
            # contact is unknown: upload
            email = xing_contact['email']

            properties = {
                'firstname': xing_contact['name'].split(' ', 1)[0],
                'lastname': xing_contact['name'].split(' ', 1)[1],
                'company': xing_contact['org'],
                'phone': xing_contact['phone'],
                'address': xing_contact['street'],
                'city': xing_contact['city'],
                'state': xing_contact['state'],
                'zip': xing_contact['zip'],
            }

            hubspot.create_or_update_contact(email, properties)
            logging.info('created %s' % xing_contact['name'])

if __name__ == '__main__':
    main()

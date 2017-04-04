import hubspot


def main():
    """
    Shows and merges potential duplicates.
    :return:
    """
    for contact in hubspot.fetch_contacts():
        # find contact with the same name
        contacts = hubspot.find_contacts(contact.get_name())
        if len(contacts) > 1:
            print('Possible duplicate for %s' % contact.get_name())

            print('[0]: Don\'t merge')
            for i in range(0, len(contacts)):
                duplicate_contact = contacts[i]
                print('[%d]: %s' % (i + 1, duplicate_contact.get_email()))
            print()

            # todo: fetch user choice and delete

if __name__ == '__main__':
    main()

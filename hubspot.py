import json
import urllib

import requests

import config

BASE_URL = 'https://api.hubapi.com/'


class Contact(object):
    data = {}

    def __init__(self, data):
        self.data = data

    def get_email(self):
        return next((item for item in self.data['identity-profiles'][0]['identities'] if item["type"] == "EMAIL"))['value']

    def get_name(self):
        properties_ = self.data['properties']
        return properties_['firstname']['value'] + ' ' + properties_['lastname']['value']


def fetch_contacts():
    contacts = []

    offset = 0
    has_more = True
    while has_more:
        url = get_url_to_fetch_contacts(offset)
        response = requests.get(url)
        response_data = response.content.decode('utf-8')
        json_data = json.loads(response_data)

        contacts_in_result = json_data['contacts']
        contacts.extend([Contact(contact_data) for contact_data in contacts_in_result])

        has_more = json_data['has-more']
        offset = json_data['vid-offset']

    return contacts


def get_url_to_fetch_contacts(offset, count=100):
    params = {
        'hapikey': config.HUBSPOT_HAPIKEY,
        'count': count,
        'vidOffset': offset,
    }
    return BASE_URL + 'contacts/v1/lists/all/contacts/all?%s' % urllib.parse.urlencode(params)


def find_contact_by_email(email):
    url = get_url_to_find_contact_by_email(email)
    response = requests.get(url)
    if response.status_code == 404:
        return None

    response_data = response.content.decode('utf-8')
    return Contact(json.loads(response_data))


def get_url_to_find_contact_by_email(email):
    params = {
        'hapikey': config.HUBSPOT_HAPIKEY
    }
    return BASE_URL + 'contacts/v1/contact/email/%s/profile?%s' % (email, urllib.parse.urlencode(params))


def create_or_update_contact(email, properties=None):
    if properties is None:
        properties = {}

    data = {'properties': []}
    for key in properties:
        value = properties[key]
        if value is not None:
            data['properties'].append(get_property_dict(key, value))

    url = get_url_to_create_or_update_contact(email)
    response = requests.post(url, json=data)


def get_url_to_create_or_update_contact(email):
    params = {'hapikey': config.HUBSPOT_HAPIKEY}
    return BASE_URL + 'contacts/v1/contact/createOrUpdate/email/%s/?%s' % (email, urllib.parse.urlencode(params))


def get_property_dict(key, value):
    return {
        'property': key,
        'value': value,
    }


def find_contact(query):
    contacts = find_contacts(query)
    return next(contacts, None)


def find_contacts(query):
    url = get_url_to_find_contacts(query)
    response = requests.get(url)

    response_data = response.content.decode('utf-8')
    search_result = json.loads(response_data)

    return [Contact(result) for result in search_result['contacts']]


def get_url_to_find_contacts(query):
    params = {
        'hapikey': config.HUBSPOT_HAPIKEY,
        'q': query,
    }
    return BASE_URL + 'contacts/v1/search/query?%s' % urllib.parse.urlencode(params)

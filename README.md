# Import Xing contacts or vcards to Hubspot

This tool imports [Xing](https://xing.com) contacts via their vcards to hubspot. It's also possible to upload arbitrary vcards to hubspot, I guess.

Because I started to use hubspot as my CRM, I wanted to import all my existing contacts.
This was easy with Linkedin because you can simply export your contacts as a CSV and import them to hubspot afterwards via their CSV import.
That's how it should work and was done within a few minutes.

On the other hand, it isn't even possible to export your contacts in bulk with Xing, all while they claim to be 'democratizing information' in their terms of service.
The only option you have to get a hold of your own contacts: Download every single vcard manually.
You can decide for yourself if this is worth the effort.
Please note, that by the terms of service I am not allowed to advertise any automatic mechanism to download your contacts.
So don't free your data by writing a small [selenium](http://selenium-python.readthedocs.io/installation.html) script that downloads all contacts' vcards [automatically](https://gist.github.com/lorey/366ef67fc7384f300dfc31f7800e45ba).
Bad idea, don't do it!

So after you have *manually* downloaded all your contacts' vcards by hand, you can upload and sync them into hubspot with this little tool.

## Usage

Please note that this is in alpha. The tool is currently only creating contacts for unknown emails.

1. Download the vcards of the Xing contacts you wish to import.
2. Put them into `out/vcards`
3. Run xing-to-hubspot.py inside the bin folder.
4. Enjoy the new or updated contacts within your hubspot account.
5. (Merge contacts that belong to the same person and they will never be created again, e.g. if you had peter@miller.com and petermiller@gmail was created as a new contact)

## Dependencies

This plugin depends on:

- [vobject](https://github.com/eventable/vobject) to read the vcards
- [requests](https://github.com/kennethreitz/requests) to make API calls to hubspot

## Installation

### Install the dependencies if you have not installed them already.

    pip install vobject
    pip install requests

### Create a Hubpsot API Key

Click on your profile image in the navigation bar and select 'Integrations'. Under 'Your integrations' you will find the possibility to crate an API key.

### Create a config file

Create a config.py file in the main directory with the following contents

    HUBSPOT_HAPIKEY = 'YOUR-HAPI-KEY'

## License

GPL
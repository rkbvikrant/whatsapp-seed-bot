"""
    Credentials to connect on Whatsapp Servers. (phone number, whatsapp key)

    To extract key use the yowsup-cli (using a python venv with yowsup installed):

    > yowsup-cli registration -C <CountryCode> -r sms -p <Phone Number with Country Code>
    ex.:
    yowsup-cli registration -C 55 -r sms -p 554899998888

    Then whatsapp will send a key via sms to the phone.
    Get that key then run:

    > yowsup-cli registration -C 55 -R <sms-key> -p 554899998888

    status: ok
    kind: free
    > pw: njH+QGBqXXXXXXXXOFa+Wth5riM=
    price: US$0.99
    price_expiration: 1444272405
    currency: USD
    cost: 0.99
    > login: 554XXXXXX087
    type: existing
    expiration: 1472404969

    Now just get the login and pw, and replace bellow. :)
"""

auth = ("XXX login XXX", "XXXXXXXXXXXXXXX pw XXXXXXXXXXXXXXX")


# Path to download the media requests
media_storage_path = "/tmp/"


# Logging settings
import logging

log_format = '_%(filename)s_\t[%(levelname)s][%(asctime)-15s] %(message)s'
logging_level = logging.DEBUG


#  - Base location code
#  for auto-complete phone numbers without it on group_admin views
#  ex.: 55 - Brazil code
#       48 - State code
BASE_LOCATIONCODE = "5548"

import urllib.parse
import os
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


def sendSms(msisdn, message):

    parameters = {
        'username' : 'osborn',
        'password' : 'P@55w0rd!',
        'type' : '0',
        'dlr' : '1',
        'destination' : msisdn,
        'source' : 'NABPTEX',
        'message' : message,
        }

    url = "http://api.nalosolutions.com/bulksms/?"+urllib.parse.urlencode(parameters)
    result = os.system("curl '{0}'".format(url))

    return result



class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
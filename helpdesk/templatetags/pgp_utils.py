"""
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. All Rights Reserved. See LICENSE for details.

templatetags/pgp_utils.py - Used for PGP related template filters
"""

from django import template

from helpdesk import settings as helpdesk_settings

if helpdesk_settings.HELPDESK_USE_GNUPG:
    
    from django.template.defaultfilters import stringfilter
    
    from helpdesk.lib import verify_signed_message, signed_message_data
    
    @stringfilter
    def is_signed(message):
        ''' returns True is message appears to be a correctly-formatted
        PGP signed message, does not attempt to verify the signature '''
        return message.find('-----BEGIN PGP SIGNED MESSAGE-----', 0) > -1
        

    @stringfilter
    def verify_sig(message):
        ''' returns True if message has a valid signature '''
        return verify_signed_message(message)
    
    def sig(message):
        ''' returns key ID and username used to sign message
        in a user-friendly string '''
        return signed_message_data(message)


    register = template.Library()
    register.filter(is_signed)
    register.filter(verify_sig)
    register.filter(sig)

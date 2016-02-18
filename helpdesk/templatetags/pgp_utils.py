"""
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. All Rights Reserved. See LICENSE for details.

templatetags/pgp_utils.py - Used for PGP related template filters
"""

from django import template

from helpdesk import settings as helpdesk_settings

if helpdesk_settings.HELPDESK_USE_GNUPG:
    
    from django.template.defaultfilters import stringfilter
    
    from helpdesk.lib import verify_signed_message

    @stringfilter
    def verify_sig(message):
        ''' returns True if message has a valid signature '''
        return verify_signed_message(message)


    register = template.Library()
    register.filter(verify_sig)

# -*- coding: utf-8 -*-
# Copyright (c) 2008 Ingeniweb

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
from zope.interface import Interface
from zope.interface import Attribute
from zope.schema import TextLine

from collective.contentrules.mail import MessageFactory as _

class IMailModel(Interface):
    """A named utility providing a mail model"""

    title = TextLine(title=_(u"A friendly name for model",))

    replacer_interface = Attribute(u"Interface providing word substitution in "\
        "mail fields: source, recipients, subject, text")

    help = Attribute(u"Help text exposing all variables provided by replacer"\
        "interface")

class IMailReplacer(Interface):
    """Interface providing variables which can be used in mail fields:
    source, recipients, subject, text"""

    id = TextLine(title=_(u"Id of content",))

    title = TextLine(title=_(u"Title of content",))

    description = TextLine(title=_(u"Description of content",))

    url = TextLine(title=_(u"Url to access content",))

    relative_url = TextLine(
        title=_(u"Relative url from portal to access content",))

    portal_url = TextLine(title=_(u"Url of portal",))

    owner_id = TextLine(title=_(u"Login of content ower",))

    owner_fullname = TextLine(title=_(u"Fullname of content owner",))
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
from zope.interface import implements
from zope.component import adapts

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.interfaces import IBaseObject

from collective.contentrules.mail.interfaces import IMailReplacer

class MailReplacer(object):
    """Provides attributes which can be used in a mail model"""

    implements(IMailReplacer)
    adapts(IBaseObject)

    def __init__(self, context):
        self.context = context
        self.utool = getToolByName(context, "portal_url")
        self.mtool = getToolByName(context, "portal_membership")

    @property
    def id(self):
        return self.context.getId()

    @property
    def title(self):
        return self.context.title_or_id()

    @property
    def description(self):
        return self.context.Description()

    @property
    def url(self):
        return self.context.absolute_url()

    @property
    def relative_url(self):
        return self.utool.getRelativeUrl(self.context)

    @property
    def portal_url(self):
        return self.utool()

    @property
    def owner_id(self):
        return self.context.Creator()

    @property
    def owner_fullname(self):
        owner = self.mtool.getMemberById(self.owner_id)

        if owner is None:
            # Owner is not registered in portal_metadata, so fullname can't
            # be retrieved
            return self.owner_id

        # Returns fullname
        return owner.getProperty('fullname')
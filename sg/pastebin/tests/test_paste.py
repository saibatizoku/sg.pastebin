# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import createObject
from zope.component import queryUtility

from Products.CMFCore.utils import getToolByName
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI

from sg.pastebin.testing import INTEGRATION_TESTING
from sg.pastebin.paste import IPaste


class TestPastebinIntegration(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

    def test_adding(self):
        self.folder.invokeFactory('sg.pastebin.paste', 'snippet1')
        snippet1 = self.folder['snippet1']
        self.failUnless(IPaste.providedBy(snippet1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='sg.pastebin.paste')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='sg.pastebin.paste')
        schema = fti.lookupSchema()
        self.assertEquals(IPaste, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='sg.pastebin.paste')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IPaste.providedBy(new_object))

    def test_properties(self):
        properties_tool = getToolByName(self.portal, 'portal_properties')
        self.failUnless('pastebin_properties' in properties_tool)

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

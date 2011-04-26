# -*- coding: utf-8 -*-

from Products.PloneTestCase import ptc
import collective.testcaselayer.ptc

ptc.setupPloneSite()


class IntegrationTestLayer(collective.testcaselayer.ptc.BasePTCLayer):

    def afterSetUp(self):
        # Install the sg.pastebin add-on
        self.addProfile('sg.pastebin:default')

Layer = IntegrationTestLayer([collective.testcaselayer.ptc.ptc_layer])

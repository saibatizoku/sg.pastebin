# -*- coding: utf-8 -*-
from five import grok

from zope.interface import Interface
from zope import schema
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName

from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.registry.browser import controlpanel

from sg.pastebin import _

LANGS = [ u"ActionScript", u"Bash",
          u"C", u"C#",
          u"C++", u"CSS",
          u"HTML", u"Java",
          u"JavaScript", u"Lua",
          u"Perl", u"PHP",
          u"Python", u"SQL",
          u"Ruby"]

class ISGPastebinSettings(Interface):
    """ Interface for the form on the control panel. """
    preferred_languages = schema.Set(title=_(u"Preferred coding languages"),
            description=_(u"A list of coding languages that will be highlighted according to their specific syntax."),
            required=False,
            default=set(LANGS),
            value_type= schema.TextLine(title=_(u"Language")))

    preferred_styles = schema.Set(title=_(u"Styles for highlighting syntax"),
            required=False,
            default=set([]),
            value_type = schema.TextLine(title=_(u"Highlighting style"))
            )


class SGPastebinSettingsEditForm(controlpanel.RegistryEditForm):
    grok.context(IPloneSiteRoot)
    grok.name("sg_questions_settings")
    grok.require("cmf.ManagePortal")

    schema = ISGPastebinSettings
    label = _(u"SoftwareGuru Pastebin Settings") 
    description = _(u"Here you can modify the settings for SG Pastebin.")

    def updateFields(self):
        super(SGPastebinSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(SGPastebinSettingsEditForm, self).updateWidgets()
        self.widgets['preferred_languages'].rows = 15
        self.widgets['preferred_languages'].style = u'width: 30%;'
        self.widgets['preferred_styles'].rows = 10
        self.widgets['preferred_styles'].style = u'width: 30%;'

class SGPastebinSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SGPastebinSettingsEditForm

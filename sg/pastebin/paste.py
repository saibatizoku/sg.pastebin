# -*- coding: utf-8 -*-
from five import grok
from zope import schema

from zope.component import getUtility

from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.memoize.instance import memoize

from plone.directives import form, dexterity
from plone.app.textfield import RichText

from pygments import highlight
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from plone.registry.interfaces import IRegistry
from sg.pastebin.controlpanel import ISGPastebinSettings
from sg.pastebin import _

class ISGPastebinLayer(IDefaultBrowserLayer):
    """ Browser layer for sg.pastebin """

class LanguageVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ISGPastebinSettings)
        terms = []
        for lang in sorted(settings.preferred_languages):
            terms.append(SimpleTerm(value=str(lang).lower(), title=lang))
        return SimpleVocabulary(terms)

grok.global_utility(LanguageVocabulary, name=u"sg.pastebin.languages")

class IPaste(form.Schema):
    """ A content-type for source code snippets. """
    lexer  = schema.Choice(title=_(u"Language"), vocabulary=u"sg.pastebin.languages", default='python')
    code = schema.SourceText(title=_(u"Source code"))


class View(grok.View):
    grok.context(IPaste)
    grok.require('zope2.View')
    grok.layer(ISGPastebinLayer)


    @memoize
    def pygmented(self):
        """ Returns highlighted source code """
        lx = get_lexer_by_name(self.context.lexer)
        return highlight(self.context.code, lx, HtmlFormatter())

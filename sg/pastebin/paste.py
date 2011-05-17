# -*- coding: utf-8 -*-
from five import grok
from zope import schema
from plone.namedfile.field import NamedFile

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.directives import form, dexterity
from plone.app.textfield import RichText

from pygments import highlight
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from sg.pastebin import _

class ISGPastebinLayer(IDefaultBrowserLayer):
    """ Browser layer for sg.pastebin """

"""
@grok.provider(IContextSourceBinder)
def lexer_vocabulary(context=None):
    cnt = 0
    terms = []
    for lexer in get_all_lexers():
        cnt += 1
        terms.append(SimpleTerm(token=cnt, value=lexer[0], title=lexer[0]))
    return None # SimpleVocabulary(terms)
"""

class IPaste(form.Schema):
    """ A content-type for source code snippets. """
    lexer  = schema.Choice(title=_(u"Language"), values=['python', 'php'], default='python')
    code = schema.SourceText(title=_(u"Source code"))
    codefile = NamedFile(title=_(u"Source-code file"), required=False)


class View(grok.View):
    grok.context(IPaste)
    grok.require('zope2.View')
    grok.layer(ISGPastebinLayer)

    def pygmented(self):
        """ Returns highlighted source code """
        lx = get_lexer_by_name(self.context.lexer)
        return highlight(self.context.code, lx, HtmlFormatter())

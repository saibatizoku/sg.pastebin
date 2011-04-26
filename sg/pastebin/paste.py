# -*- coding: utf-8 -*-
from five import grok
from zope import schema

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from plone.directives import form, dexterity
from plone.app.textfield import RichText

from pygments import highlight
from pygments.lexers import get_all_lexers
from pygments.formatters import HtmlFormatter

from sg.pastebin import _

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
    body = schema.SourceText(title=_(u"Source code"))
#    language = schema.Choice(title=_(u"Language"), values=lexer_vocabulary())

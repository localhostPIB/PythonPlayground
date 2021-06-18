# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

color = SimpleVocabulary(
        [
        SimpleTerm(value='blue', title='Blau'),
        SimpleTerm(value='red', title='Rot'),
        SimpleTerm(value='orange', title='Orange'),
        ]
       )
class ISwCustomType(model.Schema):
    """ Marker interface for SwCustomType
    """
   
    layout = schema.Choice(
        title = "Layout",
        required = False,
        description = "Die neuen Farben",
        source = color,
        default = 'blue'
    )
    
from zope.interface import implementer
 
@implementer(ISwCustomType)
class CustomTypeContainer(Container) :
    pass

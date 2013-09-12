# -*- coding: utf-8 -*-

from plone.app.textfield import RichText
from plone.directives import form


class IExample(form.Schema):
    '''Exemplo de schema para um tipo de conteúdo
    '''

    text = RichText(
        title=_(u'Body text'),
        required=False,
    )

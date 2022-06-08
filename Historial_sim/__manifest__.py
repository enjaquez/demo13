# -*- coding: utf-8 -*-
{
    'name': "Historial_cambio_sim",

    'summary': """
    Guardo los cambio de sim """,

    'description': """
    Guarda los cambio de sim en un historial
    """,

    'author': "Sursoom",
    'website': "http://sursoom.mx/",

    # for the full list
    'category': 'historial de SIM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/historia_lot.xml',

    ],

}

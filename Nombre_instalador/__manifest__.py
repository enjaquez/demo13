# -*- coding: utf-8 -*-
{
    'name': "Nom_instaladro",

    'summary': """Nombre de instalador""",

    'description': """
    se coloca un Check para saber si la persona de contactos es instalador
    para ponerlo en el modulo de gps monitor
    """,

    'author': "Sursoom",
    'website': "http://sursoom.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'usuario',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'gpsmonitor','contacts'],

    # always loaded
    'data': [
        'view/conctatos_instador.xml',
        'view/gps_instalador.xml',       
    ],
    # only loaded in demonstration mode
    'installable': True,
    'auto_install': False,
}

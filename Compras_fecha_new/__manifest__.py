# -*- coding: utf-8 -*-
{
    'name': "compras_fechas",

    'summary': """
        fechas programada""",

    'description': """
    agrear campos a factura en la parte de contabilidad
    y se crea un filtro y un agrupador por fecha programada
    """,

    'author': "Sursoom",
    'website': "http://sursoom.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'mrp',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
       'views/vista_compras.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

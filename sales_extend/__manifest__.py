# -*- coding: utf-8 -*-
{
    'name': "Modificaciones a Ventas",

    'summary': """
        Con esta aplicación realizamos personalizaciones a la aplicación
        de ventas.
        """,

    'description': """
        Modificaciones:

        1. Cuando un producto tiene una lista de precio en USD, 
        se calculará en la venta el precio en MXN y se mostrará 
        el tipo de cambio.

    """,

    'author': "Enrique Jaquez Olvera",
    'website': "https://www.sursoom.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    "version": "12.0.0.0.1",
    "application": False,
    "installable": True,
    
    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "Campos para factura",

    'summary': """
        Agregar campos a contactos para pasar el los campos para la facturacion""",

    'description': """
        agregar campos a facturacion
    """,

    'author': "Sursoom",
    'website': "http://sursoom.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','sale','sale_management','account','account_accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml', 
        'views/view_invoice.xml',       
          
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

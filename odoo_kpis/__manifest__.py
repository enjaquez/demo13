# -*- coding: utf-8 -*-
{
    'name': "kpis",

    'summary': """
        Aplicacion para KPIS""",

    'description': """
        KPIs avanzados de distintos modelos
    """,

    'author': "Enrique Jaquez",
    'website': "https://www.sursoom.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    "version": "12.0.0.0.1",
    "application": False,
    "installable": True,
    
    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

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

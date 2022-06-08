# -*- coding: utf-8 -*-
{
    'name': "gpskpi",

    'summary': """
       GPS KPI
       """,

    'description': """
    GPS KPI
    """,

    'author': "Sursoom",
    'website': "https://sursoom.odoo.com/",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','sale_management'],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_goal_view.xml',
        'views/kpi_view.xml',
    ],
    'qweb': [
        'static/src/xml/kpi.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,

}

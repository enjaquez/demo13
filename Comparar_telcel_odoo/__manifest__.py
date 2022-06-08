# -*- coding: utf-8 -*-
{
    'name': "Cmp_telcel_odoo",

    'summary': """
     compara de telcel_odoo """,

    'description': """
      cargar documento de telcel y sacar diferencias
    """,

    'author': "Sursoom",
    'website': "http://sursoom.mx/",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','gpsmonitor'],
        # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/load_data.xml',
        'views/action_telcel.xml',
        'views/view_data_odoo.xml',
        'views/view_data_telcel.xml',
        'views/menu_action.xml',
        'views/load_data_data.xml',
        'wizard/wizard_telcel.xml',


     ],

}

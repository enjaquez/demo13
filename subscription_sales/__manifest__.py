# -*- coding: utf-8 -*-
{
    'name': 'Subscription to budget accounts',
    'version': '0.1',
    'category': 'Sales',
    'summary': 'Subscription to budget accounts',
    'description': """
Subscription to budget accounts
===============================
    """,
    'depends': [
        'sale_subscription',
    ],
    'data': [
        'wizard/subscription_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}

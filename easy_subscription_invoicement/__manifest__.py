# -*- coding: utf-8 -*-
{
    'name': "Easy Subscription Invoicement",
    'summary': "Improvement of subscription invoicements tools",
    'description': "Improvement of subscription invoicements tools",
    'author': "Sursoom",
    'website': "http://www.yourcompany.com",
    'category': 'Invoicing',
    'version': '0.1',
    'depends': ['base', 'contacts', 'sale_subscription', 'account', 'l10n_mx_edi','account_accountant'],
    'data': [
        'views/res_partner.xml',
        'views/account_invoice.xml',
        'views/sale_subscription.xml',
        'views/crm_lead.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': False,
}

# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"


    payment_term_id = fields.Many2one('account.payment.term', string='Payment Terms',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    


    def _prepare_invoice_data(self):
    	res = super(SaleSubscription, self)._prepare_invoice_data()
    	sale_order = self.env['sale.order'].search([('order_line.subscription_id', 'in', self.ids)], order="id desc", limit=1)
    	res['invoice_payment_term_id'] = self.payment_term_id.id if self.payment_term_id else sale_order.payment_term_id.id if sale_order else self.partner_id.property_payment_term_id.id 
    	return res
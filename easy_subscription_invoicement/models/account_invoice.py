# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Invoice(models.Model):

    _inherit = "account.invoice"

    USAGES = [
        ('G01', 'Acquisition of merchandise'),
        ('G02', 'Returns, discounts or bonuses'),
        ('G03', 'General expenses'),
        ('I01', 'Constructions'),
        ('I02', 'Office furniture and equipment investment'),
        ('I03', 'Transportation equipment'),
        ('I04', 'Computer equipment and accessories'),
        ('I05', 'Dices, dies, molds, matrices and tooling'),
        ('I06', 'Telephone communications'),
        ('I07', 'Satellite communications'),
        ('I08', 'Other machinery and equipment'),
        ('D01', 'Medical, dental and hospital expenses.'),
        ('D02', 'Medical expenses for disability'),
        ('D03', 'Funeral expenses'),
        ('D04', 'Donations'),
        ('D05', 'Real interest effectively paid for mortgage loans (room house)'),
        ('D06', 'Voluntary contributions to SAR'),
        ('D07', 'Medical insurance premiums'),
        ('D08', 'Mandatory School Transportation Expenses'),
        ('D09', 'Deposits in savings accounts, premiums based on pension plans.'),
        ('D10', 'Payments for educational services (Colegiatura)'),
        ('P01', 'To define'),
    ]

    PAYMENT_POLICIES = [
        ('PUE', 'Single exhibition payment'),
        ('PPD', 'Blases payment'),
    ]

    payment_policy = fields.Selection(PAYMENT_POLICIES)
    payment_date = fields.Text(string="Payment Date", compute='get_payment_date')

    @api.multi
    @api.depends('payment_ids.payment_date')
    def get_payment_date(self):
        for each in self:
            each.payment_date = ''
            if each.payment_ids:
                for payment in each.payment_ids:
                    each.payment_date = each.payment_date + payment.payment_date.strftime("%d/%m/%Y") + '\n'

    @api.onchange("partner_id")
    def _compute_sat_information(self):
        for invoice in self:
            if invoice.partner_id:
                invoice.payment_policy = invoice.partner_id.payment_policy
                invoice.l10n_mx_edi_usage = invoice.partner_id.usage
                invoice.l10n_mx_edi_payment_method_id = invoice.partner_id.method_id

    @api.multi
    def _l10n_mx_edi_get_payment_policy(self):
        if self.payment_policy:
            return self.payment_policy
        return self.partner_id.payment_policy

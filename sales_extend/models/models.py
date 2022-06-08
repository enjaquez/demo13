# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import requests
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class ExtendSaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def compute_subtotal_mxn_sin_impuestos(self):
        for record in self:
            record.subtotal_mxn_sin_impuestos = record.amount_untaxed * (1 / record.currency_rate)

    @api.multi
    def compute_impuestos_mxn(self):
        for record in self:
            record.impuestos_mxn = record.amount_tax * (1 / record.currency_rate)

    @api.multi
    def compute_total_mxn(self):
        for record in self:
            record.total_mxn = record.amount_total * (1 / record.currency_rate)

    orden_mxn = fields.Boolean(string='Orden en MXN', default='True')
    tipo_cambio = fields.Float(string='Tipo de Cambio', default=1.0)
    subtotal_mxn_sin_impuestos = fields.Float(string='Base imponible MXN', compute=compute_subtotal_mxn_sin_impuestos)
    impuestos_mxn = fields.Float(string='Impuestos MXN', compute=compute_impuestos_mxn)
    total_mxn = fields.Float(string='Total MXN', compute=compute_total_mxn)

    @api.onchange('pricelist_id')
    def onchange_pricelist_id(self):

        #raise ValidationError(self.pricelist_id.name)
        if self.pricelist_id.name == "Dólares":
            self.orden_mxn = False
        else:
            self.orden_mxn = True
        self.tipo_cambio = 1 / self.currency_rate


class ExtendSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def compute_precio_mxn(self):
        for record in self:
            record.precio_mxn = record.price_unit * record.tipo_cambio
            record.subtotal_mxn = record.precio_mxn * record.product_uom_qty

    @api.multi
    def compute_subtotal_mxn(self):
        for record in self:
            record.subtotal_mxn = record.precio_mxn * record.product_uom_qty

    @api.multi
    def compute_currency_rate(self):
        for record in self:
            
            result2 = record.currency_id.name
            #raise ValidationError(result2)

            if result2 == 'USD':
                sql = "SELECT rate FROM res_currency_rate WHERE currency_id='2' ORDER BY name DESC LIMIT 1"
                record.env.cr.execute(sql)
                result = record.env.cr.fetchone()
                record.tipo_cambio = 1 / result[0]
            else:
                record.tipo_cambio = 1

    precio_mxn = fields.Float(string='Precio MXN', compute=compute_precio_mxn)
    subtotal_mxn = fields.Float(string='Subtotal MXN', compute=compute_subtotal_mxn)
    tipo_cambio = fields.Float(string="Tipo de Cambio", compute=compute_currency_rate)




# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
class SaleSubscription(models.Model):

    _inherit="sale.subscription"
    _description = "Actualizar documentos GPS"

    line_description = fields.Text(compute="_get_line_description", string="Descripción")

    @api.depends('recurring_invoice_line_ids.name')
    def _get_line_description(self):
        for rec in self:
            rec.line_description = rec.recurring_invoice_line_ids.name

    def update_gps_documents(self):
        for rec in self:
            for line in rec.recurring_invoice_line_ids:
                self._cr.execute('''
                    SELECT nombre
                    FROM auto_paquet_servicio aps
                    JOIN sale_subscription ss ON ss.id = aps.proxima_factura
                    JOIN res_partner rp ON rp.id = aps.empresa
                    WHERE aps.proxima_factura = %s  
                    AND aps.empresa = %s
                    ''', [rec.id, rec.partner_id.id])
                
                gps_record = self._cr.dictfetchall()
                if gps_record:
                    line.name = ''
                    line.name += line.product_id.get_product_multiline_description_sale()
                    for each in gps_record:
                        line.name = line.name +'\n'+ each.get('nombre')


            








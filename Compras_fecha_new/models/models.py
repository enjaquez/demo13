# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Purcahases_date(models.Model):

    _inherit=["account.invoice"]

    fechas_programada = fields.Date(string="Fecha programada")

    @api.onchange('fechas_programada')
    def _onchange_company_id(self):
        self.date_due = self.fechas_programada
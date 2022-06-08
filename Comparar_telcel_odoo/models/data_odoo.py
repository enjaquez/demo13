# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo_vs_telcel(models.Model):

    _name="data_odoo.result"

    numero_tel = fields.Char(string="Numero Teléfonica")

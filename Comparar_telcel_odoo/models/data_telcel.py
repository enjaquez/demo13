# -*- coding: utf-8 -*-

from odoo import models, fields, api

class telcel_vs_odoo(models.Model):

    _name="data_telcel.result"

    proveedor = fields.Char(string="Proveedor")

    numero_tel = fields.Char(string="Numero Teléfonica")

    serie = fields.Char(string="Serie")

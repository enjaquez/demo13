# -*- coding: utf-8 -*-

from odoo import models, fields, api

class modelos_telcel_odoo(models.Model):

    _name="load_data.telcel"

    numero_tel = fields.Char(string="Numero Teléfonica")

    consepto_MB = fields.Char(string="Concepto")

    consumido = fields.Char(string="Consumido")

    excedente = fields.Char(string="Exedente")

    gran_total=fields.Char(string="Gran Total")

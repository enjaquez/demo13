# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sim_plataforma(models.Model):

    _name="data.plataforma"

    _description="Modelo para mostrar las diferencias de odoo con excel"

    #folio = fields.Char(string="Folio")

    name = fields.Char(string="Nombre")

    imei = fields.Char(string="Imei")

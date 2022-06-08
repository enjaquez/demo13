# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sim_data(models.Model):

    _name="data.odoo"

    _description="Modelo para mostrar las diferencias del excel con odoo"

    #folio = fields.Char(string="Folio")

    name = fields.Char(string="Nombre")

    imei = fields.Char(string="Imei")

    

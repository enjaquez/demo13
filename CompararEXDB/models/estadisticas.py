# -*- coding: utf-8 -*-

from odoo import models, fields, api

class estadisticas_data(models.Model):

    _name="estadisticas.data_load"

    _description="Modelo para tener resultado estadistico"

    cantidad_act = fields.Char(string="Can. actualizado")

    

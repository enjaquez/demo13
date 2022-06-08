# -*- coding: utf-8 -*-

from odoo import models, fields, api

class numeros_telcel_odoo(models.Model):

    _name="load_data_numeros.telcel"

    numero_tel = fields.Char(string="Numero Teléfonica")

    

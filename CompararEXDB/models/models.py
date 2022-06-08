# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Load_data(models.Model):

    _name="data.data_load"

    _description="Modelo para cargar informacion de la Plataforma"

    name = fields.Char(string="Nombre")

    imel = fields.Char(string="IMEI")

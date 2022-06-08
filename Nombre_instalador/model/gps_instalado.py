# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gps_instalado(models.Model):

    _inherit="auto.paquet.servicio"

    instaladores = fields.Many2one('res.partner',string="Instalador",domain="[('is_instalador','=',True)]")

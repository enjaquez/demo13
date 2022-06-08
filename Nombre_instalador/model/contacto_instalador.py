# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Instaldo_contactos_data(models.Model):

    _inherit="res.partner"

    is_instalador = fields.Boolean(string="Es instalador")

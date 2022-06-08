# -*- coding: utf-8 -*-

from odoo import models, fields, api
#este modelo donde de agregan los tipos de pagos
class tipos_pagos_facturas(models.Model):

	_name="invoice.type.pag"

	_rec_name="nombre"

	#sequence=fields.Integer("Referencia",store=True)

	nombre=fields.Text("Nombre",store=True)

	descrip=fields.Text("Descripción",store=True)


	




	

# -*- coding: utf-8 -*-

from odoo import models, fields, api
class producto_lot(models.Model):

	_inherit="stock.production.lot"

	historial = fields.Html(string="Historial")

	@api.multi
	def write(self, vals):
		for record in self:
			if record.historial:
				temp=record.historial
				vals['historial']=temp+record.name+"<br/>"
			else:
				vals['historial']=record.name
		result = super(producto_lot, self).write(vals)
		return result

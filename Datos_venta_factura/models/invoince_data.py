# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contatos_invoice(models.Model):

	_inherit = 'account.invoice'

	@api.onchange('partner_id')
	def on_change_fields(self):		
		if self.partner_id.id>0:
			datos_usuario=self.env['res.partner'].search_read([('id','=',self.partner_id.id)],['Metodos_pago','tipo_factura','fields_selection'])
			id_forma_pago=datos_usuario[0]['Metodos_pago']
			id_tipo_pago=datos_usuario[0]['tipo_factura']
			id_fields_selection=datos_usuario[0]['fields_selection']
			self.l10n_mx_edi_payment_method_id=id_forma_pago
			self.metodos_pago_invoice=id_tipo_pago	
			self.l10n_mx_edi_usage=id_fields_selection		

	metodos_pago_invoice=fields.Many2one('invoice.type.pag')

	



	
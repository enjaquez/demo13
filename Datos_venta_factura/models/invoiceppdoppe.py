# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Invoice_PPD_PUE(models.Model):

	_inherit="account.invoice"

	@api.multi
	def _l10n_mx_edi_get_payment_policy(self):
		self.ensure_one()
		version=self.l10n_mx_edi_get_pac_version()
		term_ids=self.payment_term_id.line_ids
		if version == '3.2':
			if len(term_ids.ids) > 1:
				return 'Pago en parcialidades'
			else:
				return 'Pago en una sola exhibición'
		elif version == '3.3' and self.date_due and self.date_invoice:
			valortipo = 'PUE'
			if self.x_studio_tipo_de_pago:
				valortipo = self.x_studio_tipo_de_pago
			#return valortipo[:3]
			if valortipo=='PUE - Pago en una sola exhibicion':
				return 'PUE'
			return 'PPD'
		return ''





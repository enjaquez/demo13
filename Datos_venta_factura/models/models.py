# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contatos_ventas(models.Model):

	_inherit = 'res.partner'

	Metodos_pago=fields.Many2one('l10n_mx_edi.payment.method')

	tipo_factura=fields.Many2one('invoice.type.pag')

	fields_selection=fields.Selection([('G01', 'Adquisición de mercancías'),
        ('G02', 'Devoluciones, descuentos o bonificaciones'),
        ('G03', 'Gastos generales'),
        ('I01', 'Construcciones'),
        ('I02', 'Inversión en mobiliario y equipo de oficina'),
        ('I03', 'Equipo de transporte'),
        ('I04', 'Equipo informático y accesorios'),
        ('I05', 'Dados, matrices, moldes, matrices y herramientas'),
        ('I06', 'Comunicaciones telefónicas'),
        ('I07', 'Comunicaciones por satélite'),
        ('I08', 'Otra maquinaria y equipo'),
        ('D01', 'Gastos médicos, dentales y hospitalarios'),
        ('D02', 'Gastos médicos por discapacidad'),
        ('D03', 'Gastos funerarios'),
        ('D04', 'Donaciones'),
        ('D05', 'Intereses reales efectivamente pagados por préstamos hipotecarios (casa de habitación)'),
        ('D06', 'Contribuciones voluntarias a SAR'),
        ('D07', 'Primas de seguro médico'),
        ('D08', 'Gastos obligatorios de transporte escolar'),
        ('D09', 'Depósitos en cuentas de ahorro, primas basadas en planes de pensiones'),
        ('D10', 'Pagos por servicios educativos (Colegiatura)'),
        ('P01', 'Para definir')])


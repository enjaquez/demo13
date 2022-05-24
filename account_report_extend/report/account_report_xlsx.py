# -*- coding: utf-8 -*-
from odoo import models, _
PAYMENT_STATE = {
    'not_paid': 'Not Paid',
    'in_payment': 'In Payment',
    'paid': 'paid'
}

class AccountReportXlsx(models.AbstractModel):
    _name = "report.account_report_extend.report_account_report_excel"
    _inherit = "report.report_xlsx.abstract"
    _description = "Reporte de Facturación"

    def generate_xlsx_report(self, workbook, data, wizard):
        sheet = workbook.add_worksheet("Reporte Facturas")
        i = 0
        j = 0

        TABLE_HEADER = [
            _('Fecha Factura'),
            _('Facrtura #'),
            _('Cliente'),
            _('Importe'),
            _('Costo'),
            _('Beneficio'),
            _('Margen %'),
            _('Estado del Pago')
        ]

        move_data = wizard._get_move_data_report_values()
        bold = workbook.add_format({"bold": True})

        for table in TABLE_HEADER:
            sheet.write(i, j, table, bold)
            j += 1

        for m in move_data:
            i += 1
            j = 0
            sheet.write(i, j, str(m.invoice_date), '')
            j += 1
            sheet.write(i, j, m.name or '', '')
            j += 1
            sheet.write(i, j, m.partner_id.name or '', '')
            j += 1
            sheet.write(i, j, m.amount_untaxed, '')
            j += 1
            sheet.write(i, j, m.cost_amount, '')
            j += 1
            sheet.write(i, j, m.profit, '')
            j += 1
            sheet.write(i, j, m.margin, '')
            j += 1
            sheet.write(i, j, PAYMENT_STATE[m.invoice_payment_state], '')
            j += 1

# -*- coding: utf-8 -*-

from odoo import models


class SubscriptionReportXLSX(models.AbstractModel):
    _name = 'report.easy_subscription_invoicement.subscriptions_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, _):
        subscription_model = self.env["sale.subscription"]
        subscriptions = subscription_model.search([])
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': 'green',
            'font_color': 'white',
            'align': 'left',
        })
        sheet = workbook.add_worksheet("Suscripciones")

        sheet.write(0, 0, "Suscripcion ID", header_format)
        sheet.write(0, 1, "Cliente", header_format)
        sheet.write(0, 2, "Referencia", header_format)
        sheet.write(0, 3, "Fecha proxima de facturacion", header_format)
        sheet.write(0, 4, "Fecha de cobro", header_format)

        for idx, subscription in enumerate(subscriptions):
            sheet.write(idx + 1, 0, u"{}".format(subscription.id))
            sheet.write(idx + 1, 1, u"{}".format(subscription.partner_id.name))
            sheet.write(idx + 1, 2, u"{}".format(subscription.code))
            sheet.write(idx + 1, 3, u"{}".format(subscription.recurring_next_date))
            sheet.write(idx + 1, 4, u"{}".format(subscription.next_payment_date))

# -*- coding: utf-8 -*-

from odoo import models


class SubscriptionReportXLSX(models.AbstractModel):
    _name = 'report.easy_subscription_invoicement.lead_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, _):
        lead_model = self.env["crm.lead"]
        subscription_model = self.env["sale.subscription"]
        leads = lead_model.search([
            ('partner_id', '!=', False),
        ])
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': 'green',
            'font_color': 'white',
            'align': 'left',
        })
        sheet = workbook.add_worksheet("Suscripciones")

        sheet.write(0, 0, "CRM ID", header_format)
        sheet.write(0, 1, "Cliente", header_format)
        sheet.write(0, 2, "Referencia de la suscripcion", header_format)
        sheet.write(0, 3, "Fecha de colocacion", header_format)
        sheet.write(0, 4, "Fecha de desinstalacion", header_format)

        for idx, lead in enumerate(leads):
            subscriptions = subscription_model.search([("partner_id", "=", lead.partner_id.id)])
            subscription = None
            for subscription_obj in subscriptions:
                subscription = subscription_obj
            sheet.write(idx + 1, 0, u"{}".format(lead.id))
            sheet.write(idx + 1, 1, u"{}".format(lead.partner_id.name))
            sheet.write(idx + 1, 2, u"{}".format(subscription.code if subscription else ""))
            sheet.write(idx + 1, 3, u"{}".format(
                lead.x_studio_fecha_y_hora_de_colocacin if lead.x_studio_fecha_y_hora_de_colocacin else ""
            ))
            sheet.write(idx + 1, 4, u"{}".format(
                lead.x_studio_fecha_de_desinstalacin if lead.x_studio_fecha_de_desinstalacin else ""
            ))

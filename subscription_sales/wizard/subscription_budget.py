# -*- coding: utf-8 -*-
 
from odoo import fields, models, api, _
import logging
from dateutil.relativedelta import relativedelta

_logger = logging.getLogger(__name__)

class SubscriptionBudgetWizard(models.TransientModel):
    _name = 'subscription.budget.wizard'
    _description =  'Wizard to show a resume of information to send to budgets'

    name = fields.Char()
    budget_id = fields.Many2one("crossovered.budget")
    date_from_affect = fields.Date(string='Date From', default=lambda self: fields.date.today().replace(day=1), readonly=True)
    date_to_affect = fields.Date(string='Date to', readonly=True)
    to_sent = fields.Float(string='Amount to sent')

    # @api.multi
    # @api.depends('budget_id')
    # def _get_total_by_active(self):
    #     amount_to_sent = 0.0
    #     today = fields.date.today()
    #     date_domain_start = today.replace(day=1)
    #     date_domain_end = date_domain_start + relativedelta(months=1) - relativedelta(days=1)
    #     suscription_ids = self.env["sale.subscription"].search(
    #         [('stage_id.in_progress', '=', True),
    #          ('recurring_next_date', '>=', date_domain_start),
    #          ('recurring_next_date', '<=', date_domain_end)])
    #     for subs in suscription_ids:
    #         amount_to_sent += subs.recurring_total
    #     self.date_from_affect = today

    @api.onchange('date_to_affect','date_from_affect','budget_id')
    def onchange_date_to(self):
        amount_to_sent = 0.0
        if self.date_from_affect and self.date_to_affect:
            suscription_ids = self.env["sale.subscription"].search(
                [('stage_id.in_progress', '=', True),
                 ('analytic_account_id.name', '=', self.budget_id.name),
                 ('recurring_next_date', '>=', self.budget_id.date_from),
                 ('recurring_next_date', '<=', self.budget_id.date_to)], order='recurring_next_date asc')

            for suscription in suscription_ids:
                final = True
                date_to_sus = suscription.recurring_next_date
                while final:
                    if date_to_sus > self.budget_id.date_to:
                        final = False
                    else:
                        periods = {'daily': 'days', 'weekly': 'weeks', 'monthly': 'months', 'yearly': 'years'}
                        invoicing_period = relativedelta(**{periods[suscription.template_id.recurring_rule_type]: suscription.template_id.recurring_interval})
                        date_to_sus = date_to_sus + invoicing_period
                        if suscription.pricelist_id.currency_id.name == 'USD':
                            amount_to_sent = amount_to_sent + suscription.recurring_total * 21
                        if suscription.pricelist_id.currency_id.name == 'MXN':
                            amount_to_sent = amount_to_sent + suscription.recurring_total

            # if suscription_ids:
            #     amount_to_sent= sum(suscription.recurring_total for suscription in suscription_ids)
        self.to_sent = amount_to_sent

    @api.onchange('budget_id')
    def onchange_budget(self):
        if self.budget_id:
            self.date_to_affect = self.budget_id.date_to



    @api.multi
    def send_to_budget(self):
        for record in self:
            list_dates = []
            date_domain_start = record.budget_id.date_from
            date_domain_first = date_domain_start.replace(day=1)
            date_domain_end = date_domain_first + relativedelta(months=1) - relativedelta(days=1)
            list_dates.append({'from':date_domain_start,'to':date_domain_end})
            budget_obj = self.env['crossovered.budget.lines']
            final = True
            analytic_account_id = self.env['account.analytic.account'].search([('name','=',record.budget_id.name)], limit=1)
            count = 1
            list_budg = {}
            while final:
                if date_domain_end > record.budget_id.date_to:
                    final = False
                else:
                    
                    list_dates.append({'from':date_domain_start,'to':date_domain_end})
                    obj = {
                        'name': record.budget_id.name,
                        'analytic_account_id': analytic_account_id.id,
                        'date_from':date_domain_start,
                        'date_to': date_domain_end,
                        'planned_amount': 0,
                        'crossovered_budget_id': record.budget_id.id
                    }
                    list_budg[count]=obj
                    date_domain_start = date_domain_end + relativedelta(days=1)
                    date_domain_end = date_domain_start + relativedelta(months=1) - relativedelta(days=1)
                    count += 1
                    #budget_obj.create(obj)


            suscription_ids = self.env["sale.subscription"].search(
                    [('stage_id.in_progress', '=', True),
                     ('analytic_account_id.name', '=', record.budget_id.name),
                     ('recurring_next_date', '>=', record.budget_id.date_from),
                     ('recurring_next_date', '<=', record.budget_id.date_to)], order='recurring_next_date asc')

            
            for suscription in suscription_ids:
                final = True
                date_to_sus = suscription.recurring_next_date
                count = 1
                while final:
                    if not list_budg.get(count):
                        final = False
                    else:
                        lines_per_month = list_budg.get(count)
                        if date_to_sus >= lines_per_month['date_from'] and date_to_sus <= lines_per_month['date_to']:
                            if suscription.pricelist_id.currency_id.name == 'USD':
                                lines_per_month['planned_amount'] = lines_per_month['planned_amount'] + suscription.recurring_total * 21
                            if suscription.pricelist_id.currency_id.name == 'MXN':
                                lines_per_month['planned_amount'] = lines_per_month['planned_amount'] + suscription.recurring_total
                            #lines_per_month['planned_amount'] = lines_per_month['planned_amount'] + suscription.recurring_total
                            periods = {'daily': 'days', 'weekly': 'weeks', 'monthly': 'months', 'yearly': 'years'}
                            invoicing_period = relativedelta(**{periods[suscription.template_id.recurring_rule_type]: suscription.template_id.recurring_interval})
                            date_to_sus = date_to_sus + invoicing_period
                    count +=1
                
            for conta in list_budg:
                if list_budg[conta]['planned_amount'] != 0:
                    budget_obj.create(list_budg[conta])


            #import pdb; pdb.set_trace()
            # for dates in list_dates:
            #     date_from = dates.get('from')
            #     date_to = dates.get('to')
            #     suscription_ids = self.env["sale.subscription"].search(
            #         [('stage_id.in_progress', '=', True),
            #          ('analytic_account_id.name', '=', record.budget_id.name),
            #          ('recurring_next_date', '>=', date_from),
            #          ('recurring_next_date', '<=', date_to)])
            #     if suscription_ids:
                    
            #         amount_to_sent= sum(suscription.recurring_total for suscription in suscription_ids)
            #         name = suscription_ids[0].code
            #         analytic_account_id = suscription_ids[0].analytic_account_id
            #         if not analytic_account_id:
            #             raise ValidationError(
            #                 _("Configure account analitic from %s ")% name)
            #         obj = {
            #             'name': name,
            #             'analytic_account_id': analytic_account_id.id,
            #             'date_from':date_from,
            #             'date_to': date_to,
            #             'planned_amount': amount_to_sent,
            #             'crossovered_budget_id': record.budget_id.id
            #         }
            #         budget_obj.create(obj)
            #budget_lines = record.budget_id.crossovered_budget_line.filtered(lambda line:  record.date_to_affect >= line.date_from and record.date_to_affect <= line.date_to )
            #budget_lines.write({'planned_amount': record.to_sent})
        return True


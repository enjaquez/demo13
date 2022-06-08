from odoo import models, fields, api
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import pytz
import calendar
from dateutil.rrule import rrule, MONTHLY
from calendar import month


def start_end_date_global(start, end, tz):
    tz = pytz.timezone(tz) or 'UTC'
    current_time = datetime.now(tz)
    hour_tz = int(str(current_time)[-5:][:2])
    min_tz = int(str(current_time)[-5:][3:])
    sign = str(current_time)[-6][:1]
    sdate = start + " 00:00:00"
    edate = end + " 23:59:59"
    if sign == '-':
        start_date = (datetime.strptime(sdate, '%Y-%m-%d %H:%M:%S') + timedelta(hours=hour_tz,
                                                                                minutes=min_tz)).strftime(
            "%Y-%m-%d %H:%M:%S")
        end_date = (datetime.strptime(edate, '%Y-%m-%d %H:%M:%S') + timedelta(hours=hour_tz,
                                                                              minutes=min_tz)).strftime(
            "%Y-%m-%d %H:%M:%S")
    if sign == '+':
        start_date = (datetime.strptime(sdate, '%Y-%m-%d %H:%M:%S') - timedelta(hours=hour_tz,
                                                                                minutes=min_tz)).strftime(
            "%Y-%m-%d %H:%M:%S")
        end_date = (datetime.strptime(edate, '%Y-%m-%d %H:%M:%S') - timedelta(hours=hour_tz,
                                                                              minutes=min_tz)).strftime(
            "%Y-%m-%d %H:%M:%S")
    return start_date, end_date


class CRMLead(models.Model):
    _inherit = "crm.lead"

    @api.model
    def get_crm_stages1(self, start, end, company_id):
        if company_id:
            pass
        else:
            company_id = self.env.user.company_id.id
        current_time_zone = self.env.user.tz or 'UTC'
        s_date, e_date = start_end_date_global(start, end, current_time_zone)
        sql_query = """SELECT 
                        ct.name AS name,
                        count(cl.id) as total
                        FROM crm_lead AS cl
                        INNER JOIN crm_stage AS ct ON ct.id = cl.stage_id
                        WHERE
                        cl.create_date::DATE >= '%s'
                        AND cl.create_date::DATE <= '%s'
                        GROUP BY ct.name
                """ % (s_date, e_date)
        self._cr.execute(sql_query)
        stages = self._cr.dictfetchall()
        print("stageskjkhjghfhfgf", stages)
        en_proceso = 0
        ratification = 0
        colocacion = 0
        ratificado = 0
        
        for each in stages:
            if each.get('name') == 'CONTRATO EN PROCESO' or each.get('name') == 'CONTRATO PRESENTADO':
                en_proceso += each.get('total')
            if each.get('name') == 'CON FECHA DE RATIFICACIÓN':
                ratification += each.get('total')
            if each.get('name') == 'CON FECHA DE COLOCACIÓN':
                colocacion += each.get('total')
            if each.get('name') == 'RATIFICADO':
                ratificado += each.get('total')

        return {'en_proceso': en_proceso, 'ratification': ratification, 'colocacion': colocacion, 'ratificado':ratificado}

    @api.model
    def get_crm_won_status1(self, start, end, company_id):
        if company_id:
            pass
        else:
            company_id = self.env.user.company_id.id
        current_time_zone = self.env.user.tz or 'UTC'
        s_date, e_date = start_end_date_global(start, end, current_time_zone)

        getyear = datetime.strptime(s_date, '%Y-%m-%d %H:%M:%S').year
        months = []
        start_date = datetime.strptime(s_date, '%Y-%m-%d %H:%M:%S') 
        end_date = datetime.strptime(e_date, '%Y-%m-%d %H:%M:%S') 

        while  start_date<= end_date:
            if start_date.strftime("%B") not in months:
                months.append(start_date.strftime("%B"))
            start_date += timedelta(weeks=1)
    
        print("yearjjjjjjjjjjjjjjjjjjj..............", getyear)
        print("month....................", months)
        sql_query = """SELECT 
                        cl.won_status AS name,
                        count(cl.id) as total
                        FROM crm_lead AS cl
                        WHERE
                        cl.won_status in ('pending', 'won')
                        AND cl.create_date::DATE >= '%s'
                        AND cl.create_date::DATE <= '%s'
                        GROUP BY cl.won_status
                """ % (s_date, e_date)
        self._cr.execute(sql_query)
        won_status = self._cr.dictfetchall()
        print("stageskjkhjghfhfgf", won_status)
        new = 0
        won = 0
        
        for each in won_status:
            if each.get('name') == 'pending':
                new += each.get('total')
            if each.get('name') == 'won':
                won += each.get('total')
        goals = self.env['crm.goal'].search([('year','=', str(getyear))], limit=1)
        total_goals = goals.goal_ids.filtered(lambda x: x.name in months)
        total_goals = sum(i.goal for i in total_goals)
        print("total_goalsllllll....................", total_goals, total_goals - won)
        return {'new': new, 'won': won, 'goal': total_goals - won}

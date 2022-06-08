from odoo import models, fields, api
from datetime import datetime, date, timedelta


class CRMGoal(models.Model):
    _name = "crm.goal"
    _rec_name = 'year'

    _sql_constraints = [
        ('year_uniq', 'unique (year)', 'The Year must be unique !')
    ]

    def _get_years(self):
    	lst = []
    	for i in range(1990,2050):
    		lst.append((str(i), str(i)),)
    	return lst


    @api.model
    def default_get(self, fields):
        res = super(CRMGoal, self).default_get(fields)
        goals = [(0, 0, {'name': 'January'}),(0, 0, {'name': 'Febuary'}), (0, 0, {'name': 'March'}), (0, 0, {'name': 'April'}), (0, 0, {'name': 'May'}),(0, 0, {'name': 'June'}), (0, 0, {'name': 'July'}), (0, 0, {'name': 'August'}), (0, 0, {'name': 'September'}), (0, 0, {'name': 'October'}), (0, 0, {'name': 'November'}), (0, 0, {'name': 'December'})]
        res['goal_ids'] = goals
        return res

    year = fields.Selection(selection=_get_years, string="Year", default=datetime.now().year)
    goal_ids = fields.One2many('crm.goal.line', 'goal_id', string='Goals Configuration')


class CRMGoalConfiguration(models.Model):
	_name = 'crm.goal.line'

	goal_id = fields.Many2one('crm.goal', string='Goals')
	name = fields.Char(string='Month', required=True)
	goal = fields.Integer(string='Goal')




# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import requests
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class CrmKpis(models.Model):
    _name = 'odoo_kpis.crm'
    _description = 'KPIs definidos para el CRM'

    name = fields.Char(string='Descripción')
    op_cotizaciones_cuu = fields.Integer(string='Cotizaciones Chihuahua')
    op_cotizaciones_cdmx = fields.Integer(string='Cotizaciones CDMX')
    op_cerca_cierre = fields.Integer(string='Cerca del Cierre', compute="_get_op_cerca_cierre")
    op_proceso = fields.Integer(string='Contratos en Proceso', compute="_get_op_proceso")
    op_presentado = fields.Integer(string='Contratos Presentados', compute="_get_op_presentado")
    op_fecha_ratificacion = fields.Integer(string='Contrato con Fecha de Ratificación', compute="_get_op_fecha_ratificacion")
    op_ratificado = fields.Integer(string='Contratos Ratificados', compute="_get_op_ratificado")
    op_fecha_colocacion = fields.Integer(string='Contratos con Fecha de Colocación', compute="_get_op_fecha_colocacion")
    op_por_colocar = fields.Integer(string='Brazaletes por colocar', compute="_get_op_por_colocar")
    op_instalados = fields.Integer(string='Brazaletes instalados', compute="_get_op_instalados")
    op_desinstalados = fields.Integer(string='Brazaletes desinstalados')
    op_abogados = fields.Integer(string='Base de datos de abogados')

    #Ventas OP#
    #Webinars 2021#
    #Asistentes por webinar#

    def _get_op_cerca_cierre(self):
        sql = "SELECT count(id) AS cuenta FROM crm_lead WHERE stage_id='2' AND won_status='pending' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_cerca_cierre = result[0]

    def _get_op_proceso(self):
        sql = "SELECT count(id) AS cuenta FROM crm_lead WHERE stage_id='12' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_proceso = result[0]
    
    def _get_op_presentado(self):
        sql = "SELECT count(id) AS cuenta FROM crm_lead WHERE stage_id='10' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_presentado = result[0]
    
    def _get_op_fecha_ratificacion(self):
        sql = "SELECT count(id) AS cuenta FROM crm_lead WHERE stage_id='6' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_fecha_ratificacion = result[0]
    
    def _get_op_ratificado(self):
        sql = "SELECT count(id) AS cuenta FROM crm_lead WHERE stage_id='11' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_ratificado = result[0]

    def _get_op_fecha_colocacion(self):
        sql = "SELECT count(id) AS cuenta FROM crm_lead WHERE stage_id='7' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_fecha_colocacion = result[0]

    def _get_op_por_colocar(self):
        sql = "SELECT count(id) AS cuenta FROM crm_lead WHERE stage_id='3' OR stage_id='11' OR stage_id='12' OR stage_id='10' OR stage_id='7' OR stage_id='6' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_por_colocar = result[0]

    def _get_op_instalados(self):
        sql = "SELECT count(id) AS cuenta FROM auto_paquet_servicio WHERE paquete_ubicacion='56' AND active='t' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.op_instalados = result[0]

    def get_crm_1(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain':[('stage_id','=','CERCA DEL CIERRE -80%')],
            'context': '{"create" : "False"}'
        }

    def get_crm_2(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain':[('stage_id','=','CONTRATO EN PROCESO')],
            'context': '{"create" : "False"}'
        }

    def get_crm_3(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain':[('stage_id','=','CONTRATO PRESENTADO')],
            'context': '{"create" : "False"}'
        }

    def get_crm_4(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain':[('stage_id','=','CON FECHA DE RATIFICACIÓN')],
            'context': '{"create" : "False"}'
        }

    def get_crm_5(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain':[('stage_id','=','RATIFICADO')],
            'context': '{"create" : "False"}'
        }

    def get_crm_6(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain':[('stage_id','=','CON FECHA DE COLOCACIÓN')],
            'context': '{"create" : "False"}'
        }

    def get_crm_7(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain':[('stage_id','=',['NEGOCIO GANADO','RATIFICADO','CONTRATO EN PROCESO','CONTRATO PRESENTADO','CON FECHA DE COLOCACIÓN','CON FECHA DE RATIFICACIÓN'])],
            'context': '{"create" : "False"}'
        }

    def get_crm_8(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'CRM',
            'view_mode': 'tree,form',
            'res_model': 'auto.paquet.servicio',
            'domain':[('paquete_ubicacion','=','Externo/Clientes/OFPAY'),('active','=','True')],
            'context': '{"create" : "False"}'
        }

class IngKpis(models.Model):
    _name = 'odoo_kpis.ing'
    _description = 'KPIs definidos para Ingeniería'

    name = fields.Char(string='Descripción')
    ing_paq_completos_cuu = fields.Integer(string='Paquetes Completos Chihuahua', compute="_get_ing_paq_completos_cuu")
    ing_paq_completos_cdmx = fields.Integer(string='Paquetes Completos CDMX', compute="_get_ing_paq_completos_cdmx")
    ing_smart_tag_sueltos = fields.Integer(string='Smart Tag sueltos', compute="_get_ing_smart_tag_sueltos")
    ing_sim_gurtam_activos = fields.Integer(string='SIM en Equipos Gurtam activos', compute="_get_ing_sim_gurtam_activos")
    ing_sim_disponibles_inventario = fields.Integer(string='SIM disponibles en inventario', compute="_get_ing_sim_disponibles_inventario")
    ing_sim_inventario_telcel = fields.Integer(string='SIM inventario total Telcel', compute="_get_ing_sim_inventario_telcel")

    #Ventas OP#
    #Webinars 2021#
    #Asistentes por webinar#

    def _get_ing_paq_completos_cuu(self):
        sql = "SELECT count(id) AS cuenta FROM auto_paquet_servicio WHERE paquete_ubicacion='104' AND active='t' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.ing_paq_completos_cuu = result[0]

    def _get_ing_paq_completos_cdmx(self):
        sql = "SELECT count(id) AS cuenta FROM auto_paquet_servicio WHERE paquete_ubicacion='38' AND active='t' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.ing_paq_completos_cdmx = result[0]

    def _get_ing_smart_tag_sueltos(self):
        sql = "SELECT count(id) AS cuenta FROM stock_quant WHERE product_id='313' AND bandera='f' AND (location_id=16 OR location_id=26 OR location_id=32 OR location_id=38 OR location_id=104 OR location_id=110 OR location_id=199 OR location_id=204 OR location_id=207 OR location_id=213 OR location_id=219 OR location_id=225 OR location_id=244 OR location_id=250) "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.ing_smart_tag_sueltos = result[0]

    def _get_ing_sim_gurtam_activos(self):
        sql = "SELECT count(id) AS cuenta FROM stock_quant WHERE product_id='275' AND bandera='t' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.ing_sim_gurtam_activos = result[0]

    def _get_ing_sim_disponibles_inventario(self):
        sql = "SELECT count(id) AS cuenta FROM stock_quant WHERE product_id='275' AND bandera='f' AND proveedor='5978' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.ing_sim_disponibles_inventario = result[0]

    def _get_ing_sim_inventario_telcel(self):
        sql = "SELECT count(id) AS cuenta FROM stock_quant WHERE product_id='275' AND proveedor='5978' "
        self.env.cr.execute(sql)
        result = self.env.cr.fetchone()
        #raise ValidationError(result)
        self.ing_sim_inventario_telcel = result[0]

    def get_ing_1(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'GPS Monitor',
            'view_mode': 'tree,form',
            'res_model': 'auto.paquet.servicio',
            'domain':[('paquete_ubicacion.id','=','104'),('active','=','True')],
            'context': '{"create" : "False"}'
        }

    def get_ing_2(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'GPS Monitor',
            'view_mode': 'tree,form',
            'res_model': 'auto.paquet.servicio',
            'domain':[('paquete_ubicacion.id','=','38'),('active','=','True')],
            'context': '{"create" : "False"}'
        }

    def get_ing_3(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'GPS Monitor',
            'view_mode': 'tree,form',
            'res_model': 'stock.quant',
            'domain':['&',('product_id','=','Buddi Smart Tag'),('bandera','=','False'),('location_id.id','=',['16','26','32','38','104','110','199','204','207','213','219','225','244','250'])],
            'context': '{"create" : "False"}'
        }

    def get_ing_4(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'GPS Monitor',
            'view_mode': 'tree,form',
            'res_model': 'auto.paquet.servicio',
            'domain':[('sim_equipo','=','True'),('paquete_ubicacion','like','Cliente')],
            'context': '{"create" : "False"}'
        }

    def get_ing_5(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'GPS Monitor',
            'view_mode': 'tree,form',
            'res_model': 'stock.quant',
            'domain':['&',('product_id','=','Servicio GPRS (SIM)'),('bandera','=','False')],
            'context': '{"create" : "False"}'
        }

    def get_ing_6(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'GPS Monitor',
            'view_mode': 'tree,form',
            'res_model': 'stock.quant',
            'domain':['&',('product_id','=','Servicio GPRS (SIM)'),('proveedor','=','RADIO MOVIL DIPSA SA DE CV')],
            'context': '{"create" : "False"}'
        }


class Proyectado(models.Model):
    _name = 'odoo_kpis.proyectado'
    _description = 'Proyectado de Ingresos y Egresos'

    name = fields.Char(string='Descripción del Proyectado')
    unidad_negocio = fields.Many2one("account.analytic.account")
    sem1 = fields.Float(string='Semana 1')
    sem2 = fields.Float(string='Semana 2')
    sem3 = fields.Float(string='Semana 3')
    sem4 = fields.Float(string='Semana 4')
    mes1 = fields.Float(string='Jul 21')
    mes2 = fields.Float(string='Ago 21')
    mes3 = fields.Float(string='Sep 21')
    mes4 = fields.Float(string='Oct 21')
    mes5 = fields.Float(string='Nov 21')
    mes6 = fields.Float(string='Dic 21')
    mes7 = fields.Float(string='Ene 22')
    mes8 = fields.Float(string='Feb 22')
    mes9 = fields.Float(string='Mar 22')
    mes10 = fields.Float(string='Abr 22')
    mes11 = fields.Float(string='May 22')
    mes12 = fields.Float(string='Jun 22')
    proyectado = fields.Float(string='Proyectado')
    real       = fields.Float(string='Real')
    cobranza   = fields.Float(string='Cobranza')
    activo     = fields.Boolean(string='Activo')
    ingreso = fields.Boolean(String='Ingreso')




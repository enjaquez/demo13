# -*- coding: utf-8 -*-

from odoo import models, fields, api

class modelos_telcel_wizard_odoo(models.TransientModel):

    _name="menu_wizard.odoo_telcel"

    #borrar datos de la table o moldelo de carga de datos
    def action_limpiar_caraga(self):
        self._cr.execute("""DELETE FROM load_data_numeros_telcel""")
    #comparar la informacion del docuemento cargado de telcel con el de odoo
    def action_odoo(self):
        self._cr.execute("""DELETE FROM data_odoo_result""")
        #consulta para cargar todos lo del excel
        data_telcel=self.env['load_data_numeros.telcel'].search([])
        #deliminar la cantidad de informacion
        datas=self.env['stock.quant'].search([('quantity','>',0),('proveedor.id','=',5978)]).mapped('tele_sim')

        for record in data_telcel:
            if record['numero_tel'] not in datas:
                self.env['data_odoo.result'].create({
                               'numero_tel':record['numero_tel'],
                               })
            #else:
            #    self.env['stock.quant'].search([('quantity','>',0),('proveedor.id','=',5978)]).write({'proveedor':5978})





    #compar la informacion de odoo con el documento de telcel
    def action_telcel(self):
        self._cr.execute("""DELETE FROM data_telcel_result""")
        data_odoo_load=self.env['stock.quant'].search([('quantity','>',0),('tipo_produto','=','SIM')])
        for record in data_odoo_load:
            data_data=self.env['load_data_numeros.telcel'].search([('numero_tel','=',record['tele_sim'])])
            if data_data:
                pass
            else:
                self.env['data_telcel.result'].create({
                    'proveedor':record['proveedor'].name,
                    'numero_tel':record['tele_sim'],
                    'serie':record['lot_id'].name})

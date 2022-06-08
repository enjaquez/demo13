# -*- coding: utf-8 -*-

from odoo import models, fields, api

class compara_data(models.TransientModel):

    _name="comparar.data.load"
    #cantida = fields.Char(string="cantidad")
    @api.multi
    def compara(self):
        #limpiamos tabla para nueva comparacion
        self._cr.execute("""DELETE FROM data_odoo""")
        #cargar informacion de que se encuentra en la base de datos
        data_excel=self.env['data.data_load'].search_read([],['name','imel'])
        #recorre el documento de excel cargado
        Actualizado=0
        for record in data_excel:
            #buscar si existe el numero de serie en odoo
            data_db=self.env['auto.paquet.servicio'].search_read([('num_serie','=',record['imel']),('sim_equipo','=',True),('active','=',True)],['nombre','num_serie'])
            #self.env['data.data_load'].create({'excel_name':record['name'],'excel_imei':record['imel']})
            if data_db:
                if data_db[0]['nombre']!=record['name']:
                    self.env['auto.paquet.servicio'].search([('num_serie','=',record['imel']),('sim_equipo','=',True)]).write({'nombre':record['name']})
                    Actualizado=Actualizado+1
            else:
                self.env['data.odoo'].create({'name':record['name'],'imei':record['imel']})
        #self.cantida=Actualizado
        self.env['estadisticas.data_load'].create({'cantidad_act':Actualizado})

    @api.multi
    def def_archi(self):
        #limpimos tabla para nueva comparacion
        self._cr.execute("""DELETE FROM data_plataforma""")
        data_odoo=self.env['auto.paquet.servicio'].search_read([('sim_equipo','=',True),('active','=',True)],['nombre','num_serie'])
        for record in data_odoo:
            data_odoo=self.env['data.data_load'].search_read([('imel','in',record['num_serie'])],['name','imel'])
            print(data_odoo)
            if data_odoo:
                pass
            else:
                if record['num_serie']:
                    self.env['data.plataforma'].create({'name':record['nombre'],'imei':record['num_serie'][1]})
                else:
                    self.env['data.plataforma'].create({'name':record['nombre']})

    @api.multi
    def borrar(self):
        self._cr.execute("""DELETE FROM data_data_load""")

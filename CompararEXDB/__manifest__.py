# -*- coding: utf-8 -*-
{
    'name': "cmp_db_excel",

    'summary': """
        comparar el fichero con la base de datos
        """,

    'description': """
        1. Tener definido el campo que se caompara con el del fichero
        2. De alguna manera cargar la informacion o el excel que se comparar
        3. compara el numero de serie con los de la bas de datos
        4. verificar que la exitencia de los paquete de la base de datos asi como el excel
        5. si existe y el nombre con la que esta rigistrado la sim es difetene se replaza el nombre de paquete
    """,

    'author': "Sursoom",
    'website': "http://sursoom.mx/",


    # for the full list
    'category': 'Inventario de stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
         'views/menu.xml',
         'views/estadisticas.xml',
         'views/carga_data.xml',
         'views/odoo_data.xml',
         'views/plataforma_data.xml',
         'wizard/ventana.xml',
    ],

}

# -*- coding: utf-8 -*-
#Módulo creado por Ing. Industrial Hermes Colina
{
    'name': "Paquete_timna",

    'summary': """
        Conjunto de modificaciones a modulos estandar de Odoo""",

    'description': """
        
        Motivo: Este campo estara en la plantilla de presupuesto en el menu Analisis de presupuesto
        
    """,

    'author': "Ing. Hermes Colina",
    'website': "https://contablesag.com",
    
    #Siempre se debe agregar los módulos de los que depende el nuevo módulo para evitar errores
    #inesperados. (Ej. TypeError, ¡tal módulo no existe!)
    'depends': ['base', 'account_accountant', 'account_budget'],

    # Siempre cargar
    'data': [
        'view/motivo.xml',
        'view/ejecutado.xml',
    ],

    # Solo carga los datos de demostracion
    #'demo': [
    #    'demo/demo.xml',
    #],
    
    'installable': True,
    'application': True,
    'auto_install': False,

    #'qwe': [
    #    'view/motivo.xml',
    #],

    'license': 'LGPL-3',
}
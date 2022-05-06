# -*- coding: utf-8 -*-
#Módulo creado por Ing. Industrial Hermes Colina
{
    'name': "Paquete_grupo_kamy",

    'summary': """
        Conjunto de modificaciones en el estandar de Odoo""",

    'description': """
        
        En este modulo se añadiran un conjunto de campos adicionales en las plantillas de productos, informes y plantillas de lote
        
        1. Plantilla productos:
        
        Estado de inventario
        Modelo
        Capacidad
        Marca
        Accesorio/repuesto de
        Equipo compuesto
        
        2. Lotes/numeros de serie
        
        Marca (Many2one)
        Modelo (Many2one)
        Capacidad (Many2one)
        Fabricacion
        
        3. Informe de inventario
        
        Cantidad por unidad
        cantidad total
        Capacidad
        Equipo compuesto
        Estado
        Marca (Many2one)
        Modelo (many2one)
        fecha de fabricacion
    """,

    'author': "Ing. Hermes Colina",
    'website': "https://contablesag.com",
    
    #Siempre se debe agregar los módulos de los que depende el nuevo módulo para evitar errores
    #inesperados. (Ej. TypeError, ¡tal módulo no existe!)
    'depends': ['base', 'stock'],

    # Siempre cargar
    'data': [
        'view/producto.xml',
        'view/lote.xml',
        'view/informe.xml',
    ],

    # Solo carga los datos de demostracion
    #'demo': [
    #    'demo/demo.xml',
    #],
    
    'installable': True,
    'application': True,
    'auto_install': False,

    #'qweb': [
    #    'static/src/bugfix/bugfix.xml',
    #    'static/src/xml/hr_templates.xml',
    #],

    'license': 'LGPL-3',
}
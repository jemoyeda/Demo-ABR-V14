# -*- coding utf-8 -*-

{

    'name': "Libreria Odoo",
    'description': "Este modulo se usa para registgrar en una base de datos los libros, por tanto es un modulo personalizado. Autor: Ing. Hermes Colina",
    'summary': "Este modulo se puede instalar en Enterprise y SH",
    'author': 'Ing. Hermes Colina',
    'Category': 'General',
    'Version': '1.0.0.0',
    'depends':['hr'],
    'data':[

            'views/menu_view.xml',
            'views/libros_view.xml',
            'views/hr_employee_view.xml',
            'security/libreria_security.xml',
            'security/ir.model.access.csv',
        ],
    

}

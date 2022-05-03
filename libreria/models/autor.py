from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name = 'autor'
    _rec_name = 'last_name'

    name = fields.Char(string="Autor", required=True)
    last_name = fields.Char(string="Apellido", required=True)
    
    
    
    

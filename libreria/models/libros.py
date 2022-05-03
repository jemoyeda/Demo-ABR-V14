from tkinter import commondialog
from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name = 'libros'
    

    name = fields.Char(string="Nombre del libro", required=True)
    editorial = fields.Char(string="editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name='autor', string="Autor", required=True)
    apellido_autor = fields.Many2one(related='autor_id.last_name', string="Apellido del autor")
    imagen = fields.Binary(string="Imagen")
    
    
    
    

from odoo import models, fields, api

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name = 'libros'
    
#Campos del modulo creado
    supervisor_id = fields.Many2one(comodel_name='hr_employee', string="Supervisor")
    name = fields.Char(string="Nombre del libro", required=True)
    editorial = fields.Char(string="editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name='autor', string="Autor", required=True)
    lastname_autor = fields.Char(related='autor_id.last_name', string="Apellido del autor")
    imagen = fields.Binary(string="Imagen")
    description = fields.Char(string="Descripcion", compute="_compute_description")

#Funciones de campos calculados    
    @api.depends('name', 'editorial', 'lastname_autor')        #Se coloca el api.depends para mejorar la actualizacion de datos del campo computado
    def _compute_description(self):
        self.description = self.name + " es de la editorial " + self.editorial + " y escrito por " + self.lastname_autor
    
    
    
    

from odoo import models, fields, api

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    
    id_suprevisor = fields.Boolean(string="Es supervisor")
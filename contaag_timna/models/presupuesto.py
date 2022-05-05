from odoo import models, fields

class motivo(models.Model):
      _inherit = 'crossovered.budget.lines'
      
      motivo = fields.Text(string="Motivo")
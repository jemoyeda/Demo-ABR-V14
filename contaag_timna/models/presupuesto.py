from odoo import models, fields, api 

class motivo(models.Model):
      _inherit = 'crossovered.budget.lines'
      
      motivo = fields.Text(string="Motivo")

class ejecutado(models.Model):
      _inherit = 'crossovered.budget.lines'
      
      ejecutado = fields.Float(string="Importe Ejecutado", compute='_compute_ejecutado')
      
      @api.depends('practical_amount', 'planned_amount')
      def _compute_ejecutado(self):
            for record in self:
                  if record[('planned_amount')] == 0:
                        record[('ejecutado')] = 0
                  else:
                        record[('ejecutado')] = abs(record.practical_amount/record.planned_amount)
      
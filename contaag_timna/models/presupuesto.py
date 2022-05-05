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
                        
class desviacion(models.Model):
      _inherit = 'crossovered.budget.lines'
      
      desviacion = fields.Float(string="Desviacion", compute='_compute_desviacion')
      
      @api.depends('practical_amount', 'planned_amount')
      def _compute_desviacion(self):
            for record in self:
                  if record[('planned_amount')] == 0:
                        record[('x_desviacion')] = 0
                  else:
                        if record[('practical_amount')] == 0:
                              record[('x_desviacion')] = -1
                        else:
                              record[('x_desviacion')] = (record.practical_amount / record.planned_amount) + 1
      
      
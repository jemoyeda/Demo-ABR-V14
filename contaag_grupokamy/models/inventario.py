from odoo import models, fields, api

class producto(models.Model):
    _inherit = 'product.template'
    
    modelo = fields.Char(string="Modelo")
    aplica = fields.Char(string="Aplica")
    capacidad = fields.Char(string="Capacidad")
    cantidad_unidad = fields.Float(string="Cantidad por Unidad")
    equipo = fields.Selection([('Si', 'No')])
    estado = fields.Selection([('Verificado', 'No Verificado')])
    marca = fields.Char(string="Marca")
    
class lote(models.Model):
    _inherit = 'stock.production.lot'
    
    lote_capacidad = fields.Char(string="Capacidad")
    lote_equipos_compuestos = fields.Char(string="Equipos Compuestos")
    lote_estado = fields.Selection([('Perfecto', 'Defectuoso', 'Incompleto', 'Con Parte(s) Defectuosa(s)', 'En Reparacion', 'En Revision', 'Por Garantia')])
    lote_fecha_fabricacion = fields.Date(string="Fecha de Fabricacion")
    lote_marca = fields.Char(string="Marca")
    lote_modelo = fields.Char(string="Modelo")

class informe(models.Model):
    _inherit = 'stock.quant'
    
    informe_cantidad_unidad = fields.Float(related='product_id.cantidad_unidad', string="Cantidad por Unidad")
    informe_cantidad_total = fields.Float(string="Cantidad Total", compute='_compute_cantidad_total')
    informe_capacidad = fields.Char(related='product_id.capacidad', string="Capacidad")
    informe_equipo_compuesto  = fields.Char(related='product_id.equipo', string="Equipo Compuesto")
    informe_estado = fields.Char(related='product_id.estado', string="Estado")
    informe_marca = fields.Char(related='product_id.marca', string="Marca")
    informe_modelo = fields.Char(related='product_id.modelo', string="Modelo")
    informe_fecha_fabricacion = fields.Char(related='lot_id.lote_fecha_fabricacion', string="Fecha de fabricacion")
    
    #Calcular cantidad total de inventario en el modelo informe
    @api.depends('available_quantity', 'informe_cantidad_unidad')
    def _compute_cantidad_total(self):
        for record in self:
            if record['informe_cantidad_unidad'] == 0 :
                record['informe_cantidad_total'] = record['available_quantity']
            else:
                record['informe_cantidad_total'] = record['informe_cantidad_unidad'] * record['available_quantity']
    
    
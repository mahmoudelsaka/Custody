# -*- coding: utf-8 -*-
import time
from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import datetime


class custody(models.Model):
    _name = 'custody.custody'
    _rec_name = 'employee'
    _order = 'date desc'
    _inherit = ['mail.thread']

    employee = fields.Many2one('hr.employee', 'Employee', track_invisiblty='onchange', required='1')
    equipment_id = fields.Many2one('custody.equipment', 'Equipment', track_invisiblty='onchange', required='1',domain=[('is_open','=',False)],track_visibility='onchange',)
    department = fields.Many2one('hr.department', 'Department')
    date = fields.Datetime('Request Date',default=lambda *a: time.strftime('%Y-%m-%d %H:%M:%S',), track_invisiblty='onchange')
    partner_id = fields.Many2one('res.partner', 'Partner', track_invisiblty='onchange')
    deliv_date = fields.Datetime('Delivery Date',
                                 states={'delivery': [('readonly', '1')]}, track_invisiblty='onchange')
    state = fields.Selection(selection=[('new', 'New'), ('progress', 'In Progress'), ('delivery', 'Deliverd'),
                                        ('cancel', 'Canceled'), ('close', 'Closed')], track_invisiblty='onchange', default='new')


    @api.onchange("employee")
    def onchange_employee(self):
        if self.employee:
            self.department = self.employee.id



    @api.multi
    def action_new(self):
        self.state = 'new'

    @api.multi
    def action_progress(self):
        self.state = 'progress'
        

    @api.multi
    def action_delivery(self):
        self.deliv_date = datetime.now()
        self.state = 'delivery'


    @api.multi
    def action_cancel(self):
        self.equipment_id.is_open = False
        self.state = 'cancel'

    @api.multi
    def action_close(self):
        self.equipment_id.is_open = False
        self.state = 'close'

    @api.model
    def create(self, vals):
        newrecord = super(custody, self).create(vals)
        newrecord.equipment_id.is_open=True
        print (newrecord.equipment_id, newrecord.equipment_id.is_open)
        return newrecord



class CustodyEquipment(models.Model):
    _name = 'custody.equipment'
    _rec_name = 'equipment'
    _inherit = ['mail.thread' ]
    equipment = fields.Char('Name', required='1')
    code = fields.Char('Code', required='1')
    serial = fields.Char('Serial Num', track_invisiblty='onchange')
    bio = fields.Text('Bio', track_visibility='onchange',)
    category_id = fields.Many2one('equipment.category', 'Category', track_visibility='onchange',)
    item_id = fields.Many2many('equipment.item',string='Item')
    item_ids = fields.One2many(comodel_name="equipment.item.line", inverse_name="equip", required=False,string='Item' )
    value = fields.Text('Value')
    is_open=fields.Boolean('Open?')



class EquipmentItemLINE(models.Model):
    _name = 'equipment.item.line'
    _rec_name = 'items'
    items= fields.Many2one(comodel_name="equipment.item", string='Item', track_invisiblty='onchange')
    code_id = fields.Char(string="ID",related="items.code")
    value_id = fields.Char(string="Value", track_invisiblty='onchange')
    equip = fields.Many2one(comodel_name="custody.equipment", string="Equipment", required=False, )





class EquipmentCategory(models.Model):
    _name = 'equipment.category'
    _rec_name = 'category'
    _inherit = ['mail.thread']
    category = fields.Char('Name', required='1', track_visibility='onchange',)
    code = fields.Char('Code', required='1', track_visibility='onchange')


class EquipmentItem(models.Model):
    _name = 'equipment.item'
    _rec_name = 'item'
    _inherit = ['mail.thread']
    item = fields.Char('Name', required='1', track_visibility='onchange',)
    code = fields.Char('ID', required='1', track_visibility='onchange',)
    value=fields.Char('Value')


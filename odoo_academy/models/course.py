# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Diego Course'
    
    name = fields.Char(String='Name', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                             selection=[('beginner', 'Beginner'),
                                       ('intermediate', 'Intermediate'),
                                       ('expert', 'Expert')],
                             copy=False)
    
    active = fields.boolean(string='Active', default=True)
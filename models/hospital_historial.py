# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Historial(models.Model):
    _name = 'hospital_historial'

    codi = fields.Integer(
        string='Codi',
        required=True,
        size=12
    )

    hospital_visital_id = fields.Many2one("hospital_visita",string="Visita")
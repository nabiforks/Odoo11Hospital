# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Historial(models.Model):
    _name = 'hospital_visita'

    data = fields.Char(
        string='Data',
        required=True,
        size=12
    )


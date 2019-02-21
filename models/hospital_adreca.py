# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Adreca(models.Model):
    _name = "hospital_adreca"

    ciutat = fields.Char(
        string='Ciutat',
        size=12
    )
    codiPostal = fields.Integer(
        string='Codi Postal',
        size=12
    )
    carrer = fields.Char(
        string='Carrer',
        size=12
    )
    numero = fields.Integer(
        string='Número',
        size=12
    )
    planta = fields.Char(
        string='Planta',
        size=12
    )
    porta = fields.Char(
        string='Porta',
        size=12
    )
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Malaltia(models.Model):

    _name = "hospital_malaltia"

    codi = fields.Integer(
    string='Codi',
    required=True,
    size=12
    )

    nom = fields.Char(
    string='Nom',
    size=12
    )

    causaBaixa = fields.Boolean(string="Causa baixa?")

    tractament = fields.Char(
    string='Tractament',
    size=30
    )

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hospital(models.Model):
    _name = "hospital"

    name = fields.Char(string = "Nom")
    active = fields.Boolean("És actiu?")
    hospital_metge_id = fields.Many2many("hospital_metge",string="Metge Hospital")
    hospital_persona_id = fields.Many2many("hospital_persona",string="Persona Hospital")
    hospital_adreca_id = fields.Many2one("hospital_adreca",string="Adreça Hospital")
    hospital_malaltia_id = fields.Many2many("hospital_malaltia",string="Malaltia Hospital")

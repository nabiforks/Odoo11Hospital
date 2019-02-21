# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Metge(models.Model):
    _name = "hospital_metge"

    nom = fields.Char(
        string='Nom',
        size=15
    )
    cognom1 = fields.Char(
        string='Primer cognom',
        size=15
    )
    cognom2 = fields.Char(
        string='Segon cognom',
        size=15
    )
    numSegSocial = fields.Char(
        string='Seg Social',
        size=12
    )
    nif = fields.Char(
        string='NIF',
        required=True,
        size=9
    )
    telefon = fields.Char(
        string='Telèfon',
        size=12
    )
    _numEmpleat = fields.Integer(
        string='N Empleat',
    )
    _salariMensual = fields.Integer(
        string='Salari Mensual',
    )
    _codiCompteCorrent = fields.Char(
        string='Codi Compte Corrent',
        size=24,
    )

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PokedexType(models.Model):
    _name = 'partner_pokedex.type'

    name = fields.Char()
    color = fields.Integer()
    


# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PokedexMoves(models.Model):
    _name = 'partner_pokedex.move'
    name = fields.Char()
    Power = fields.Char()
    type = fields.Many2one('partner_pokedex.type')
    pokedex_id = fields.Many2one('partner_pokedex.pokedex')
    

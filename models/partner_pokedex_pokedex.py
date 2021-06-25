# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pokedex(models.Model):
    _name = 'partner_pokedex.pokedex'
    _parent_store = True
    name = fields.Char()
    height = fields.Float()
    weight = fields.Float()
    description = fields.Text()
    type = fields.Many2many('partner_pokedex.type')
    image = fields.Binary()
    partner_id = fields.Many2one('res.partner')

    moves_ids = fields.One2many('partner_pokedex.move', 'pokedex_id')
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)
    parent_id = fields.Many2one(
        'partner_pokedex.pokedex',
        ondelete='restrict',
        index=True)

    child_ids = fields.One2many(
        'partner_pokedex.pokedex', 'parent_id'
    )

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError(
                'Error! You cannot create recursive categories.')



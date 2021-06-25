# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    # pokedex_ids = fields.One2many('partner_pokedex.pokedex', 'partner_id')
    pokedex_ids = fields.Many2many('partner_pokedex.pokedex')
    # pokedex_ids = fields.Many2one('partner_pokedex.pokedex')

    @api.multi
    def evolve_pokemon(self):
        return {
            'name': 'Evolve Pokemon',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'partner_pokedex.evolve',
            # pass the id,
            'context': {
                # for passing Many2One field context value in Wizard form view
                'partner_id': self.id,
                'pokedex_ids': self.pokedex_ids.ids,               
            },
            # 'res_id': message_id.id,
            'target': 'new'
        }

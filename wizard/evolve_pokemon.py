from odoo.exceptions import ValidationError
from odoo import _, api, fields, models


class EnvolvePokemon(models.TransientModel):
    _name = 'partner_pokedex.evolve'
    _description = 'New Description'

    
    def _get_current_pokemon(self):
        selection=[]
        if 'partner_id' in self._context:
            pokemons=self.env['res.partner'].browse(self._context['partner_id']).pokedex_ids
            for pokemon in pokemons:
                selection.append((pokemon.id,pokemon.name))
        return selection

    def _selection_filter(self):      
        if self.pokedex_ids_c:
            self.pokedex_ids_e=self.env['partner_pokedex.pokedex'].search([('parent_id','in',[self.pokedex_ids_c])]).id
        print(self)
            

    confirmation = fields.Boolean()    
    pokedex_ids_c = fields.Selection(_get_current_pokemon)
    
    pokedex_ids_e = fields.Many2one('partner_pokedex.pokedex')



    @api.onchange('pokedex_ids_c')
    def _onchange_pokedex_ids_c(self):
        self._selection_filter()


    @api.multi
    def evolve_pokemon(self):
        if self.confirmation:
            if 'partner_id' in self._context and self.pokedex_ids_e and int(self.pokedex_ids_c):
                pokemons=self.env['res.partner'].browse(self._context['partner_id'])
                pokemons.pokedex_ids=[(3,int(self.pokedex_ids_c))]
                pokemons.pokedex_ids = [(4, self.pokedex_ids_e.id)] 
                print(pokemons.pokedex_ids)
            else:
                raise ValidationError("You must select at least one pokemon")

        else:
            raise ValidationError("You must confirm the evolution of your pokemon")


                




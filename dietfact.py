

class Dietfacts_product_template(models.Model) :
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer('Calories')
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Datetime('Serving Size')

class Dietfacts_res_users_meal(models.Model) :
    _name = 'res.users.meal'
    name = fields.Char('Meal name')
    meal_date = fields.Datetime('Meal Date')
    item_ids = fields.One2many('res.users.mealitem' , 'meal_id')
    user_id = fields.Many2one('res.users','Meal USer')

    @api.one
    @api.depends('item_ids' , 'item.id.servings')

    def _calccalories(self):
        currentcalories = 0
        for mealitem in self.item_ids :
            currentcalories += mealitem.item_id.calories
        self.totalcalories = currentcalories

    totalcalories = fields.Integer(string='Total Calories' , store = True , compute='_calccalories')
    notes = fields.Text('Meal Notes')

class Dietfacts_res_users_mealitem(models.Model) :
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one('product.template','Meal Item')
    servings = fields.Float('Servings')
    calories = fields.Integer(related='item_id.calories', string='Calories per Serving' , store = True , readonly = True)
    notes = fields.Text('Meal item notes')
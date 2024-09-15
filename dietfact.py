

class Dietfacts_product_template(models.Model) :
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer('Calories')
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Datetime('Last updated')
    nutrient_ids = fields.One2many('product.template.nutrient','product_id','Nutrients')

class Dietfacts_res_users_meal(models.Model) :
    _name = 'res.users.meal'
    name = fields.Char('Meal name')
    meal_date = fields.Datetime('Meal Date')
    item_ids = fields.One2many('res.users.mealitem' , 'meal_id')
    user_id = fields.Many2one('res.users','Meal USer')


    @api.depends('item_ids' , 'item_ids.servings')

    def _calccalories(self):
        currentcalories = 0
        for mealitem in self.item_ids :
            currentcalories += mealitem.calories * mealitem.servings
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

class Dietfacts_product_nutrient(models.Model) :
    _name = 'product.nutrient'
    name = fields.Char('Nutrient Name')
    uom_id = fields.Many2one('product.uom','Unit of Measure')
    description = fields.Text('Description')

class Dietfacts_product_template_nutrient(models.Model) :
    _name = 'product.template..nutrient'
    nutrient_id = fields.Many2one('product.nutrient' , string='Product Nutrient')
    product_id = fields.Many2one('product.template')
    uom = fields.String(related='nutrient_id.name' , string = 'UOM' , readonly = True)
    value = fields.Float('Nutrient Value')
    dailypercent = fields.Float('Daily recommended Value')
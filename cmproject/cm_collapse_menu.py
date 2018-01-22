
from odoo import models, fields, api, _

class collapse_menu(models.TransientModel):
    _name = 'collapse.menu'

    @api.model
    def customize_collapse_menus(self):
        self._cr.execute("""select distinct parameterize_menu_collapse.main_menus 
                        from parameterize_menu_collapse
                        inner join ir_model_data on parameterize_menu_collapse.main_menus = ir_model_data.res_id
                        where parameterize_menu_collapse.collapse_true = true""")
        menus = self._cr.fetchall()
        list_test = []
        if menus:
            for menu in menus:
                list_test.append(menu[0])
        print list_test
        return list_test


class parameterize_menu_collapse(models.Model):
    _name = 'parameterize.menu.collapse'

    @api.multi
    def _get_menus_with_child(self):
        self._cr.execute("""select ir_ui_menu.id from ir_ui_menu 
					inner join ir_model_data 
					on ir_ui_menu.id = ir_model_data.res_id
					inner join ir_module_module 
					on ir_model_data.module = ir_module_module.name 
					where ir_model_data.model = 'ir.ui.menu'
					and ir_ui_menu.parent_id is null 
					and ir_module_module.state = 'installed' """)
        menus = self._cr.fetchall()
        search_ids = []
        for menu in menus:
            search_ids.append(menu[0])
        domain= [('id', 'in', search_ids)]
        return domain

    collapse_true = fields.Boolean('Collapse')
    main_menus = fields.Many2one('ir.ui.menu','Module',domain = _get_menus_with_child)



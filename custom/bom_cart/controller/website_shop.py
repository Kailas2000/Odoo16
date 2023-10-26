from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteShop(WebsiteSale):

    @http.route(['/shop/cart'], type='http', auth="public", website=True)
    def cart(self, access_token=None, revive='', **post):
        bom_cart = request.env['ir.config_parameter'].sudo().get_param(
            'bom_cart.bom_cart')
        print(bom_cart, 'she')
        bom_pros = request.env['ir.config_parameter'].sudo().get_param(
            'bom_cart.bom_products_ids').split(',')
        setting_products = []
        try:
            for id in range(len(bom_pros)):
                if id == 0:
                    first_split = bom_pros[id].split('[')
                    setting_products.append(int(first_split[1]))
                elif id == len(bom_pros) - 1:
                    second_split = bom_pros[id].split(']')
                    setting_products.append(int(second_split[0]))
                else:
                    setting_products.append(int(bom_pros[id]))
            print(setting_products, 'settings products')
        except:
            pass

        cart_products = request.website.sale_get_order().order_line.product_template_id
        print(cart_products, 'cart products')
        bom_product_list = []
        for data in cart_products:
            if data.id in setting_products:
                if data.bom_ids:
                    print(data.bom_ids)
                    bom_line_products = []
                    for records in data.bom_ids.bom_line_ids:
                        bom_line_products.append(records.product_tmpl_id.name)
                    bom_product_list.append({
                        'product_id': data.bom_ids.product_tmpl_id.id,
                        'bom_products': bom_line_products
                    })
                    print(bom_product_list)
        res = super(WebsiteShop, self).cart(access_token=access_token,
                                            revive=revive, **post)
        res.qcontext['bom_line_products'] = bom_product_list
        print(res.qcontext, 'context')
        return res


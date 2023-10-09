from odoo.http import Controller, request, route


class Partner(Controller):
    @route('/partner', auth='public', website=True)
    def partner(self):
        print("hello", request.env.uid)
        country_ids = request.env['res.country'].search([])
        return request.render('website_session.website_partner_template',
                              {'country_ids': country_ids})

    @route('/create/partner', auth='public', website=True)
    def create_partner(self, name, email, **kw):
        print("create", kw)
        partner_id = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email,
            'phone': kw.get('phone'),
            'street': kw.get('street'),
            'country_id': kw.get('country'),
        })
        partner_ids = request.env['res.partner'].sudo().search([], limit=4, order='create_date desc')
        return request.render('website_session.website_partner_success_template',
                              {'partner_id': partner_id, 'partner_ids': partner_ids})

    @route(['''/view/partner/<model("res.partner"):partner>'''], auth='user', website=True)
    def view_partner(self, partner):
        print('partner', partner)
        return request.render('website_session.website_partner_view_template', {'partner': partner})
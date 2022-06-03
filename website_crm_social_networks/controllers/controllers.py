from odoo import http
from odoo.http import request

customer_per_page = 20


class WebsiteCrmSocialNetworks(http.Controller):
    @http.route(
        ["/my_customers", "/my_customers/page/<int:page>"],
        type="http",
        auth="public",
        website=True,
    )
    def my_customers(self, page=0, **post):
        Partner = request.env["res.partner"]
        search_value = post.get("search")
        domain = [("active", "=", True), ("parent_id", "=", False)]
        if search_value:
            domain += [
                "|",
                "|",
                ("name", "ilike", search_value),
                ("facebook_account", "ilike", search_value),
                "|",
                ("twitter_account", "ilike", search_value),
                ("linkedin_account", "ilike", search_value),
            ]

        # pager
        url = "/my_customers"
        partner_count = Partner.sudo().search_count(domain)
        pager = request.website.pager(
            url=url,
            total=partner_count,
            page=page,
            step=customer_per_page,
            scope=7,
            url_args=post,
        )
        partners = Partner.sudo().search(
            domain, offset=pager["offset"], limit=customer_per_page
        )

        values = {"partners": partners, "pager": pager, "post": post}

        return request.render(
            "website_crm_social_networks.partner_social_networks", values
        )

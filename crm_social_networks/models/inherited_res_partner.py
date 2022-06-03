from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    profile_complete = fields.Boolean(
        "Profile Complete", compute="_compute_profile_complete", store=True
    )
    facebook_account = fields.Char("Facebook Account")
    twitter_account = fields.Char("Twitter Account")
    linkedin_account = fields.Char("LinkedIn Account")

    @api.depends("facebook_account", "twitter_account", "linkedin_account")
    def _compute_profile_complete(self):
        for partner in self:
            partner.profile_complete = not (
                not partner.facebook_account
                or not partner.twitter_account
                or not partner.linkedin_account
            )

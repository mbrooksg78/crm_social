from odoo.tests import common, tagged


@tagged("post_install")
class SearchTest(common.SingleTransactionCase):
    def setUp(self, *args, **kwargs):
        super(SearchTest, self).setUp(*args, **kwargs)

        admin_user = self.env.ref("base.user_admin")
        self.ResPartner = self.env["res.partner"].with_user(admin_user)
        self.partner_complete = self.ResPartner.create(
            {
                "name": "Complete Profile User",
                "facebook_account": "ksdjlsajdlaj",
                "twitter_account": "jdasjadljs",
                "linkedin_account": "sdasdasdna",
            }
        )
        self.partner_partial = self.ResPartner.create(
            {
                "name": "Complete Profile User",
                "facebook_account": "ksdjlsajdlaj",
                "twitter_account": "jdasjadljs",
            }
        )
        self.partner_empty = self.ResPartner.create({"name": "Complete Profile User",})

    def test_01_compute_profile_complete(self):
        self.assertEqual(self.partner_complete.profile_complete, True, "Expected True")

    def test_02_check_compute_profile_incomplete(self):
        self.assertEqual(self.partner_partial.profile_complete, False, "Expected False")
        self.assertEqual(self.partner_empty.profile_complete, False, "Expected False")

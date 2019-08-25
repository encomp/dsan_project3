import unittest

from problem7.Route import Router


class RouterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.root_handler = "root handler"
        self.error_handler = "not found handler"
        self.router = Router(self.root_handler, self.error_handler)
        self.router.add_handler("/home/about", "about handler")
        self.router.add_handler("/home/help", "help handler")
        self.router.add_handler("/home/help/customer/support", "customer support handler")

    def test_root_handler(self):
        self.assertEqual(self.root_handler, self.router.lookup("/"))

    def test_home_handler_is_not_present(self):
        self.assertEqual(self.error_handler, self.router.lookup("/home"))

    def test_home_about_handler(self):
        self.assertEqual("about handler", self.router.lookup("/home/about"))

    def test_home_about_handler_with_trailing_separator(self):
        self.assertEqual("about handler", self.router.lookup("/home/about/"))

    def test_home_about_me_handler_is_not_present(self):
        self.assertEqual(self.error_handler, self.router.lookup("/home/about/me"))

    def test_home_help_handler(self):
        self.assertEqual("help handler", self.router.lookup("/home/help"))

    def test_home_help_customer_support_handler(self):
        self.assertEqual("customer support handler", self.router.lookup("/home/help/customer/support"))
        self.assertEqual("customer support handler", self.router.lookup("/home/help/customer/support/"))


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.loader import makeSuite
from add_player_invalid_test_data import TestAddANewPlayerInvalid
from add_player_valid_test_data import TestAddPlayer
from check_players_button import TestPlayersButton
from check_search_player_field import TestCheckSearchPlayer
from check_sign_out_button import TestCheckSignOut
from login_to_the_system import TestLoginPage
from test_cases.framework import TestMediumPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestMediumPage))
    test_suite.addTest(makeSuite(TestCheckSignOut))
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestAddANewPlayerInvalid))
    test_suite.addTest(makeSuite(TestPlayersButton))
    test_suite.addTest(makeSuite(TestCheckSearchPlayer))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())

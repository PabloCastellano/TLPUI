import unittest
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import os
os.environ['XDG_CONFIG_HOME'] = os.path.dirname(os.path.abspath(__file__)) + '/settings/default'
from tlpui import settings
from tlpui.file import read_tlp_file_config, get_json_schema_object_from_file


def get_config_count(categories):
    configcount = 0
    for category in categories:
        configs = category['configs']
        for config in configs:
            if 'group' in config:
                groupitems = config['ids']
                configcount += len(groupitems)
            else:
                configcount += 1
    return configcount


class MyTestCase(unittest.TestCase):
    def test_tlp_version_0_8(self):
        version = "0_8"
        settings.tlpconfig = read_tlp_file_config('test/default_tlp_config_files/tlp-config-{}'.format(version))
        jsoncategories = get_json_schema_object_from_file('categories', 'tlpui/configschema/{}.json'.format(version))
        jsonconfigcount = get_config_count(jsoncategories)

        self.assertEqual(len(jsoncategories), 11)
        self.assertEqual(80, len(settings.tlpconfig))
        self.assertEqual(jsonconfigcount, len(settings.tlpconfig))

    def test_tlp_version_0_9(self):
        version = "0_9"
        settings.tlpconfig = read_tlp_file_config('test/default_tlp_config_files/tlp-config-{}'.format(version))
        jsoncategories = get_json_schema_object_from_file('categories', 'tlpui/configschema/{}.json'.format(version))
        jsonconfigcount = get_config_count(jsoncategories)

        self.assertEqual(len(jsoncategories), 11)
        self.assertEqual(84, len(settings.tlpconfig))
        self.assertEqual(jsonconfigcount, len(settings.tlpconfig))

    def test_tlp_version_1_0(self):
        version = "1_0"
        settings.tlpconfig = read_tlp_file_config('test/default_tlp_config_files/tlp-config-{}'.format(version))
        jsoncategories = get_json_schema_object_from_file('categories', 'tlpui/configschema/{}.json'.format(version))
        jsonconfigcount = get_config_count(jsoncategories)

        self.assertEqual(len(jsoncategories), 11)
        self.assertEqual(90, len(settings.tlpconfig))
        self.assertEqual(jsonconfigcount, len(settings.tlpconfig))

    def test_tlp_version_1_1(self):
        version = "1_1"
        settings.tlpconfig = read_tlp_file_config('test/default_tlp_config_files/tlp-config-{}'.format(version))
        jsoncategories = get_json_schema_object_from_file('categories', 'tlpui/configschema/{}.json'.format(version))
        jsonconfigcount = get_config_count(jsoncategories)

        self.assertEqual(len(jsoncategories), 11)
        self.assertEqual(91, len(settings.tlpconfig))
        self.assertEqual(jsonconfigcount, len(settings.tlpconfig))

    def test_tlp_version_1_2(self):
        version = "1_2"
        settings.tlpconfig = read_tlp_file_config('test/default_tlp_config_files/tlp-config-{}'.format(version))
        jsoncategories = get_json_schema_object_from_file('categories', 'tlpui/configschema/{}.json'.format(version))
        jsonconfigcount = get_config_count(jsoncategories)

        self.assertEqual(len(jsoncategories), 11)
        self.assertEqual(100, len(settings.tlpconfig))
        self.assertEqual(jsonconfigcount, len(settings.tlpconfig))


if __name__ == '__main__':
    unittest.main()

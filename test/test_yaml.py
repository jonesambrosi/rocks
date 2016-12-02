
import unittest
import yaml


class TestReadingStructures(unittest.TestCase):
    """Reading 
    """
    _yaml_ex = '''
--- !clarkevans.com/^invoice
invoice: 34843
date   : 2001-01-23
bill-to: &id001
    given  : Chris
    family : Dumars
    address:
        lines: |
            458 Walkman Dr.
            Suite #292
        city    : Royal Oak
        state   : MI
        postal  : 48046
ship-to: *id001
product:
    - sku         : BL394D
      quantity    : 4
      description : Basketball
      price       : 450.00
    - sku         : BL4438H
      quantity    : 1
      description : Super Hoop
      price       : 2392.00
tax  : 251.42
total: 4443.52
comments: >
    Late afternoon is best.
    Backup contact is Nancy
    Billsmer @ 338-4338.
    '''

    def test_read_yaml(self):
        docs = yaml.load_all(_yaml_ex)
        for doc in docs:
            for k, v in doc.items():
                print(k, "->", v)
            print("\n",)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

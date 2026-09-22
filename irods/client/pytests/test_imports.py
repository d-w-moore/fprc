from os.path import abspath, dirname, join
import sys

verbose = False

def do_imports():
    import irods.client
    import irods.client.low_level.message.property_types
    import irods.client.low_level.message.ordered
    import irods.client.low_level.message.message
    import irods.client.low_level.message.quasixml
    return irods.client.low_level.message.ET()

def test_et():
  assert do_imports() is not None

if __name__ == '__main__':
    verbose = True
    print(do_imports())

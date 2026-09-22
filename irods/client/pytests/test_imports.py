from os.path import abspath, dirname, join
import sys

verbose = False

def do_imports():
    import irods.client
    import irods.client.message.property_types
    import irods.client.message.ordered
    import irods.client.message.message
    import irods.client.message.quasixml
    return irods.client.message.ET()

def test_et():
  assert do_imports() is not None

if __name__ == '__main__':
    verbose = True
    print(do_imports())

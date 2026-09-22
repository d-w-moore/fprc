from os.path import abspath, dirname, join
import sys

verbose = False

def do_imports():
    saved_library_path = sys.path.copy()
    this_directory = dirname(sys.argv[0])
    try:
        sys.path[:0] = [
            abspath(join(this_directory, '..','..','..'))
        ]
        import irods.client
        import irods.client.message.property_types
        import irods.client.message.ordered
        import irods.client.message.message
        import irods.client.message.quasixml
        if verbose:
            print(sys.path)
#       return irods.client.message.ET()
    finally:
        sys.path[:] = saved_library_path

def test_et():
  assert do_imports() is not None

if __name__ == '__main__':
    verbose = True
    print(do_imports())

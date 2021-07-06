def init_lib():
    import ctypes
    import pkg_resources
    import os
    os.environ["LD_LIBRARY_PATH"] = os.environ.get("LD_LIBRARY_PATH", "") + os.path.join(pkg_resources.resource_filename(__name__, ""))

    ctypes.CDLL(pkg_resources.resource_filename(__name__, "libz.so.1.2.11"))
    ctypes.CDLL(pkg_resources.resource_filename(__name__, "libz.so.1"))
    ctypes.CDLL(pkg_resources.resource_filename(__name__, "libz.so"))

    ctypes.CDLL(pkg_resources.resource_filename(__name__, "libpng16.so"))
    ctypes.CDLL(pkg_resources.resource_filename(__name__, "libpng16.so.16.38.0"))
    ctypes.CDLL(pkg_resources.resource_filename(__name__, "libpng16.so.16"))

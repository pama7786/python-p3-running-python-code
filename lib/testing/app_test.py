import os.path as path
import io
import sys
import runpy
import pytest

class TestAppPy:
    def test_app_py_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello World! Pass this test, please.\n"

    def test_app_py_exists_in_lib_directory(self):
        '''
        exists in lib directory
        '''
        assert path.exists("lib/app.py")

    def test_app_py_is_executable(self):
        '''
        is executable
        '''
        assert path.isfile("lib/app.py")

# Add more tests as described in the README

import sys
import os

# Add src to sys.path globally for all tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

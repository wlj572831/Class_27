import os
import sys
base_name = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_name)

from core import main
main.entry_point()
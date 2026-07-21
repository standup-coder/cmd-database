import traceback
from pathlib import Path
import builtins
orig_print = builtins.print
def my_print(*args, **kwargs):
    s = ' '.join(str(a) for a in args)
    if 'network.yaml' in s:
        raise RuntimeError('network error: '+s)
    orig_print(*args, **kwargs)
builtins.print = my_print
import importlib.util
spec = importlib.util.spec_from_file_location('conv', 'scripts/convert_to_wiki.py')
mod = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mod)
except RuntimeError:
    traceback.print_exc()
finally:
    builtins.print = orig_print

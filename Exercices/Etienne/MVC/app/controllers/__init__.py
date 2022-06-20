import os
import glob

# print(os.path.dirname(__file__))
# print(glob.glob(os.path.dirname(__file__) + "/*.py"))
# print([os.path.basename(f)[: - 3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")])

__all__ = [os.path.basename(f)[: - 3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
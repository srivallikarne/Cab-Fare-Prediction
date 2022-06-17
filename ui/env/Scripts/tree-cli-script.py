#!c:\users\deii\desktop\mycabfareprediction\ui\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Tree==0.2.4','console_scripts','tree-cli'
__requires__ = 'Tree==0.2.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Tree==0.2.4', 'console_scripts', 'tree-cli')()
    )

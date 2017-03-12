"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import os
import sys
from battmon.battmonlibs import run_battmon

if __name__ == '__main__':
    # try:
    pid = os.fork()
    # except OSError as e:
        # print("ERROR: %s [%d]" % (e.strerror, e.errno))

    if pid == 0:
        os.setsid()
        try:
            pid = os.fork()
            if pid == 0:
                os.chdir("/")
                os.umask(0)
                run_battmon.run_main()
            else:
                sys.exit(0)
        except OSError as e:
            print("ERROR: %s [%d]" % (e.strerror, e.errno))
    else:
        os.wait()
        sys.exit(0)

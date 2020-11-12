# Copyright (C) 1998-2018 by the Free Software Foundation, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

"""Parse mystery style generated by MTA at caiwireless.net."""

import re
import email
from io import StringIO

tcre = re.compile(r'the following recipients did not receive this message:',
                  re.IGNORECASE)
acre = re.compile(r'<(?P<addr>[^>]*)>')



def process(msg):
    if msg.get_content_type() != 'multipart/mixed':
        return None
    # simple state machine
    #     0 == nothing seen
    #     1 == tag line seen
    state = 0
    # This format thinks it's a MIME, but it really isn't
    for line in email.iterators.body_line_iterator(msg):
        line = line.strip()
        if state == 0 and tcre.match(line):
            state = 1
        elif state == 1 and line:
            mo = acre.match(line)
            if not mo:
                return None
            return [mo.group('addr')]

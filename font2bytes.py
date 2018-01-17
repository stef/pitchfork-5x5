#!/usr/bin/env python

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys, datetime

if len(sys.argv)!=4:
    print "invoke with: %s <author> <width> <height> < <some-font.bmf>" % sys.argv[0]
    sys.exit(1)

header = """/*
 * font%(width)d%(height)d.h
 *
 * Created: %(date)s
 *  Author: %(author)s
 */

// Title    : Graphic LCD Font (Ascii Charaters)

#ifndef FONT%(width)dX%(height)d_H
#define FONT%(width)dX%(height)d_H

// standard ascii %(width)dx%(height)d font
// defines ascii characters 0x20-0x7F (32-126)

static const char Font[] = {
""" % {
    'date': datetime.datetime.now().isoformat(),
    'author': sys.argv[1],
    'width': int(sys.argv[2]),
    'height': int(sys.argv[3])}

tail = """};

#endif /* FONT%(width)dX%(height)d_H */
""" % {
    'width': int(sys.argv[2]),
    'height': int(sys.argv[3])}

def readchar():
    char = sys.stdin.readline().strip()
    rows = [sys.stdin.readline()[1:-2] for r in xrange(5)]
    return (char, rows)

print header

for _ in xrange(0x20,0x7f):
    char, rows = readchar()
    #print char
    #print '\n'.join(rows)
    rotated=[''.join(x) for x in zip(*rows)]
    cols=[]
    for col in rotated:
        b=0
        for i in xrange(5):
            if col[i]!=' ': b+=(1<<i)
        cols.append(b)
    print ' '.join("0x%02x," % x for x in cols), "// '%s'" % char

print tail


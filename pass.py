#!/usr/bin/env python3

#    Copyright (C) 2016 cacahuatl < cacahuatl at autistici dot org >
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random, math, argparse
class password_generator():
    loaded = False

    def __init__(self, wf='words', wpp=5):
        """Get entropy source and load wordlist"""
        self.entropy = random.SystemRandom()
        self.w = open(wf).read().strip().split('\n')
        self.wpp = wpp
        self.loaded = True

    def estimate_entropy(self):
        """Work out the worst case scenario entropy estimate"""
        if self.loaded:
            return int(math.floor(math.log(len(self.w) ** int(self.wpp), 2)))
        else:
            raise Exception('Generator is not loaded.')

    def generate(self):
        """Generate a passphrase from the wordlist"""
        if self.loaded:
            pw = []
            for _ in range(0,int(self.wpp)):
                pw.append(self.entropy.choice(self.w))
            return ' '.join(pw)
        else:
            raise Exception('Generator is not loaded.')

    def __str__(self):
        return self.generate()

if __name__ == '__main__':
    from os.path import realpath, dirname
    from sys import argv
    default_wordlist = realpath(dirname(argv[0])) + "/eff_words"
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("--count", "-c", default=5, type=int,
            help="Words per passphrase")
    parser.add_argument("--word-list", "-w", default=default_wordlist, type=str,
            help="Word list to generate from")
    args = parser.parse_args()
    p = password_generator(wf=args.word_list, wpp=args.count)
    print('Estimated {} bits of entropy'.format(p.estimate_entropy()))
    print('{}'.format(p.generate()))

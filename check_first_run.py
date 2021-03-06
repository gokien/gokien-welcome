# -*- coding: utf8 -*-
#
# This file is part of the gokien project.
#
# Copyright (C) 2013 Long T. Dam <longdt90@gmail.com>
# Copyright (C) 2013 Trung Ngo <ndtrung4419@gmail.com>
#
# gokien is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gokien is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gokien.  If not, see <http://www.gnu.org/licenses/>.
#

import os

lock_file_path = os.path.expanduser("~/.config/gokien/welcome-lock")


def is_first_run():
    # Check config file existence
    try:
        open(lock_file_path)
        return False
    except:
        return True

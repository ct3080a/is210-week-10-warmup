#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictinary functions"""


import data


CORRECTED = data.BANDS.copy()

del CORRECTED['Van Halen']


dict.fromkeys(['Van Halen'], 'Sammy Hager')

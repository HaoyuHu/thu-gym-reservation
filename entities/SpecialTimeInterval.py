#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TimeInterval import TimeInterval


class SpecialTimeInterval(TimeInterval):
    def __init__(self, interval, start, end):
        TimeInterval.__init__(self, start, end)
        self.interval = interval

    def get_interval(self):
        return self.interval

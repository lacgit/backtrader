#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from datetime import datetime
import backtrader as bt


class AtrCross(bt.SignalStrategy):
    def __init__(self):
        atr1 = bt.ind.ATR(period=5)
        atr2 = bt.ind.ATR(period=10)
        crossover = bt.ind.CrossOver(atr1, atr2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

        atr1
        atr2


cerebro = bt.Cerebro()
cerebro.addstrategy(AtrCross)

data0 = bt.feeds.YahooFinanceData(dataname='GOOG',
                                  fromdate=datetime(2021, 1, 1),
                                  todate=datetime(2023, 12, 31))

cerebro.adddata(data0)

cerebro.run()
cerebro.plot()


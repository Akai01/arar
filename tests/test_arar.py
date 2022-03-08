#!/usr/bin/env python

"""Tests for `arar` package."""

import pytest
from arar.arar import ARAR
import pandas as pd

def test_arar():
    data = pd.DataFrame({'ds': pd.date_range('1984-04-01', periods=40,
                                             freq='M'),
                         'y': [112, 118, 132, 129, 121, 135, 148,
                               148, 136, 119, 104, 118, 115, 126,
                               141, 135, 125, 149, 170, 170, 158,
                               133, 114, 140, 145, 150, 178, 163,
                               172, 178, 199, 199, 184, 162, 146,
                               166, 171, 180, 193, 181]})
    rs = ARAR(data, h=1, freq='M').forecast().get_forecast()["mean"].values
    assert rs != 187.32589871

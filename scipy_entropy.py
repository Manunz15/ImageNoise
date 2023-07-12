# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:06:05 2021

@author: matth
"""

# This a slighty edited version of the original code
# 10/07/2023

from __future__ import annotations
import numpy as np
from scipy import special
from typing import Optional, Union

__all__ = ['entropy']


def entropy(pk: np.typing.ArrayLike,
            qk: Optional[np.typing.ArrayLike] = None,
            base: Optional[float] = None,
            axis: int = 0
            ) -> Union[np.number, np.ndarray]:

    if base is not None and base <= 0:
        raise ValueError("`base` must be a positive number or `None`.")

    pk = np.asarray(pk)
    pk = 1.0*pk / (np.sum(pk, axis=axis, keepdims=True)+1e-32)  # The only edited line
    if qk is None:
        vec = special.entr(pk)
    else:
        qk = np.asarray(qk)
        pk, qk = np.broadcast_arrays(pk, qk)
        qk = 1.0*qk / np.sum(qk, axis=axis, keepdims=True)
        vec = special.rel_entr(pk, qk)
    S = np.sum(vec, axis=axis)
    if base is not None:
        S /= np.log(base)
    return S
# terrain_generator/noise.py
"""
PerlinNoiseGenerator: implementación 2D del ruido Perlin (Ken Perlin),
devuelve valores en el rango [-1.0, 1.0].
"""
from __future__ import annotations
import math
import random
from typing import List, Tuple


class PerlinNoiseGenerator:
    def __init__(self, seed: int | None = None):
        self.seed = seed if seed is not None else random.randrange(2**31)
        self._perm = self._build_permutation(self.seed)

    @staticmethod
    def _build_permutation(seed: int) -> List[int]:
        rng = random.Random(seed)
        p = list(range(256))
        rng.shuffle(p)
        # Duplicate to avoid overflow
        return p + p

    @staticmethod
    def _fade(t: float) -> float:
        # 6t^5 - 15t^4 + 10t^3
        return t * t * t * (t * (t * 6 - 15) + 10)

    @staticmethod
    def _lerp(a: float, b: float, t: float) -> float:
        return a + t * (b - a)

    @staticmethod
    def _grad(hash_: int, x: float, y: float) -> float:
        # Use 8 gradient directions (Ken Perlin)
        h = hash_ & 7  # 0..7
        # pre-defined gradients for 8 directions
        grads: List[Tuple[float, float]] = [
            (1, 1), (-1, 1), (1, -1), (-1, -1),
            (1, 0), (-1, 0), (0, 1), (0, -1),
        ]
        gx, gy = grads[h]
        return gx * x + gy * y

    def noise(self, x: float, y: float) -> float:
        # Find unit grid cell containing point
        xi = math.floor(x) & 255
        yi = math.floor(y) & 255

        # Relative x, y inside cell
        xf = x - math.floor(x)
        yf = y - math.floor(y)

        # Fade curves for x, y
        u = self._fade(xf)
        v = self._fade(yf)

        # Hash coordinates of the 4 cell corners
        p = self._perm
        aa = p[p[xi] + yi]
        ab = p[p[xi] + yi + 1]
        ba = p[p[xi + 1] + yi]
        bb = p[p[xi + 1] + yi + 1]

        # Add blended results from corners
        x1 = self._lerp(self._grad(aa, xf, yf),
                        self._grad(ba, xf - 1, yf), u)
        x2 = self._lerp(self._grad(ab, xf, yf - 1),
                        self._grad(bb, xf - 1, yf - 1), u)
        result = self._lerp(x1, x2, v)

        # Result is typically in range [-sqrt(2), sqrt(2)] but roughly normalized.
        # To guarantee roughly [-1,1], we can clamp / normalize by factor ~1.4142.
        return max(-1.0, min(1.0, result / 1.41421356237))

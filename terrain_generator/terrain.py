# terrain_generator/terrain.py
"""
TerrainMapBuilder: construye una heightmap 2D (numpy.ndarray) usando PerlinNoiseGenerator
con múltiples octavas (fractal noise).
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from .noise import PerlinNoiseGenerator
from typing import Tuple


@dataclass(frozen=True)
class Heightmap:
    width: int
    height: int
    values: np.ndarray  # shape (height, width), dtype=float64


class TerrainMapBuilder:
    def __init__(
        self,
        seed: int | None = None,
        scale: float = 50.0,
        octaves: int = 4,
        persistence: float = 0.5,
        lacunarity: float = 2.0,
    ):
        if scale <= 0:
            raise ValueError("scale must be > 0")
        self.noise = PerlinNoiseGenerator(seed=seed)
        self.scale = float(scale)
        self.octaves = max(1, int(octaves))
        self.persistence = float(persistence)
        self.lacunarity = float(lacunarity)

    def build(self, width: int, height: int, offset: Tuple[float, float] = (0.0, 0.0)) -> Heightmap:
        """
        Genera la matriz de alturas sin normalizar (valores en algún rango).
        width, height: dimensiones en píxeles/celdas.
        offset: (ox, oy) desplazamiento aplicado a coordenadas de ruido.
        """
        values = np.zeros((height, width), dtype=np.float64)

        ox, oy = float(offset[0]), float(offset[1])

        for j in range(height):
            for i in range(width):
                x = (i + ox) / self.scale
                y = (j + oy) / self.scale

                amplitude = 1.0
                frequency = 1.0
                noise_height = 0.0

                for o in range(self.octaves):
                    sample_x = x * frequency
                    sample_y = y * frequency
                    n = self.noise.noise(sample_x, sample_y)
                    noise_height += n * amplitude

                    amplitude *= self.persistence
                    frequency *= self.lacunarity

                values[j, i] = noise_height

        return Heightmap(width=width, height=height, values=values)

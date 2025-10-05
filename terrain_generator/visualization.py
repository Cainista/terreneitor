# terrain_generator/visualization.py
"""
MapVisualizer: normaliza la heightmap y la convierte a imagen (Pillow).
Aplica un Strategy simple para coloreado por rangos.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from PIL import Image
from typing import Tuple
from .terrain import Heightmap


@dataclass
class MapVisualizer:
    heightmap: Heightmap

    def normalize(self) -> np.ndarray:
        arr = self.heightmap.values
        min_v = float(np.nanmin(arr))
        max_v = float(np.nanmax(arr))
        if max_v - min_v == 0:
            return np.zeros_like(arr, dtype=np.float32)
        normalized = (arr - min_v) / (max_v - min_v)
        return normalized.astype(np.float32)

    def height_to_color(self, h: float) -> Tuple[int, int, int]:
        """
        Strategy para mapear alturas normalizadas [0,1] a RGB.
        Reglas:
          - h < 0.20 -> water (deep blue -> light blue)
          - 0.20 <= h < 0.50 -> land (green)
          - 0.50 <= h < 0.80 -> mountain/base (brownish -> gray)
          - h >= 0.80 -> snow (white)
        """
        if h < 0.2:
            # interpolate from deep blue to light blue
            t = h / 0.2
            deep = np.array([0, 32, 128], dtype=int)
            light = np.array([64, 160, 255], dtype=int)
            c = (deep * (1 - t) + light * t).astype(int)
            return int(c[0]), int(c[1]), int(c[2])
        if h < 0.5:
            t = (h - 0.2) / 0.3
            dark = np.array([20, 120, 40], dtype=int)
            bright = np.array([120, 200, 80], dtype=int)
            c = (dark * (1 - t) + bright * t).astype(int)
            return int(c[0]), int(c[1]), int(c[2])
        if h < 0.8:
            t = (h - 0.5) / 0.3
            brown = np.array([120, 90, 50], dtype=int)
            gray = np.array([180, 180, 180], dtype=int)
            c = (brown * (1 - t) + gray * t).astype(int)
            return int(c[0]), int(c[1]), int(c[2])
        # snow
        t = min(1.0, (h - 0.8) / 0.2)
        base = np.array([230, 230, 230], dtype=int)
        pure = np.array([255, 255, 255], dtype=int)
        c = (base * (1 - t) + pure * t).astype(int)
        return int(c[0]), int(c[1]), int(c[2])

    def to_image(self) -> Image.Image:
        norm = self.normalize()
        h, w = norm.shape
        rgb = np.zeros((h, w, 3), dtype=np.uint8)
        # Vectorize mapping reasonably efficiently
        for j in range(h):
            for i in range(w):
                rgb[j, i] = self.height_to_color(float(norm[j, i]))
        return Image.fromarray(rgb, mode="RGB")

    def save(self, path: str = "terrain.png", show: bool = False) -> None:
        img = self.to_image()
        img.save(path)
        if show:
            img.show()

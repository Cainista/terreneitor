# main.py
"""
Script principal para generar y guardar un mapa de alturas usando Perlin noise fractal.
Ejemplo de uso:
    python main.py --width 256 --height 256 --scale 60 --octaves 5 --persistence 0.5 --lacunarity 2.0 --seed 42 --out terrain.png --show
"""
from __future__ import annotations
import argparse
from terrain_generator.terrain import TerrainMapBuilder
from terrain_generator.visualization import MapVisualizer


def parse_args():
    parser = argparse.ArgumentParser(description="Generador de terreno 2D usando Perlin (fractal).")
    parser.add_argument("--width", type=int, default=256, help="Ancho en píxeles (default 256)")
    parser.add_argument("--height", type=int, default=256, help="Alto en píxeles (default 256)")
    parser.add_argument("--scale", type=float, default=60.0, help="Escala (affects zoom) (default 60.0)")
    parser.add_argument("--octaves", type=int, default=4, help="Número de octavas (default 4)")
    parser.add_argument("--persistence", type=float, default=0.5, help="Persistence (default 0.5)")
    parser.add_argument("--lacunarity", type=float, default=2.0, help="Lacunarity (default 2.0)")
    parser.add_argument("--seed", type=int, default=None, help="Semilla aleatoria (int) (default None)")
    parser.add_argument("--out", type=str, default="terrain.png", help="Ruta de salida PNG (default terrain.png)")
    parser.add_argument("--show", action="store_true", help="Abrir la imagen después de generar")
    return parser.parse_args()


def main():
    args = parse_args()

    builder = TerrainMapBuilder(
        seed=args.seed,
        scale=args.scale,
        octaves=args.octaves,
        persistence=args.persistence,
        lacunarity=args.lacunarity,
    )

    heightmap = builder.build(width=args.width, height=args.height)

    visual = MapVisualizer(heightmap=heightmap)
    visual.save(path=args.out, show=args.show)
    print(f"Imagen guardada en: {args.out}")


if __name__ == "__main__":
    main()

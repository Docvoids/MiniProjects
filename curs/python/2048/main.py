import pygame
import random
import math

pygame.init()

# Constants
FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        return self.COLORS[color_index]

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (
                self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
                self.y + (RECT_HEIGHT / 2 - text.get_height() / 2),
            ),
        )

    def set_pos(self, ceil=False):
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]


class Game:
    def __init__(self):
        self.tiles = self.generate_initial_tiles()
        self.clock = pygame.time.Clock()

    def generate_initial_tiles(self):
        tiles = {}
        for _ in range(2):
            row, col = self.get_random_pos(tiles)
            tiles[f"{row}{col}"] = Tile(2, row, col)
        return tiles

    def get_random_pos(self, tiles):
        while True:
            row = random.randrange(0, ROWS)
            col = random.randrange(0, COLS)
            if f"{row}{col}" not in tiles:
                return row, col

    def draw_grid(self, window):
        for row in range(1, ROWS):
            y = row * RECT_HEIGHT
            pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
        for col in range(1, COLS):
            x = col * RECT_WIDTH
            pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)
        pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

    def draw(self, window):
        window.fill(BACKGROUND_COLOR)
        for tile in self.tiles.values():
            tile.draw(window)
        self.draw_grid(window)
        pygame.display.update()

    def move_tiles(self, direction):
        updated = True
        blocks = set()

        move_params = {
            "left": (lambda x: x.col, False, (-MOVE_VEL, 0), lambda tile: tile.col == 0, lambda tile: self.tiles.get(f"{tile.row}{tile.col - 1}"), lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL, lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL, True),
            "right": (lambda x: x.col, True, (MOVE_VEL, 0), lambda tile: tile.col == COLS - 1, lambda tile: self.tiles.get(f"{tile.row}{tile.col + 1}"), lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL, lambda tile, next_tile: tile.x + RECT_WIDTH + MOVE_VEL < next_tile.x, False),
            "up": (lambda x: x.row, False, (0, -MOVE_VEL), lambda tile: tile.row == 0, lambda tile: self.tiles.get(f"{tile.row - 1}{tile.col}"), lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL, lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL, True),
            "down": (lambda x: x.row, True, (0, MOVE_VEL), lambda tile: tile.row == ROWS - 1, lambda tile: self.tiles.get(f"{tile.row + 1}{tile.col}"), lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL, lambda tile, next_tile: tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y, False)
        }

        sort_func, reverse, delta, boundary_check, get_next_tile, merge_check, move_check, ceil = move_params[direction]

        while updated:
            self.clock.tick(FPS)
            updated = False
            sorted_tiles = sorted(self.tiles.values(), key=sort_func, reverse=reverse)

            for i, tile in enumerate(sorted_tiles):
                if boundary_check(tile):
                    continue

                next_tile = get_next_tile(tile)
                if not next_tile:
                    tile.move(delta)
                elif tile.value == next_tile.value and tile not in blocks and next_tile not in blocks:
                    if merge_check(tile, next_tile):
                        tile.move(delta)
                    else:
                        next_tile.value *= 2
                        sorted_tiles.pop(i)
                        blocks.add(next_tile)
                elif move_check(tile, next_tile):
                    tile.move(delta)
                else:
                    continue

                tile.set_pos(ceil)
                updated = True

            self.update_tiles(sorted_tiles)

        return self.end_move()

    def update_tiles(self, sorted_tiles):
        self.tiles.clear()
        for tile in sorted_tiles:
            self.tiles[f"{tile.row}{tile.col}"] = tile
        self.draw(WINDOW)

    def end_move(self):
        if len(self.tiles) == 16:
            return "lost"
        row, col = self.get_random_pos(self.tiles)
        self.tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col)
        return "continue"

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_tiles("left")
            if event.key == pygame.K_RIGHT:
                self.move_tiles("right")
            if event.key == pygame.K_UP:
                self.move_tiles("up")
            if event.key == pygame.K_DOWN:
                self.move_tiles("down")


def main():
    game = Game()
    run = True

    while run:
        game.clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            game.handle_input(event)

        game.draw(WINDOW)

    pygame.quit()


if __name__ == "__main__":
    main()

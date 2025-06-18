import random
from collections import deque

def search_mines(cs, coords_mines):
    y, x = cs[0], cs[1]
    side_coords = [
        (y + 1, x - 1), (y + 1, x), (y + 1, x + 1),
        (y, x - 1),                (y, x + 1),
        (y - 1, x - 1), (y - 1, x), (y - 1, x + 1)
    ]
    num_mines = 0
    for cx, cy in coords_mines:
        if (cx, cy) in side_coords:
            num_mines += 1
    return num_mines

def expand_zeros(start, coords_mines, revealed, height, length):
    queue = deque()
    queue.append(tuple(start))
    visited = set()

    while queue:
        y, x = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))

        if [y, x] not in revealed:
            revealed.append([y, x])

        if search_mines([y, x], coords_mines) == 0:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny, nx = y + dy, x + dx
                    if 1 <= ny <= height and 1 <= nx <= length:
                        if [ny, nx] not in revealed:
                            revealed.append([ny, nx])
                        if (ny, nx) not in visited and search_mines([ny, nx], coords_mines) == 0:
                            queue.append((ny, nx))

def create_terrain(height, length, coords, mode, coords_inputs, flags_coords):
    RESET = "\033[0m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    YELLOW_BG = "\033[43m"

    COLORS = {
        1: "\033[38;5;152m",  # Verde suave
        2: "\033[38;5;114m",
        3: "\033[38;5;150m",
        4: "\033[38;5;186m",
        5: "\033[38;5;220m",
        6: "\033[38;5;208m",
        7: "\033[38;5;202m",
        8: "\033[38;5;196m",  # Rojo fuerte
    }

    # Encabezado de columnas
    terrain = "   "
    for x in range(1, length + 1):
        terrain += f"{x%10}"
    terrain += "\n"

    for i in range(1, height + 1):
        terrain += f"{i:2d}|"

        for x in range(1, length + 1):
            current_input = [i, x]
            already_played = current_input in coords_inputs
            is_flagged = current_input in flags_coords
            is_mine = current_input in coords

            if already_played:
                if is_mine and mode == "step" and coords_inputs[-1] == current_input:
                    terrain += f"{RED}M{RESET}"
                    print("YOU LOSE")
                    exit()
                else:
                    n = search_mines(current_input, coords)
                    color = COLORS.get(n, RESET)
                    terrain += f"{color}{n}{RESET}"
            elif is_flagged:
                terrain += f"{RED}P{RESET}"
            else:
                terrain += f"{BLUE}X{RESET}"

        terrain += f"{YELLOW_BG}|{RESET}\n"

    return terrain

def generate_mines(height, length):
    num_mines = round((height * length) / 8)
    coords = set()
    while len(coords) < num_mines:
        x = random.randint(1, height)
        y = random.randint(1, length)
        coords.add((x, y))
    return [[x, y] for x, y in coords]

def check_win_condition(height, length, mine_coords, revealed_coords):
    total_cells = height * length
    total_mines = len(mine_coords)
    total_revealed = len(revealed_coords)

    if total_cells - total_mines == total_revealed:
        print("\n¡FELICIDADES! Has descubierto todas las casillas sin minas. ¡Has ganado!")
        exit()

if __name__ == "__main__":
    height = 10
    length = 30
    coords = generate_mines(height, length)
    mode = "step"
    coords_inputs = []
    flags_coords = []

    input_player = ""
    while input_player != "end":
        print(f"\nSeleccione unas coordenadas (1-{height}, 1-{length}) o cambia de modo ('step' o 'flag'):")
        input_player = input("> ")

        if input_player == "step":
            print("Modo: Paso")
            mode = "step"
        elif input_player == "flag":
            print("Modo: Bandera")
            mode = "flag"
        elif input_player == "end":
            print("Fin del juego")
            break
        else:
            try:
                coords_string = input_player.split(",")
                row = int(coords_string[0].strip())
                col = int(coords_string[1].strip())
                new_input = [row, col]

                if mode == "flag":
                    if new_input in flags_coords:
                        flags_coords.remove(new_input)
                    else:
                        flags_coords.append(new_input)
                elif mode == "step":
                    if new_input in flags_coords:
                        print("No puedes pisar una casilla con bandera. Quita la bandera primero.")
                    elif new_input in coords:
                        coords_inputs.append(new_input)
                        print(create_terrain(height, length, coords, mode, coords_inputs, flags_coords))
                        continue
                    elif search_mines(new_input, coords) == 0:
                        expand_zeros(new_input, coords, coords_inputs, height, length)
                    else:
                        coords_inputs.append(new_input)

                print(create_terrain(height, length, coords, mode, coords_inputs, flags_coords))
                check_win_condition(height, length, coords, coords_inputs)

            except Exception as e:
                print("Entrada inválida. Usa formato: 'fila, columna' (ej: 2, 5)")

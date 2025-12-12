
import re
import copy

def normalize_shape(coords):
    # Normalize a set of shape coordinates so that it's top-most and left-most
    min_x = min(x for x,y in coords)
    min_y = min(y for x,y in coords)
    return frozenset({(x-min_x , y-min_y) for x,y in coords}) 

def rotate(coords):
    max_x = max(x for x,y in coords)
    return frozenset({(y,max_x-x) for x,y in coords})

def flip(coords):
    max_y = max(y for x,y in coords)
    return frozenset({(x,max_y-y) for x,y in coords})

def generate_orientations(coords):
    orientations = set()
    current_orientation = coords
    
    for _ in range(2): # original and flipped
        for _ in range(4):
            current_orientation = normalize_shape(current_orientation)
            orientations.add(current_orientation)
            current_orientation = rotate(current_orientation)
        current_orientation = flip(coords)
    return list(orientations)

def solve_packing(width, height, shapes_orientations, required_present):
    present_count = {i: count for i, count in enumerate(required_present) if count > 0}
    
    grid = [[False for _ in range(width)] for _ in range(height)]
    
    def find_next_empty_cell(current_grid):
        for x in range(height):
            for y in range(width):
                if not current_grid[x][y]:
                    return x,y
        return None
    
    def try_place_presents(current_grid, current_present_counts):
        if all(count == 0 for count in current_present_counts.values()):
            return True
        
        start_x, start_y = find_next_empty_cell(current_grid)
        if (start_x, start_y) is None:
            return False
        
        for shape_idx, count in current_present_counts.items():
            if count == 0:
                continue
            for orientation_coords in shapes_orientations[shape_idx]:
                for o_x, o_y in orientation_coords:
                    x_offset = start_x - o_x
                    y_offset = start_y - o_y
                    
                    can_place = True
                    
                    cells_to_occupy = []
                    for shape_x, shape_y in orientation_coords:
                        target_x = x_offset + shape_x
                        target_y = y_offset + shape_y
                        
                        if not (0 <= target_x < height and 0 <= target_y < width and not current_grid[target_x][target_y]):
                            can_place = False
                            break
                        cells_to_occupy.append((target_x,target_y))
                    if can_place:
                        new_grid = [row[:] for row in current_grid]
                        for x,y in cells_to_occupy:
                            new_grid[x][y] = True
                        
                        new_present_counts = current_present_counts.copy()
                        new_present_counts[shape_idx] -= 1
                        
                        if try_place_presents(new_grid,new_present_counts):
                            return True
        return False
    return try_place_presents(grid, present_count)
          
f = open("day_12_input.txt","r")

shapes_data_original = {}
shapes_data = {}
shape_index = -1
read_shape = True
shapes_orientations = []

region_count = 0
for line in f:
    line = line.strip()
        
    if read_shape:
        if line != "":
            if ":" in line:
                shape_index = int(line[0])
                shapes_data_original[shape_index] = []
            else:
                shapes_data_original[shape_index].append(line)
                
        elif line == "" and shape_index == 5:
            read_shape = False
            
            # Transfer shapes data to the coordinates
            for i, shape_lines in shapes_data_original.items():
                coords = set()
                for x, row in enumerate(shape_lines):
                    for y, char in enumerate(row):
                        if char == "#":
                            coords.add((x,y))
                shapes_data[i] = frozenset(coords)
                
                # Calculate orientations
                orientations = generate_orientations(coords)
                shapes_orientations.append(orientations)
                
    else:
        # region data
        area, counts = line.split(": ")
        width, height = map(int, area.split("x"))
        counts = list(map(int,counts.split(" ")))
        
        if solve_packing(width, height, shapes_orientations, counts):
            print("yes")
            region_count += 1
        else:
            print("no")
                        
          
f.close()



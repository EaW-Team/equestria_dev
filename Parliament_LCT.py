import math
import matplotlib.pyplot as plt

def generate_parliament_positions(total_members, rows=6, sectors=4, corridor_angle_deg=6.0, inner_radius=60, row_spacing=35):
    corridor = math.radians(corridor_angle_deg)

    available_angle = math.pi - sectors * corridor
    if available_angle <= 0:
        raise ValueError("Corridor angles too large for semicircle")
    
    sector_angle = available_angle / sectors

    radius = [inner_radius + r*row_spacing for r in range(rows)]

    # using arc length to estimate the proportionality of the amount of points of each line segment
    capacities = []
    for i in range(len(radius)):
        for s in range(sectors):
            cap = radius[i] * sector_angle
            capacities.append(cap)
    total_cap = sum(c for c in capacities)
    raw = [(c/total_cap)*total_members for c in capacities]
    counts = [int(x) for x in raw]

    # rounding correction
    # this is stupid
    diff = total_members - sum(counts)
    if diff != 0:
        fr = [raw[i] - math.floor(raw[i]) for i in range(len(raw))]
        order = sorted(range(len(fr)), key=lambda i: fr[i], reverse=True)
        for i in range(abs(diff)):
            idx = order[i % len(order)]
            counts[idx] += 1 if diff > 0 else -1

    sector_starts = []
    running = math.radians(corridor_angle_deg/2)
    for s in range(sectors):
        sector_starts.append(running)
        running += sector_angle + corridor

    seats = []
    idx = 0
    c_index = 0

    # Outer loop is looping through every row
    # Inner loop is looping through every sector
    for i in range(len(radius)):
        for s in range(sectors):
            seat_count = counts[c_index]
            c_index += 1

            if seat_count <= 0:
                continue

            start = sector_starts[s]
            inner = start + (sector_angle * 0.1)
            outer = start + sector_angle - (sector_angle * 0.1)

            if seat_count == 1:
                angles = [(inner + outer)/2]
            else:
                step = (outer - inner) / seat_count
                angles = [inner + (i+0.5)*step for i in range(seat_count)]

            for j in range(len(angles)):
                x = radius[i] * math.cos(angles[j])
                y = radius[i] * math.sin(angles[j])
                rotation_angle = round(180-math.degrees(math.atan2(y,x)))

                seats.append({"x": x, "y": y, "rotation_angle": rotation_angle, "idx": idx })
                idx += 1

    # re-order to help with gridbox implementation from left to right using atan2
    seats.sort(key=lambda s: math.atan2(s["y"], s["x"]), reverse=True)
    for i, s in enumerate(seats):
        s["global_index"] = i

    return seats

seats = generate_parliament_positions(90)

# Extract coordinate lists for plotting
xs = [s["x"] for s in seats]
ys = [s["y"] for s in seats]
rots = [s["rotation_angle"] for s in seats]

# Plot seat dots
plt.figure(figsize=(6,6))
plt.scatter(xs, ys, s=15)
for i in range(len(xs)):
    plt.text(xs[i], ys[i], f"{i} , Rot: {rots[i]}", fontsize=10)
plt.gca().set_aspect("equal")
print(xs[0],ys[0])
print(xs[-1],ys[-1])
plt.show()

for i in range(len(xs)):
    print(f'Point {i+1}:')
    print(f'x = {xs[i]}')
    print(f'y = {ys[i]}')
    print(f'')

scripted_effect_entry = '''
    add_to_array = {{ LCT_DIET_seats_x = {x_coord} }}
    add_to_array = {{ LCT_DIET_seats_y = {y_coord} }}
    add_to_array = {{ LCT_DIET_seats_rot = {rot_deg} }}
'''

out = ""
for i in range(len(xs)):
    out += scripted_effect_entry.format(x_coord = round(xs[i] + max(xs)), y_coord = round(abs(ys[i] - max(ys))), rot_deg = 360 - rots[i])
with open('Parliament_LCT.txt', 'w') as f:
    f.write(out)
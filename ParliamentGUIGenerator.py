import os
import tkinter as tk
import tkinter.filedialog as filedialog
import string
import math
try:
	from PIL import ImageTk, Image, ImageOps
	has_pil = True
except ImportError:
	has_pil = False

# by Flaxbeard
# based on https://github.com/slashme/parliamentdiagram, the open-source
# online parliament generator, found at https://parliamentdiagram.toolforge.org/parlitest.php

curr_dir, _ = os.path.split(os.getcwd())

ROW_TOTALS = [4, 15, 33, 61, 95, 138, 189, 247, 313, 388, 469, 559, 657, 762, 876, 997, 1126, 1263, 1408, 1560, 1722, 1889, 2066, 2250, 2442, 2641, 2850, 3064, 3289, 3519, 3759, 4005, 4261, 4522, 4794, 5071, 5358, 5652, 5953, 6263, 6581, 6906, 7239, 7581, 7929, 8287, 8650, 9024, 9404,
		9793, 10187, 10594, 11003, 11425, 11850, 12288, 12729, 13183, 13638, 14109, 14580, 15066, 15553, 16055, 16557, 17075, 17592, 18126, 18660, 19208, 19758, 20323, 20888, 21468, 22050, 22645, 23243, 23853, 24467, 25094, 25723, 26364, 27011, 27667, 28329, 29001, 29679, 30367, 31061]

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450


GUI_FILE = '''
### Insert as a top-level container in your .gui file

containerWindowType = {{
	name = "{container_name}"
	position = {{ x = 0 y = 0 }}

	iconType = {{ 
		name = "{parliament_dot_icon}"
		quadTextureSprite = "{sprite_name}"
		{tooltip_info}
	}}
}}


'''

GUI_FILE_2 = '''
### Insert where you want the diagram to go, feel free to adjust position etc


# LEAVE THESE COMMENTS IN SO YOU CAN REGENERATE THIS DIAGRAM
# IF THE SCRIPT IS IMPROVED DOWN THE LINE
# YOU HAVE BEEN WARNED
# Spread: {spread}
# First Row Radius: {first_row_rad}
# Total Delegates: {total_delegates}
gridboxtype = {{
	name = "{parliament_diagram}"
	position = {{ x = 0 y = 0 }}
	size = {{ width = 100%% height = 100%% }}
	slotsize = {{ width = 100%% height = 0 }}
	max_slots_horizontal = 1
	add_horizontal = no
}}


'''

SCRIPTED_GUI = '''
### Insert into the scripted GUI for the container which holds the parliament_diagram gridboxtype

dynamic_lists = {{
	{parliament_diagram} = {{
		array = {x_array}
		change_scope = no
		entry_container = {container_name}
		index = seat_idx
	}}
}}

properties = {{
	{parliament_dot_icon} = {{
		x = {x_array}^seat_idx
		y = {y_array}^seat_idx
		frame = {frame_array}^seat_idx
	}}
}}


'''

SCRIPTED_EFFECTS = '''
### Insert into a history file or scripted effect, this sets up all of the seat positions
### Note that you'll need to fill out {frame_array} yourself with the proper frames for each seat
{spam}


'''

def invert_image(im):
	if im.mode == 'RGBA':
		r,g,b,a = im.split()
		rgb_image = Image.merge('RGB', (r,g,b))
		inverted_image = ImageOps.invert(rgb_image)
		r2,g2,b2 = inverted_image.split()

		return Image.merge('RGBA', (r2,g2,b2,a))
	else:
		return ImageOps.invert(im)

class UI(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()

		if has_pil:
			self.create_widgets()
		else:
			self.create_pil_msg()
		self.load_image("./small_circle.png")

	def create_pil_msg(self):
		self.pil_msg = tk.Label(self)
		self.pil_msg["text"] = "You must install the Pillow library to run this tool. Run `pip install pillow`"
		self.pil_msg.pack(side="top")

	def create_widgets(self):
		
		self.total_delegates_slider_label = tk.Label(self)
		self.total_delegates_slider_label["text"] = "Total Delegates:"
		self.total_delegates_slider_label.pack(side="top")

		self.total_delegates_slider = tk.Scale(self, from_=10, to=600, orient=tk.HORIZONTAL, command=self.update_positions, length=600)
		self.total_delegates_slider.set(450)
		self.total_delegates_slider.pack()

		self.other_color_slider_label = tk.Label(self)
		self.other_color_slider_label["text"] = "Preview Progress:"
		self.other_color_slider_label.pack(side="top")

		self.other_color_slider = tk.Scale(self, from_=0, to=600, orient=tk.HORIZONTAL, command=self.update_positions, length=600)
		self.other_color_slider.set(0)
		self.other_color_slider.pack()

		self.oaf_slider_label = tk.Label(self)
		self.oaf_slider_label["text"] = "Ordering Adjustment Factor:"
		#self.oaf_slider_label.pack(side="top")
		self.oaf_slider = tk.Scale(self, from_=-1, to=1, orient=tk.HORIZONTAL, resolution = 0.01,  command=self.update_positions, length=600)
		self.oaf_slider.set(0)
		#self.oaf_slider.pack()

		self.spread_slider_label = tk.Label(self)
		self.spread_slider_label["text"] = "Spread:"
		self.spread_slider_label.pack(side="top")
		self.spread_slider = tk.Scale(self, from_=0, to=10, orient=tk.HORIZONTAL, resolution = 0.01,  command=self.update_positions, length=600)
		self.spread_slider.set(1.85)
		self.spread_slider.pack()

		self.hole_slider_label = tk.Label(self)
		self.hole_slider_label["text"] = "First Row Radius:"
		self.hole_slider_label.pack(side="top")
		self.hole_slider = tk.Scale(self, from_=0, to=20, orient=tk.HORIZONTAL, resolution = 0.01,  command=self.update_positions, length=600)
		self.hole_slider.set(5.7)
		self.hole_slider.pack()

		self.select_image_button = tk.Button(self)
		self.select_image_button["text"] = "Select Preview Image\n(Crops to square, frames ok)"
		self.select_image_button["command"] = self.select_image_path
		self.select_image_button.pack(side="top")

		self.preview_label = tk.Label(self)
		self.preview_label["text"] = "Preview:"
		self.preview_label.pack(side="top")
		self.canvas = tk.Canvas(self, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "#061015")
		self.canvas.pack()

		


		frame1 = tk.Frame(self)
		frame1l = tk.Frame(self)
		frame2 = tk.Frame(self)
		frame2l = tk.Frame(self)

		self.x_pos_array_name_label = tk.Label(frame1l)
		self.x_pos_array_name_label["text"] = "X Position Array Name:"
		self.x_pos_array_name_label.pack(padx=13, pady=5, side=tk.LEFT)
		self.x_pos_array_name = tk.Entry(frame1)
		self.x_pos_array_name.pack(side="top")
		self.x_pos_array_name.pack(padx=15, pady=10, side=tk.LEFT)

		self.y_pos_array_name_label = tk.Label(frame1l)
		self.y_pos_array_name_label["text"] = "Y Position Array Name:"
		self.y_pos_array_name_label.pack(padx=13, pady=5, side=tk.LEFT)
		self.y_pos_array_name = tk.Entry(frame1)
		self.y_pos_array_name.pack(padx=15, pady=10, side=tk.LEFT)

		self.frame_array_name_label = tk.Label(frame1l)
		self.frame_array_name_label["text"] = "Frame Array Name:"
		self.frame_array_name_label.pack(padx=17, pady=5, side=tk.LEFT)
		self.frame_array_name = tk.Entry(frame1)
		self.frame_array_name.pack(side="top")
		self.frame_array_name.pack(padx=15, pady=10, side=tk.LEFT)

		self.tooltip_label = tk.Label(frame2l)
		self.tooltip_label["text"] = "Tooltip loc, empty if none:"
		self.tooltip_label.pack(padx=5, pady=5, side=tk.LEFT)

		self.dc_name_label = tk.Label(frame2l)
		self.dc_name_label["text"] = "New container name for seat:"
		self.dc_name_label.pack(padx=2, pady=5, side=tk.LEFT)
		
		self.gfxid_label = tk.Label(frame2l)
		self.gfxid_label["text"] = "Seat icon sprite name:"
		self.gfxid_label.pack(padx=5, pady=5, side=tk.LEFT)
		
		self.dig_name_label = tk.Label(frame2l)
		self.dig_name_label["text"] = "Diagram container names:"
		self.dig_name_label.pack(padx=15, pady=5, side=tk.LEFT)
		
		self.seat_name_label = tk.Label(frame2l)
		self.seat_name_label["text"] = "Seat icon gui name:"
		self.seat_name_label.pack(padx=15, pady=5, side=tk.LEFT)

		self.tooltip = tk.Entry(frame2)
		self.tooltip.pack(padx=15, pady=5, side=tk.LEFT)

		self.dc_name = tk.Entry(frame2)
		self.dc_name.pack(padx=15, pady=5, side=tk.LEFT)

		self.gfxid = tk.Entry(frame2)
		self.gfxid.pack(padx=15, pady=5, side=tk.LEFT)

		self.dig_name = tk.Entry(frame2)
		self.dig_name.pack(padx=15, pady=5, side=tk.LEFT)

		self.seat_name = tk.Entry(frame2)
		self.seat_name.pack(padx=15, pady=5, side=tk.LEFT)
		
		frame1l.pack(side="top")
		frame1.pack(side="top")

		frame2l.pack(side="top")
		frame2.pack(side="top")


		self.run_script = tk.Button(self)
		self.run_script["text"] = "Generate Output"
		self.run_script["command"] = self.output_file
		self.run_script.pack(side="top")

	def select_image_path(self):
		self.select_image_file = filedialog.askopenfilename(initialdir=curr_dir + "\gfx")
		self.load_image(self.select_image_file)

	def load_image(self, pth):
		im = Image.open(pth)
		w, h = im.size
		im = im.crop((0, 0, h, h))
		self.width = w
		self.img = ImageTk.PhotoImage(im)
		self.img2 = ImageTk.PhotoImage(invert_image(im))
		self.update_positions()

	def output_file(self):
		x_pos_array_name = self.x_pos_array_name.get()
		y_pos_array_name = self.y_pos_array_name.get()
		frame_array_name = self.frame_array_name.get()
		dc_name = self.dc_name.get()
		tooltip = self.tooltip.get()
		gfxid = self.gfxid.get()
		diagram_name = self.dig_name.get()
		seat_name = self.seat_name.get()

		total_delegates = self.total_delegates_slider.get()
		spread_dist = self.spread_slider.get()
		hole_size = self.hole_slider.get()

		if tooltip != '':
			tooltip = 'pdx_tooltip = "' + tooltip + '"'

		if diagram_name == '':
			diagram_name = 'parliament_diagram'

		if seat_name == '':
			seat_name = 'parliament_dot_icon'

		out = GUI_FILE.format(container_name = dc_name, sprite_name = gfxid, tooltip_info=tooltip, parliament_dot_icon=seat_name)
		out += GUI_FILE_2.format(spread = spread_dist, first_row_rad = hole_size, total_delegates = total_delegates, parliament_diagram=diagram_name)
		out += SCRIPTED_GUI.format(x_array = x_pos_array_name, y_array = y_pos_array_name, container_name = dc_name, frame_array = frame_array_name, parliament_diagram=diagram_name, parliament_dot_icon=seat_name)

		a2a_spam = ''

		xpositions = [self.poslist[i][1]*100.0 for i in range(len(self.poslist))]
		ypositions = [self.poslist[i][2]*100.0 for i in range(len(self.poslist))]
		out_width = max(xpositions) - min(xpositions) + self.circle_image_rad
		out_height = max(ypositions) - min(ypositions) + self.circle_image_rad + 10

		for i in range(len(self.poslist)):
			entry = self.poslist[i]
			a2a_spam += "add_to_array = {{ {x_pos_array_name} = {x} }}\nadd_to_array = {{ {y_pos_array_name} = {y} }}\n".format(
				x = round(entry[1]*100.0+(out_width/2) - self.circle_image_rad/2),
				y = round(out_height - 100.0*(entry[2]) - self.circle_image_rad/2),
				x_pos_array_name = x_pos_array_name,
				y_pos_array_name = y_pos_array_name,
			)
		out += SCRIPTED_EFFECTS.format(frame_array = frame_array_name, spam=a2a_spam)

		with open('./parliament_gui_code.txt', 'w') as f:
			f.write(out)

	def update_positions(self, _ = 0):
		total_delegates = self.total_delegates_slider.get()
		other_color = self.other_color_slider.get()

		self.canvas.delete("all")
		if total_delegates < 10:
			return

		# Grab parameters from sliders
		spread_dist = self.spread_slider.get()
		hole_size = self.hole_slider.get()
		oaf = self.oaf_slider.get()

		# Figure out how many rows are needed:
		for i in range(len(ROW_TOTALS)):
			if ROW_TOTALS[i] >= total_delegates:
				rows = i+1
				break
		
		radius = 0.1

		self.poslist = []
		for i in range(1, rows):
			# Each row can contain pi/(2asin(2/(3n+4i-2))) spots, where n is the number of rows and i is the number of the current row.
			# Fill each row proportionally to the "fullness" of the diagram, up to the second-last row.
			J = int(float(total_delegates) / ROW_TOTALS[rows-1] *
					math.pi/(2*math.asin(2.0/(3.0*rows+4.0*i-2.0))))
			# The radius of the ith row in an N-row diagram (Ri) is (3 * hole_size + spread_dist * i - 2) / (4 * N)
			R = (3.0 * hole_size + spread_dist * i - 2.0) / (4.0 * 4)
			if J == 1:
				self.poslist.append([math.pi / 2.0, 1.75 * R, R, R])
			else:
				for j in range(J):
					# The angle to a spot is n.(pi-2sin(r/Ri))/(Ni-1)+sin(r/Ri) where Ni is the number in the arc
					# x=R.cos(theta) + 1.75
					# y=R.sin(theta)
					angle = float(j) * \
							(math.pi-2.0*math.sin(radius/R)) / \
							(float(J)-1.0)+math.sin(radius/R)
					self.poslist.append([angle, R*math.cos(angle), R*math.sin(angle), R])

		# Now whatever seats are left go into the outside row:
		J = total_delegates-len(self.poslist)
		R = (3.0*hole_size + spread_dist*rows-2.0)/(4.0*4)
		if J == 1:
			self.poslist.append([math.pi/2.0, 1.75*R, R])
		else:
			for j in range(J):
				angle = float(j) * \
						(math.pi-2.0*math.sin(radius/R)) / \
						(float(J)-1.0)+math.sin(radius/R)
				self.poslist.append([angle, R*math.cos(angle), R*math.sin(angle), R])
		
		self.poslist.sort(reverse=True, key=lambda p: (p[0] + oaf * p[3] if p[0] > math.pi/2.0 else p[0] - oaf * p[3]))

		self.circle_image_rad = self.width
		out_width = CANVAS_WIDTH #154 + rows * 48 + 10
		out_height = CANVAS_HEIGHT #82 + rows * 24 + 10

		for i in range(total_delegates):
			x = round(self.poslist[i][1]*100.0+(out_width/2) - self.circle_image_rad/2)
			y = round(out_height - 100.0*(self.poslist[i][2])-5.0 - self.circle_image_rad/2)
			self.canvas.create_image(x, y, anchor=tk.NW, image=(self.img2 if i < other_color else self.img) )

		

root = tk.Tk()
root.geometry("850x950")
root.title("Parliament GUI Generator")
app = UI(master=root)
app.mainloop()
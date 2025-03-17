NDefines_Graphics.NGraphics.COUNTRY_FLAG_TEX_MAX_SIZE = 2048	--default 256
NDefines_Graphics.NGraphics.COUNTRY_FLAG_SMALL_TEX_MAX_SIZE = 512 	--default 64
NDefines_Graphics.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_WIDTH = 10 	--default 10
NDefines_Graphics.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_HEIGHT = 8196 	--default 4096
NDefines_Graphics.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_WIDTH = 41 	--default 41
NDefines_Graphics.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_HEIGHT = 24000 	--default 16384

NDefines_Graphics.NGraphics.COMMANDGROUP_PRESET_COLORS_HSV = { -- thanks Better Preset Colors
		00.0/360.0, 0.95, 0.86,
		39.0/360.0, 0.95, 0.86,
		55.0/360.0, 0.95, 0.86,
		80.0/360.0, 0.95, 0.86,
		117.0/360.0, 0.95, 0.80,
		177.0/360.0, 0.95, 0.86,
		201.0/360.0, 0.95, 0.80,
		279.0/360.0, 0.95, 0.92,
		318.0/360.0, 0.95, 0.86,
		00.0/360.0, 0.00, 0.86
}

NDefines_Graphics.NMapMode.MAP_MODE_MANPOWER_RANGE_MAX = 1000000	-- When a state has that much manpower, it will be colored with the color MAP_MODE_MANPOWER_RANGE_COLOR_TO. Everything below that will have an interpolated color.

NDefines_Graphics.NInterface.MINIMAP_TOGGLE_SHIFT = 203				-- horizontal shift for minimap to close it

for k,v in pairs( NDefines_Graphics ) do NDefines[k] = v end

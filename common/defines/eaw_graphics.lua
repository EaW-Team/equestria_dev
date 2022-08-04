NDefines_Graphics.NGraphics.COUNTRY_FLAG_TEX_MAX_SIZE = 2048	--default 256
NDefines_Graphics.NGraphics.COUNTRY_FLAG_SMALL_TEX_MAX_SIZE = 512 	--default 64
NDefines_Graphics.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_WIDTH = 10 	--default 10
NDefines_Graphics.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_HEIGHT = 8196 	--default 4096
NDefines_Graphics.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_WIDTH = 41 	--default 41
NDefines_Graphics.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_HEIGHT = 24000 	--default 8192

NDefines_Graphics.NGraphics.VICTORY_POINT_MAP_ICON_TEXT_CUTOFF = {200, 350, 600}  	-- Vanilla is 150, 250, 500
NDefines_Graphics.NGraphics.VICTORY_POINTS_DISTANCE_CUTOFF = {300, 500, 1000} 		-- Vanilla is 250, 500, 1000

NDefines_Graphics.NGraphics.COMMANDGROUP_PRESET_COLORS_HSV = { -- thanks Better Preset Colors
	00.0/360.0, 0.95, 0.86,
	39.0/360.0, 0.95, 0.86,
	55.0/360.0, 0.95, 0.86,
	80.0/360.0, 0.95, 0.86,
	117.0/360.0, 0.95, 0.86,
	177.0/360.0, 0.95, 0.86,
	201.0/360.0, 0.95, 0.86,
	279.0/360.0, 0.95, 0.86,
	300.0/360.0, 0.95, 0.86,
	00.0/360.0, 0.00, 0.86
} 

for k,v in pairs( NDefines_Graphics ) do NDefines[k] = v end

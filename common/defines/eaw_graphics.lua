NDefines_Graphics.NGraphics.COUNTRY_FLAG_TEX_MAX_SIZE = 2048	--default 256
NDefines_Graphics.NGraphics.COUNTRY_FLAG_SMALL_TEX_MAX_SIZE = 512 	--default 64
NDefines_Graphics.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_WIDTH = 10 	--default 10
NDefines_Graphics.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_HEIGHT = 8196 	--default 4096
NDefines_Graphics.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_WIDTH = 41 	--default 41
NDefines_Graphics.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_HEIGHT = 24000 	--default 8192

NDefines_Graphics.NGraphics.VICTORY_POINT_MAP_ICON_TEXT_CUTOFF = {200, 350, 600}  	-- Vanilla is 150, 250, 500
NDefines_Graphics.NGraphics.VICTORY_POINTS_DISTANCE_CUTOFF = {300, 500, 1000} 		-- Vanilla is 250, 500, 1000

for k,v in pairs( NDefines_Graphics ) do NDefines[k] = v end

local FILETYPE = arg[1]
local SPRITEPATH = arg[2]
local TAG = arg[3]

local function fetchAllSprites(dirpath)
	local sprites = {}
	local command
	if package.config:sub(1,1) == '\\' then
		command = string.format('dir "%s" /b', dirpath)
	else
		command = string.format('ls -1 "%s"', dirpath)
	end
	local p = io.popen(command)
	if not p then return sprites end
	for filename in p:lines() do
		if filename:match("%.tga$") then
			local name = filename:gsub("%.tga$", "")
			table.insert(sprites, name)
		end
	end
	p:close()
	return sprites
end

local function createSpriteEntry(tag, filename)
	local spritedef = string.format(
[[
	SpriteType = {
		name = "GFX_focus_%s"
		textureFile = "gfx/interface/goals/%s/%s.tga"
	}
]], filename, tag, filename)
	return spritedef
end

local function createSpriteShineEntry(tag, filename)
	local spriteshinedef = string.format(
[[
	SpriteType = {
		name = "GFX_focus_%s_shine"
		texturefile = "gfx/interface/goals/%s/%s.tga"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {
			animationmaskfile = "gfx/interface/goals/%s/%s.tga"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}

		animation = {
			animationmaskfile = "gfx/interface/goals/%s/%s.tga"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = { x = 0.0 y = 0.0 }
			animationtexturescale = { x = 1.0 y = 1.0 }
		}
		legacy_lazy_load = no
	}
]], filename, tag, filename, tag, filename, tag, filename)
	return spriteshinedef
end

local function generateGFXFile(tag, sprites)
	local filename
	if (FILETYPE == "focus") then
		filename = "focus_" .. tag .. ".gfx"
	elseif (FILETYPE == "shine") then
		filename = "focus_" .. tag .. "_shine.gfx"
	end
	local file = io.open(filename, "w")

	file:write("spriteTypes = {\n")
	for _, sprite in ipairs(sprites) do
		if (FILETYPE == "focus") then
			file:write(createSpriteEntry(tag, sprite))
		elseif (FILETYPE == "shine") then
			file:write(createSpriteShineEntry(tag, sprite))
		end
	end
	file:write("}")

	file:close()
end

local sprites = fetchAllSprites(SPRITEPATH)

generateGFXFile(TAG, sprites)

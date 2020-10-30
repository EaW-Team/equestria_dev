Mini mod by Thinking_waffles

Notes for integration into Equestria at War

I have provided some generic plane texture which could be useful for stuffs like rebels, the problem is that cosmetic tag model variations don't work for planes in 1.9.3

Italian planes have Wingbardian roundels
French planes have Aquileian roundels


To create new ones create a copy of a base game plane texture (for example take SOV_plane_light_texture and copy it as STG_plane_light_texture, although any name can be used)
in gfx/entities have a file to define custom meshes (equestria_meshes_planes.gfx for example)

pdxmesh = {
	name = "STG_plane_light_mesh" #->name to be referenced elsewhere
	file = "gfx/models/units/planes/SOV_plane_light.mesh" #->model upon which you will put your texture
	animation = { id = "idle" type = "fighter_default_idle_animation" }

	meshsettings = {
		texture_diffuse = "STG_plane_light_diffuse.dds" #->your new texture
		texture_normal = "SOV_plane_light_normal.dds" # you probably won't need to change those two
		texture_specular = "SOV_plane_light_spec.dds" #->for some it's _spec and others its _specular
	}
}

#In gfx/entities/unit_planes (or equivalent)

entity = { #please copy the original and modify accordingly this is just an example
	name = "STG_light_plane_entity" #affect all light planes for STG, can also be used on cultures with commonwealth_gfx or unique model like with "BUL_tac_bomber_equipment_0_entity"
	pdxmesh = "STG_plane_light_mesh" 
	state = { name = "fire" animation = "idle" 
		event = { time = 0 node = "gun1"	particle = "plane_mg_muzzle_particle" keep_particle = yes sound = { soundeffect = "airplane_light_fire" } }
		event = { time = 0.02 node = "gun2"	particle = "plane_mg_muzzle_particle" keep_particle = yes }
		event = { trigger_once = yes sound = { soundeffect = "distance_airplane_light_fire" } }
	}
	state = { name = "bomb" animation = "idle" 
		event = { time = 0 particle = "bomb_particle" keep_particle = yes sound = { soundeffect = "airplane_bomb" } }
	}
	state = { name = "idle" animation = "idle"
		event = { trigger_once = yes sound = { soundeffect = "airplane_idle" } }
		event = { trigger_once = yes sound = { soundeffect = "distance_airplane_idle" } }
	}
	state = { name = "crash" animation = "idle" 
		event = { time = 0 node = "root"	particle = "explosion_particle" keep_particle = yes sound = { soundeffect = "airplane_crash" } }
		event = { trigger_once = yes sound = { soundeffect = "distance_airplane_crash" } }
		}
	state = { name = "explode" animation = "idle" 
		event = { time = 0 particle = "vehicle_explode_effect" keep_particle = yes }
		event = { trigger_once = yes sound = { soundeffect = "distance_airplane_crash" } }
	}
	scale = 0.144
	#you can add version = [NUMBER] to set it as prioritary compared to other models, useful if you have a dlc model and then need a replacement for non dlc owners 
	#dlc models won't happear in game for non dlc owners. Due to the free nature of the Polish dlc and the 5 planes it contains I recommend its use but please be aware that since release some models are swapped in that dlc (like the interwar fighter is used as the light fighter and vice versa.
}


for i in range(20):
    v = []
    for j in range(20):
        v.append("			title_%d_visible = { always = %s }" % (j, "yes" if j == i else "no"))
        v.append("			message_%d_visible = { always = %s }" % (j, "yes" if j == i else "no"))
    t = '''	eaw_diplo_popup_%d = {
		context_type = player_context
		window_name = "eaw_diplo_popup_window"

		visible = {
			is_ai = no
			has_variable = eaw_diplo_popup_type^%d
		}

		dirty = eaw_diplo_popup_type^%d

		effects = {
			ok_button_click = {
				clear_variable = eaw_diplo_popup_sender^%d
				clear_variable = eaw_diplo_popup_reciever^%d
				clear_variable = eaw_diplo_popup_type^%d
			}
		}

		triggers = {
			diplo_war_large_icon_visible = {
				check_variable = { eaw_diplo_popup_type^%d = 4 } # war
			}
			diplo_war_large_icon2_visible = {
				check_variable = { eaw_diplo_popup_type^%d = 4 } # war
			}
%s
		}

		properties = {
			sender_flag = {
				image = "[?eaw_diplo_popup_sender^%d.GetFlag]"
			}
			receiver_flag = {
				image = "[?eaw_diplo_popup_reciever^%d.GetFlag]"
			}
		}
	}''' % (i, i, i, i, i,i,i, i, "\n".join(v), i, i)
    g = '''		instantTextBoxType = {
			name = "title_%d"
			position = { x = 110 y = 36 }
			textureFile = ""
			font = "hoi_18mbs"
			borderSize = {x = 0 y = 0}
			text = "eaw_diplo_popup_window_title_%d"	
			maxWidth = 280
			maxHeight = 24
			fixedsize = yes
			format = centre
		}''' % (i, i)
    #print(t)

l = [f'eaw_diplo_popup_window_message_{i}:0 "[This.GetDiploPopupMessage{i}]"' for i in range(20)] + [f'eaw_diplo_popup_window_title_{i}:0 "[This.GetDiploPopupTitle{i}]"' for i in range(20)]
l = [f'eaw_diplo_popup_window_message_{i}_invite_faction:0 "[?eaw_diplo_popup_reciever_{i}^0.GetNameDef] joined [?eaw_diplo_popup_sender_{i}.GetNameDef]"' for i in range(20)] + [f'eaw_diplo_popup_window_title_{i}_invite_faction:0 "Transmission from [?eaw_diplo_popup_sender_{i}.GetNameDef]"' for i in range(20)]
l = [f'eaw_diplo_popup_window_message_{i}_join_faction:0 "[?eaw_diplo_popup_sender_{i}.GetNameDef] joined [?eaw_diplo_popup_reciever_{i}^0.GetNameDef]"' for i in range(20)] + [f'eaw_diplo_popup_window_title_{i}_join_faction:0 "Transmission from [?eaw_diplo_popup_sender_{i}.GetNameDef]"' for i in range(20)]
l = [f'eaw_diplo_popup_window_message_{i}_puppet:0 "[?eaw_diplo_popup_sender_{i}.GetNameDef] became a subject of [?eaw_diplo_popup_reciever_{i}^0.GetNameDef]"' for i in range(20)] + [f'eaw_diplo_popup_window_title_{i}_puppet:0 "Transmission from [?eaw_diplo_popup_sender_{i}.GetNameDef]"' for i in range(20)]
l = [f'eaw_diplo_popup_window_message_{i}_free:0 "[?eaw_diplo_popup_sender_{i}.GetNameDef] broke free from the influence of [?eaw_diplo_popup_reciever_{i}^0.GetNameDef]"' for i in range(20)] + [f'eaw_diplo_popup_window_title_{i}_free:0 "Transmission from [?eaw_diplo_popup_sender_{i}.GetNameDef]"' for i in range(20)]
l = [f'eaw_diplo_popup_window_message_{i}_become_major:0 "[?eaw_diplo_popup_sender_{i}.GetNameDef] is now considered a major power"' for i in range(20)] + [f'eaw_diplo_popup_window_title_{i}_become_major:0 "Transmission from [?eaw_diplo_popup_sender_{i}.GetNameDef]"' for i in range(20)]
l = [f'eaw_diplo_popup_window_message_{i}_lose_major:0 "[?eaw_diplo_popup_sender_{i}.GetNameDef] is no longer considered a major power"' for i in range(20)] + [f'eaw_diplo_popup_window_title_{i}_lose_major:0 "Transmission from [?eaw_diplo_popup_sender_{i}.GetNameDef]"' for i in range(20)]

sl = []
for i in range(20):
    sl.append(
        '''defined_text = {
	name = GetDiploPopupMessage%d
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 1 } }
		localization_key = eaw_diplo_popup_window_message_%d_invite_faction
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 2 } }
		localization_key = eaw_diplo_popup_window_message_%d_invite_faction
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 3 } }
		localization_key = eaw_diplo_popup_window_message_%d_puppet
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 6 } }
		localization_key = eaw_diplo_popup_window_message_%d_free
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 7 } }
		localization_key = eaw_diplo_popup_window_message_%d_become_major
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 8 } }
		localization_key = eaw_diplo_popup_window_message_%d_lose_major
	}
}''' % (i,i,i,i,i,i,i,i,i,i,i,i,i)
    )
    sl.append(
        '''defined_text = {
	name = GetDiploPopupTitle%d
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 1 } }
		localization_key = eaw_diplo_popup_window_title_%d_join_faction
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 2 } }
		localization_key = eaw_diplo_popup_window_title_%d_join_faction
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 3 } }
		localization_key = eaw_diplo_popup_window_title_%d_puppet
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 6 } }
		localization_key = eaw_diplo_popup_window_title_%d_free
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 7 } }
		localization_key = eaw_diplo_popup_window_title_%d_become_major
	}
	text = {
		trigger = { check_variable = { eaw_diplo_popup_type^%d = 8 } }
		localization_key = eaw_diplo_popup_window_title_%d_lose_major
	}
}''' % (i,i,i,i,i,i,i,i,i,i,i,i,i)
    ) 
print("\n".join(sl))
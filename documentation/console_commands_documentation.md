# Console Commands

Console commands are split into two categories: actual commands and tweakable
variables.

Tweakable variables differ from console command in that they are more
specialized and usualy modify a single variable in the game. They are often
used to toggle on or off some behavior.

Console command are more general purpose and can affect a wider variety of
stuff, such as reloading some file, toggling off some gfx effects, starting
a civil war, ...

## Table of Content

* [All Console Commands](#all-console-commands)
* [All Tweakable Variables](#all-tweakable-variables)

## 3dstats

Toggles 3D Stats

## AddFunds
* Aliases: mio.AddFunds, IndustrialOrganisation.AddFunds
* Arguments: \<Industrial Organisation token\> (optional), \<Funds amount\> (optional)

"Add funds to one or all Military Industrial Organisations
ex:
AddFunds org_token 2000
AddFunds org_token // default added funds is NDefines::NIndustrialOrganisation::FUNDS_FOR_SIZE_UP
AddFunds 2000 // Funds added to all the player's MIOs
AddFunds // default funds amount added to all the player's MIOs"

## AddSize
* Aliases: mio.AddSize, IndustrialOrganisation.AddSize
* Arguments: \<Industrial Organisation token\> (optional), \<capacity amount\> (optional)

"Add sizes to one or all Military Industrial Organisations.
ex:
AddSize org_token 2
AddSize org_token // adds 1 size
AddSize 2 // adds input size to all the player's MIOs
AddSize // adds 1 size to all the player's MIOs"

## AddTaskCapacity
* Aliases: mio.AddTaskCapacity, IndustrialOrganisation.AddTaskCapacity
* Arguments: \<Industrial Organisation token\> (optional), \<capacity amount\> (optional)

"Add task capacity to one or all Military Industrial Organisations.
Value can be negative but final task capacity will be capped at 0.
ex:
AddTaskCapacity org_token 2
AddTaskCapacity org_token // adds 1 capacity
AddTaskCapacity 2 // adds input capacity to all the player's MIOs
AddTaskCapacity // adds 1 capacity to all the player's MIOs"

## Agency.Instant

Activates Operation.Instant, IntelNetwork.Instant, Agency.InstantSlotUnlock and Agency.Autocomplete

## Audio.PlayEffect
* Arguments: effect_name

Play the specified sound effect

## CrashReporter.DeleteCrashData

Delete local crash dumps older than X days.

## CrashReporter.SimulateCrash

Simulates a crash (resulting in the game exiting).

## IP

Shows your IP

## InternationalMarket.AddSubsidyForTags
* Arguments: \<CIC\>, \<Archetype\>, \<Tag\>

Add a Equipment Subsidy to the player's international market.

## InternationalMarket.AddSubsidyForTrigger
* Arguments: \<CIC\>, \<Archetype\>, \<ScriptedTrigger\> 

Add a Equipment Subsidy to the player's international market.

## InternationalMarket.CancelPurchase
* Arguments: \<SellerTag\>, \<BuyerTag\>, \<ContractIndex\>

Cancel the purchase contract between the seller and the buyer

## InternationalMarket.Dev.SetMarketRequestAutomation
* Arguments: \<AcceptMarketAccess\>, \<SendMarketAccess\>, \<AcceptPurchase\>

Set the market requests automation state

## InternationalMarket.ReleaseFromMarketStockpile
* Arguments: \<EquipmentName\>, \<EquipmentAmount\>

Release equipment to main stockpile from market stockpile

## InternationalMarket.RequestPurchase
* Arguments: \<SellerTag\>, \<BuyerTag\>, \<PaidCivs\>, \<EquipmentName\>, \<EquipmentAmount\>

Request Equipment Purchase.

## InternationalMarket.ReserveToMarketStockpile
* Arguments: \<EquipmentName\>, \<EquipmentAmount\>

Reserve equipment from main stockpile to market stockpile

## InternationalMarket.SetPriceLevel
* Arguments: \<EquipmentName\>, \<Level\>

Sets the price level for the given equipment in the Market Stockpile

## ListIncorrectCenterOfRegions
* Not available in release build

List regions center point that is located within another region

## PopsFileStorage.Sync
* Not available in release build

Sync POP File Storage

## PostEffectVolumes.Default
* Arguments: posteffect_values name
* Not available in release build

Toggles default posteffect values

## PrintSynchStuff

Prints random count and seed

## SetRandomCount

Sets the randomcount to 0 or arg

## acclimatization
* Aliases: acc
* Arguments: \<climate_name\>, \<value 0-100\>

Sets the acclimatization on a division(s).

## add_autonomy
## add_cic_bank
* Aliases: stonks, cic, bank
* Arguments: \<value\>

Add CIC to the CIC bank (negative value subtracts)

## add_core
* Arguments: \<Province ID\>

Add core

## add_critical_hit
* Arguments: \<critical_hit_name\>

add critical hit to selected ships

## add_diplo

Adds diplomatic entroute

## add_equipment
* Aliases: ae
* Arguments: equipment amount, equipment name

Gives player amount of equipment that has the specified name

## add_exile_manpower
* Arguments: \<TAG\>, \<value\>

Adds legitimacy to specified tag. add_legitimacy TAG amount

## add_fake_armies

Creates fake intel armies for the player

## add_fleet_arrow
* Arguments: color
* Not available in release build

Add an arrow around a strategic region

## add_ideas
* Arguments: all|\<idea1\> \<idea2\> ...\>

Adds ideas (ministers or national spirits) with \<ID\> to the country. Use 'all' to add them all

## add_intel

Set the values of a static intel pool against a specific country. E.g. `add_intel GER POL army=10`

## add_latest_equipment
* Aliases: ale
* Arguments: equipment amount

Gives player amount of latest equipment variants

## add_legitimacy
* Arguments: \<TAG\>, \<value\>

Adds legitimacy to specified tag. add_legitimacy TAG amount

## add_mines
* Aliases: mines
* Arguments: \<Amount of naval mines\>

Add naval mines to selected region(s)

## add_opinion
* Arguments: \<Country tag\>

Add opinion to/from tag

## add_party_popularity
* Arguments: \<party\>, \<amount\>

Adds party popularity for specified party to the current country

## add_rain
* Arguments: \<rain_amount\>

Adds rain to the selected province

## add_snow
* Arguments: \<snow_amount\>

Adds snow to the selected province

## add_stability
* Aliases: st
* Arguments: unity amount

Gives/removes stability from player

## add_subsidies
## add_subsidies_second
## add_tech
## add_temp_supply_node
* Not available in release build

Add temp supply node

## add_temporary_buff
* Arguments: \<buff_index\>

adds temporary buff to selected units

## add_war_support
* Aliases: ws
* Arguments: unity amount

Gives/removes war support from player

## ai

Toggles the AI on or off

## ai_accept
* Aliases: yesman

Toggles AI always accept diplomacy

## ai_dump
* Aliases: aidump
* Not available in release build

Dump AI data to log file

## ai_force_equipment

Force the AI to only spend army XP on equipment design

## ai_force_template

Force the AI to only spend army XP on template design

## ai_front_dump
* Aliases: aifrontdump
* Not available in release build

Dump AI front data to log file, needs to have a unit selected

## ai_front_id

Get the address of selected group's front debug id

## ai_idea_desire_log

Prints AI desire for ideas to log. For Current country only.

## ai_invasion

Toggles AI AI naval invasions

## ai_pp_log

Prints AI use of PP to log

## ai_research_log
* Not available in release build

Toggles ai research logging

## ai_trace
* Not available in release build

Toggles the AI Trace window

## aircombat
* Aliases: airc
* Arguments: \<scenario name\>, \<result name\>, \<province id\>, \<state id with airbase\>, \<state id with airbase\>, \<equipment type\>, \<equipment type\>, [equipment creator country], [equipment creator country]
* Not available in release build

Spawns an air combat in desired location.

## airealism

Enable realistic AI

## aiview

Enable AI debug info

## allowdiplo
* Aliases: adiplo, nocb

Allows to use all diplomatic actions for no matter the rules.

## allowideas

Allows to learn all ideas.

## allowoperations

Allows to execute all operations.

## allowtraits

Allows to learn all traits.

## analyzetheatres
* Aliases: anth

Analyze theatres for errors.

## annex
* Arguments: \<Target Country Tag\>

Begin annex/annexes the specified tag

## armageddon

Deliver a thermonuclear strike to every state in the game.

## bloom
* Not available in release build

Toggles bloom

## bop_add
* Arguments: \<ID\>, \<value\>

Changes the value of the specified power balance.

## bop_addmod
* Arguments: \<ID\>, \<ModID\>

Adds static modifier to a power balance.

## bop_remove
* Arguments: \<ID\>

Deactivates a power balance for the current country.

## bop_rmmod
* Arguments: \<ID\>, \<ModID\>

Removes static modifier from a power balance.

## bop_set
* Arguments: \<ID\>

Activates a power balance for the current country.

## bop_show

Shows current country's active power balances.

## browser
* Arguments: url
* Not available in release build

Show browser window

## build_war_blobs

Prints a list of all your wars

## building_health
* Aliases: bhealth
* Arguments: \<building type\>, \<state or prov id\>, \<building level\>, \<health to add\>

Changes specified building health

## bypass_invasion_superiority_check
* Aliases: bisc

Ignore superiority in the strategic areas crossed by a naval invasion order

## cameraclamp

Toggles the camera clamping

## cityreload

Reloads the cities

## civilwar
* Arguments: \<ideology\>, [target country tag]

Spawns a civil war

## clear_critical_hits

clear all critical hits

## clear_intel_pools

Reset the specified intel pool

## clear_tech
## collaboration

Adds collaborations against selected country. Right click to select a country and use "collaboration 0.3"

## collision
* Aliases: debug_collision

Toggles debug display of normals/bounding boxes/collision

## combat_analyzer
* Arguments: \<TAG1\>, \<TAG2\>, \<OOB1\>, \<OOB2\>, \<num runs\> OPTIONAL, \<num days\> OPTIONAL

Runs a combat between the 2 OOBs owned by the two TAGs either until done or for the specified number of days. 
Using \<num runs\> the combat will be run multiple times and the averages are printed

## combatsound

How often does the combat view give a random sound? 0-50

## combattest
* Not available in release build

combat simulation process

## compare_to_last_checksum

Compare current checksum with the most recent dump

## compliance
* Arguments: amount

increases decreases compliance in a state

## cp
* Arguments: CP amount

Gives command power to player

## createarmygroup

Create field marshal group from selected groups

## createlean
* Not available in release build

Create LEAN textures

## ct

Puts timer info in clipboard

## damage_units
* Arguments: \<org\>, \<str\>, \<num\>

Damage or heal selected units or units under pointer if there is none selected. Enter 1 argument to apply damage for both types, two for individual both types

## dbg_enable_scripted_gui
* Arguments: \<scope\>
* Not available in release build

Enables scripted GUIs

## dbg_prov
* Arguments: \<int\>
* Not available in release build

Sets type of debugging information on provinces.

## dbg_task_force_role_insignia_assignment
* Aliases: tfria

print the role that would be deduced for the selected task force

## dbg_tf_fulfillment

Show the managed fulfillment of a taskforce (exepected number of ships after all ships have been merged in)

## debug

Toggle debug mode on/off.

## debug_achievements
* Not available in release build

Enables popups for achievements to debug them

## debug_achievements_clear
* Not available in release build

Clear all achievements and user stats

## debug_air_vs_land
* Aliases: dbg_cas
* Not available in release build

Toggle debug mode for air vs land combat.

## debug_army_entity
* Aliases: dae

Shows debug entity for all armies

## debug_assert
* Not available in release build

Toggles asserts on/off

## debug_bloom

Toggles Bloom on/off

## debug_borders

Toggles Borders on/off

## debug_checkportraitssanity

Analyse all characters' portraits and write failures in error log

## debug_cities

Toggles Cities painting mode on/off

## debug_commands
* Not available in release build

Printing commandcount to message.log

## debug_crash
* Aliases: crash
* Not available in release build

Crash!

## debug_custom_achievements

For testing custom achievements, clear completion status (delete files on cloud storage) and reload mod achievement files

## debug_diploactions
* Not available in release build

Start Counting diplomatic actions

## debug_dumpdiploactions
* Not available in release build

Dump diplomatic action data to game log

## debug_dumpevents

Dump Event data to game log

## debug_entities
* Not available in release build

Toggles Debug entities

## debug_events

Start Counting events

## debug_force_capitulate
* Aliases: dfc
* Arguments: \<tag\>

forces capitulation of a country on next daily tick

## debug_front_sections
* Aliases: dbg_fs
* Arguments: \<Theatre index\>, \<Front index\>, \<Section index\>

Visual debug of theatres, fronts and sections.

## debug_fronts
* Not available in release build

Toggles interpolated fronts debug

## debug_info
* Not available in release build

Toggles Debug info

## debug_lines
* Not available in release build

Toggles Debuglines

## debug_lockcamera

Toggles Camera locked on/off

## debug_nogui

Toggles GUI on/off

## debug_nomouse

Toggles mouse scrollwheel on/off

## debug_norender

Toggle rendering of map

## debug_off_front_snap
* Aliases: dbg_fsnap
* Not available in release build

Toggles offensive fronts snapping debug

## debug_orders_tree
* Aliases: dot
* Not available in release build

Print out debug about orders chain.

## debug_particle
* Not available in release build

Toggles Particles Debug info

## debug_postfx

Toggles PostFX on/off

## debug_rivers

Toggles Rivers on/off

## debug_show_event_ID

Shows event ID

## debug_sky

Toggles Sky on/off

## debug_smooth

Toggle framesmoothing

## debug_tactics

Toggle visibility of debug tooltip for tactics

## debug_terrain

Toggles Terrain on/off

## debug_texture
* Not available in release build

draws textures like bloom

## debug_textures
* Not available in release build

Writes Texture info to application debug log

## debug_tooltip

Toggles Tooltips on/off

## debug_trees

Toggles Trees on/off

## debug_types
* Not available in release build

Will print the data type for all dynamic reference objects. Can only be used if using RTTI.

## debug_unit_controller_weights
* Aliases: dbg_ucw
* Arguments: \<weight token\>

Visual debug of unit controller weights. Enable track_unit_controller_weights first!

## debug_unit_entity
* Aliases: dbg_ue

Print out the entity hierarchy.

## debug_validate_supply
* Aliases: dbg_sply
* Not available in release build

Toggle debug validate supply cache.

## debug_water

Toggles Water on/off

## debug_wireframe
* Not available in release build

Toggles forced wireframe on/off

## debug_zoom

Zooms in the game

## deironman
* Not available in release build

Removes Ironman status from current game.

## deleteallairwings
* Aliases: delallair

Delete all airwings.

## deleteallunits
* Aliases: delall

Delete all armies and fleets of the specified countries.

## deleteallunitsbut
* Aliases: delallbut

Delete all armies and fleets of ALL countries, except specified one.

## deltat
* Arguments: \<speed factor\>

control animation speeds

## disable_ai

Disables the AI

## disable_weather

Disable weather simulation

## drop_cosmetic_tag
* Arguments: \<country tag\>

Drops 'cosmetic tag' for a specified country

## dump_cached_random_logs

dumps cached random logs

## dump_checksum

Compute and store the checksum in a file

## dump_equipment_loc
* Arguments: desc: Dump equipment descriptions instead of the names, \<country_tag\>: Multiple allowed. Only include loc strings for the given countries. Generic loc strings are included if no tags are given, or with argument 'generic'., \<type\>: Multiple allowed. Only include equipment that are all of the given types, e.g. 'armor anti_tank' will only include tank destroyers., path=\<filepath\>: File path to write the dump to. Default is 'logs/equipment_loc.csv'.

Dumps equipment loc strings to file. All arguments are optional.

## dump_garrison_templates

Dump garrison templates to game log

## dump_synchronized_members

Dump the synchronized game state (the one that has checksum ID 2)

## easy_decisions
* Aliases: ezd

Toggles Easy Decisions Mode which makes all decisions with days_remove take only 1 day to be removed, and all decisions with cost not have any cost or cost trigger.

## effect
* Aliases: e
* Arguments: \<tag\> scripted_effect_name

Runs a scripted effect on selected scope

## empty_fuel_tanks
* Arguments: Fuel amount

Clear fuel tanks of all armies

## emulate_ai_operative_assignment

Log ai operative assignment if it were to run this tick. Takes as first argument the tag of the country to test, default to the player's.

## enable_ai

Enables the AI

## enable_weather

Enable weather simulation

## endraids
* Arguments:  \<Success Level: 1-4 OR { failure, limitedsuccess, success, criticalsuccess}\>
* Not available in release build

Instantly end all active raids, optionally with a specific success level

## error

Show errors in log

## eval_effect

Runs the inlined effect on a selected scope

## eval_trigger

Runs the inlined trigger on a selected scope

## event
* Arguments: event id, \<Target Country Tag\>

Executes an event

## flagsoutput
* Arguments: \<path\>

Creates texture atlas files from memory.

## focus_count
* Arguments: \<Target Country Tag\>

Counts how many focuses a tag has. For science

## force_operative_detection
* Aliases: snitch

Print intel network related information

## forget_medals_and_ribbons
* Not available in release build

Make the game forget that you have earned medals and ribbons.

## fow
* Aliases: debug_fow
* Arguments: \<Province ID\> OPTIONAL

Turns off fog of war in a province or in general

## freefocuses
* Aliases: ff

Enable freely activating any focuses

## fronts

Toggle visibility of the foreign fronts

## fuel
* Aliases: army_juice
* Arguments: Fuel amount

Adds/removes fuel to the player

## fuel_gain
* Arguments: Daily Fuel amount

Adds/removes daily fuel gain for player

## fullscreen

Toggles fullscreen

## gain_xp
* Arguments: \<trait\>

Gain xp for selected leader or for a leader trait

## gamespeed
* Arguments: speed \<0-5\>

Set the current game speed, pausing the game at speed 0.

## gamestate_timer
* Aliases: gstimer
* Arguments: on / off

Enable / Disable recording of how long an hour / day / week etc takes to process.

## gbpaint
* Arguments: layer, channel
* Not available in release build

Toggles gradient border painting

## gbreload
* Not available in release build

Reloads gradient borders

## get_capital
* Arguments: \<Country tag\>

Get the capital of a country

## get_country_flag
* Arguments: \<flag name\>

Gets country flag on specified TAG. Defaults to current country

## get_flag
* Arguments: \<flag name\>

Get a flag

## get_var
* Arguments: \<var name\>

Gets a variable

## goto_province
* Arguments: province id

Centers to province

## goto_region
* Arguments: region id

Centers to region

## goto_state
* Arguments: state id

Centers to state

## grow_intel_network

Grow the intel network in the specified tag

## guibounds
* Aliases: gui

Toggles GUI bounds debug

## hdr
* Not available in release build

Toggles hdr

## hdr_debug
* Not available in release build

Toggles hdr debugging

## help
* Arguments: command name

Print out all console commands or a specific command description.

## helphelp

Double Rainbow help.

## helplog

Print out all console commands to game.log file.

## highlight_encirclements

Toggle highlighting of detected encirclements

## history_logger

Toggle history logger

## hsv
* Not available in release build

Converts RGB to HSV

## human_ai

Toggles AI for Human countries

## imgui

Controls ImGui UIs. See the sub commands.

## instant_prepare

Instantly prepares naval invasions

## instant_wargoal

Generation of wargoals are instant

## instantconstruction
* Aliases: ic

Toggles instant construction cheat.

## instantevents

Ignores event mth s

## instantshiprefit
* Aliases: isr

Toggles instant ship refitting cheat.

## instanttraining
* Aliases: it

Toggles instant army training cheat.

## ironman
* Not available in release build

Applies Ironman status to current game.

## launch_nuke
* Aliases: ln
* Arguments: [Nuke Type], \<Province ID\>, ...

Launch nuke to any specified province(s) without checking any conditions.

## list_flags
* Arguments: \<scope\>

Lists all flags in a scope or for the selected country/state/unitleader

## list_ideas

Dump all ideas to console (ministers or national spirits)

## list_modifiers
* Arguments: \<scope\>

Lists all modifiers in a scope or for the selected country/state/unitleader

## list_temporary_buffs

lists all temporary buffs on selected units

## list_vars
* Arguments: \<scope\>

Lists all variables in a scope or for the selected country/state/unitleader

## loc_check

Check for missing localization

## loc_check_characters

Check characters for missing localization

## loc_check_decisions

Check decisions for missing localization

## loc_check_events

Check events for missing localization

## loc_check_focuses

Check national focuses for missing localization

## loc_check_modifiers

Check modifiers for missing localization

## loc_check_national_spirits

Check national spirits for missing localization

## lock_air_det
* Arguments: \<CountryTag\>, \<Detection\> (0.0-1.0) OPTIONAL

Locks Air Detection for a country, omit detection value to reset

## lock_air_eff
* Arguments: \<CountryTag\>, \<Efficiency\> (0.0-1.0) OPTIONAL

Locks Air Efficiency for a country, omit efficiency value to reset

## log_advisor_trait_errors

Logs all instances of unit leader advisors not having the corresponding unit leader traits.

## manpower
* Arguments: \<Amount\>

Adds manpower to player

## map_icon_reload_type
* Arguments: \<NUM\> or \<help\>
* Not available in release build

Specify a map icon type to reload

## mapmode
* Arguments: Mapmode type (int)

Change mapmode.

## mapnames

Toggle map names

## massconquer
* Aliases: massc
* Not available in release build

Mass conquer tool.

## metrics
* Arguments: log_units|log_pools|player|air_mission|global|unit_assignments \<days\>|decision|log|file\<=file_name\>|tag=\<country_tag\>|add_tag=\<country_tag\>
* Not available in release build

Toggles collecting metrics

## morehumans
* Aliases: humans
* Arguments: num

Adds more humans

## morehumanswithcountries
* Arguments: num

Adds more humans and assigns them to the highest scoring countries available

## moveunit
* Arguments: \<Unit ID\>, \<Province ID\>

Moves a unit to a province

## navalcombatlog
* Not available in release build

logs naval combat

## night
* Not available in release build

Toggles night

## no_wargoal

No need to have a wargoal for declaring war

## nomapicons

Toggles map icons.

## nopausetext

Toggles the pausebanner for nicer screenshots.

## nudge

Go to the nudge tool

## nukes
* Aliases: nuke
* Arguments: \<count\>

add nukes

## observe
* Aliases: spectator

Switches to play no country at all, and no longer shows messages or pauses the game

## occupationpaint
* Aliases: op
* Arguments: tag\<OPTIONAL\>

Toggles occupation painting. If specifying a tag, that country will be occupied.

## oos
* Not available in release build

Out of Synch

## oos_dump
* Aliases: oosdump
* Not available in release build

Generates an oos dump on demand for local client.

## operation_debug
* Arguments: Operation ID, Target Tag

Allows to execute all operations.

## operation_start
* Arguments: Operation ID, Target Tag

Allows to execute all operations.

## operation_test_phase_selection
* Arguments: Operation ID, Target Tag

Test an operation phase.

## pathfind_cache
* Arguments: on / off
* Not available in release build

Enable / Disable the PathFind Cache

## pathfind_stats
* Not available in release build

Print PathFind Cache Stats

## pause_in_hours

Pauses the game after X hours have passed after command is called

## pause_on_trigger

Pauses the game when trigger activates

## pops_account_disconnect_steam
* Not available in release build

Disconnect Paradox account from Steam

## pops_account_login
* Arguments: email, password
* Not available in release build

Login to a POPS Account

## pops_account_logout
* Not available in release build

Login to a POPS Account

## pops_account_status
* Not available in release build

Show whether you are currently logged into POPS or not.

## pp
* Aliases: political_power
* Arguments: PP amount

Gives political power to player

## prep_for_war
* Arguments: \<TAG\>

Make AI country with specified TAG to prepare fight for another country 

## prepareraids
* Arguments:  \<[Optional] the degree to which the raid should be prepared (0.0-1.0)\>
* Not available in release build

Instantly complete preparation of all active raids, optionally to a specific progress level

## prevent_operative_detection

Prevent a country from detecting and harming foreign operatives

## prices

Price Info

## print_controllers

Prints countries controlled by human players.

## print_intel_network

Print intel network related information

## print_intel_values

Print the intel a country has over another

## print_operation_tokens

Runs a scripted effect on selected scope

## print_radar_intel

Print the intel value breakdown generated by radar

## profile
* Arguments: \<on\> \<off\> \<print\> \<clear\>

profile options

## province_ids
* Aliases: pid

Show province IDs on the map

## provtooltipdebug
* Aliases: tdebug

Toggles the debug info in province tooltip

## puppet
* Arguments: \<Target Country Tag\>

Puppets the specified tag

## railroads

Toggle rendering of railroads

## railwaygun
* Aliases: rg
* Not available in release build

create railway gun in supply capital

## railwaygun_damage
* Aliases: rg_damage
* Not available in release build

damage railway guns

## random_seed

reseeds random with specified seed or reseeds random

## randomlog
* Aliases: rlog
* Not available in release build

Toggles the random logs.

## rebuildfronts
* Arguments: \<Country tag\>
* Not available in release build

Rebuild fronts.

## rebuildlayers

Reload mapmodes.

## release
* Aliases: rls
* Arguments: Tag of a country to be released

Released a given country

## reload_textures
* Aliases: rt, reload_texture
* Arguments: \<optional file name filters...\>

Reloads all textures, with an optional filter to reload only files that include the given text

## reloadfx
* Arguments: Arguments: map/mapname/postfx or *.fx filename

Reloads the shader

## reloadinterface

Reloads the entire interface

## reloadoob
* Arguments: \<Target Country Tag\>

Reloads OOBs

## reloadtechnologies

Reloads the technology database

## reloadweather
* Arguments: \<randomseed\>

Reload and regenerate weather

## remove_core
* Arguments: \<Province ID\>

Remove core

## remove_ideas
* Arguments: all|\<idea1\> \<idea2\> ...

Removes ideas (ministers or national spirits) with \<ID\> to the country. Use 'all' to remove them all

## research
* Arguments: \<slot id\> or "all"

Researches an technology from research slot or all.

## research_fast

Base cost of every technology is set to 1 RP

## research_on_icon_click
* Aliases: roic

Research a technology when clicking on technology tree icon

## resign

Resign from the game

## resistance
* Arguments: amount

increases decreases resistance in a state

## restart
* Not available in release build

Restart the game as the current country

## retire_country_leader
## run

Runs the specified file with list of commands

## savecheck

Makes a savegame (Test_01), loads the savegame, makes a new savegame (Test_02). Those savegames should look the same.

## savegame
* Aliases: save

Creates a save file.

## select
* Aliases: sel
* Arguments: \<object id\>, \<object type id\> (optional)
* Not available in release build

select object by id

## set_cosmetic_tag
* Arguments: \<country tag\>, \<cosmetic tag\>

Sets 'cosmetic tag' for a specified country

## set_country_flag
* Arguments: \<flag name\>

Sets country flag on specified TAG for a duration. Defaults to current country and value 1 with infinite duration.

## set_debug_unit_controller
* Aliases: dbg_unit_controller
* Not available in release build

Sets debug unit controller tag, other countries will not update units

## set_flag
* Arguments: \<flag name\>

Set a flag

## set_global_flag
* Arguments: \<flag name\>

Sets the specified global flag to a value. Defaults to 1

## set_mud

Sets mud for the selected province

## set_ruling_party
* Arguments: \<ideology\>

Sets ruling party for the country

## set_var
* Arguments: \<var name\>

Set a variable

## set_weather
* Arguments: \<weather_type\>

Sets the weather for the selected province (and corresponding region)

## setcontroller
* Arguments: country tag, province id

Sets province controller

## setowner
* Arguments: country tag, state id

Sets state owner

## show_all_medals
* Arguments: \<bronze|silver|gold\>

Show all medals as achieved in the grid without actually earning them.

## show_all_ribbons

Show all ribbons as achieved in the grid without actually earning them.

## show_enemy_ships

Toggle always showing of enemy ships

## show_medal
* Arguments: \<medal_token\>, \<bronze|silver|gold\>

Show the popup for earning a medal without actually earning it.

## show_ribbon
* Arguments: \<ribbon_token\>

Show the popup for earning a ribbon without actually earning it.

## show_ships

Toggle always showing of player ships

## show_xp_gain
* Aliases: xp_gain

Show XP gain information.

## simplified_transport

Toggle simplified naval transports

## sleep
* Aliases: wait
* Arguments: time in sec
* Not available in release build

Sleep

## social_addfriend
* Arguments: Context Index, Account ID
* Not available in release build

Add a friend to friends list

## social_debuginfo
* Not available in release build

Print debug info about the social layer

## social_joinroom
* Arguments: Context Index, Room Name, Nick Name
* Not available in release build

Join a chat room using the given social context

## social_sendmessage
* Arguments: Context Index, Room Name, Message
* Not available in release build

Send a message to a chat room.

## sp_add_mastermind

"Add a scientist with max skill in all specializations"

## sp_add_scientist
* Arguments: \<Level\> (optional), \<Specialization\> (optional)

"Add a scientist. Is specified a specialization and level that will be applied to the scientist. If no specialization is specified the level will be applied to all.
ex:
sp_add_scientist 3 nuclear
sp_add_scientist 2
sp_add_scientist"

## sp_add_selected_scientist_level
* Arguments: \<Level\>, \<Specialization\> (optional)

"Add level and if specified, specifically to a specialization for a scientist. If no specialization is specified, the level will be added for each specialization. Requires the facility view with an attached scientist to be open.
ex:
sp_add_scientist_level 3 nuclear
sp_add_scientist_level 2"

## sp_add_selected_scientist_trait
* Arguments: \<Trait\>

"Add a trait to the scientist. Requires the facility view with an attached scientist to be open.
ex:
sp_add_scientist_trait my_trait_token"

## sp_available

"Trigger available returns true for all Special Projects.
ex:
sp_available"

## sp_breakthrough
* Aliases: sp_br
* Arguments: \<amount\> optional \<specialization\>

"Create breakthrough points."

## sp_fast

"All phases in Special Projects take now 1 day to complete.
For prototype phase, it's the iterations that will take 1 day. And it will require as many iterations as usual.
ex:
sp_fast"

## sp_instant

"All started Special Projects finish on the daily tick. It skips the iterations of the Prototyping phase and their reward.
ex:
sp_instant"

## sp_prototype_reward
* Aliases: spr

"Trigger a specified prototype reward during a project."

## sp_remove_selected_scientist_trait

"Remove a trait from the scientist. Requires the facility view with an attached scientist to be open.
ex:
sp_remove_selected_scientist_trait my_trait_token"

## sp_research_all
* Aliases: sp_ra

"Research all special projects. If no scientist exist it will create one, otherwise it will pick an arbitrary one. Imagine there is a secret hidden facility
in a controlled province where the projects are researched."

## sp_set_selected_scientist_level
* Arguments: \<Level\>, \<Specialization\> (optional)

"Set level and if specified, specifically to a specialization for a scientist. If no specialization is specified, the level will be added for each specialization. Requires the facility view with an attached scientist to be open.
ex:
sp_set_scientist_level 3 nuclear
sp_set_scientist_level 2"

## sp_unlock_all

"All Special Projects are always visible and available. Whether or not the triggers returns true, and whether the parents are completed.
ex:
sp_unlock_all"

## spawn
* Arguments: \<SubUnit Type\>, \<Province ID\>, \<Amount\>
* Not available in release build

Spawns a unit in a province

## spawn_3D_models
## spawnactor
* Arguments: \<Actorname\>, \<Province ID\>, \<Animation\> OPTIONAL

Spawns an actor with an optional animation

## srgb
* Not available in release build

Toggles sRGB

## supply_toggle_flow_penalties
* Not available in release build

Toggle the supply penalties due to bad supply flow

## tag
* Arguments: \<Country tag\>

Switch tag to another country

## tag_color

Test setting a country's color

## teleport
* Aliases: tp
* Arguments: \<province_id\>

Teleports selected armies or ships to the specified province

## test
* Not available in release build

This is a placeholder command. Use it for your debug code if you need to quickly test something locally. Or copy and paste it to create a new console command.

## test_log

Enable / Disable tests

## test_naval_move_danger
* Arguments: \<from region id\>, \<to region id\>
* Not available in release build

Tests if path between two regions is blocked for surface warships

## test_save_mode

Sets if save game for failed test should be for current or previous day

## testevent
* Arguments: \<Event ID\>, \<Character ID\>

Tests an event without triggering it

## testrtti
* Arguments: \<test case\>

Tests performance for RTTI

## testtool
* Not available in release build

Testing tool.

## theatersrebuild
* Aliases: trebuild
* Not available in release build

Rebuilds all theatres in the world. All orders will be cleaned.

## threat
* Aliases: tension
* Arguments: threat amount

Adds or show threat level of player

## time

What time is it?

## timer

Prints out debug timing info

## timer_dump

Dumps debug timing info

## timer_reset

Resets debug timing

## timer_restart

Restarts (resets and starts) debug timing

## timer_start

Starts debug timing

## timer_stop

Stops debug timing

## toggle_hidden_techs
* Aliases: tht

"Toggle show/hide all hidden techs."

## toggle_offset_ai_daily_update
* Not available in release build

Whether a country's ai daily update should be spread over a day

## toggle_silhouette_portraits
* Not available in release build

Enables and disables silhouette portraits.

## track_unit_controller_weights
* Aliases: track_ucw

Will start tracking unit controller weights for current country, should be used together with debug_unit_controller_weights to view the data.

## traderoutes

Toggle visibility of trade routes

## trigger
* Aliases: t
* Arguments: \<tag\> scripted_trigger_name

Runs a scripted trigger on selected scope

## trigger_ability
* Arguments: \<ability_name\>

triggers an ability

## trigger_docs
* Aliases: effect_docs, scripting_docs, docs

Print docs for triggers, effects and variables

## unit_address

Get the address of the first selected unit, for debugging

## unit_stats

lists stats of selected units

## update_loc
* Arguments: localization tag

Updates the localization tag file

## updateequipments

Updates the equipment database

## updatesubunits

Updates the subunit database

## version

Show current game version

## war_relations
* Arguments: \<tag\>

Prints war relations info

## weather

Toggle weather simulation

## whitepeace
* Aliases: wp
* Arguments: \<country tags\>

White peace with the specified countries.

## window
* Aliases: wnd
* Arguments: Arguments: open/close, window gui name

Opens or closes the specified window

## xp
* Arguments: XP amount

Gives Army, navy and air experience to player

## All Tweakable Variables


Tweakable variables have a type which defines how they are used.

Boolean variables are toggled on and off just by entering their name in the
console. They can also be force enabled by entering the name of the variable
followed by a none zero number, or force disabled by using zero.

Examples:
```
> Agency.AutoComplete
[ Agency.AutoComplete ] Enabled
> Agency.AutoComplete
[ Agency.AutoComplete ] Disabled
> Agency.AutoComplete
[ Agency.AutoComplete ] Enabled
> Agency.AutoComplete 1
[ Agency.AutoComplete ] Enabled
> Agency.AutoComplete 0
[ Agency.AutoComplete ] Disabled
```

Integer and Float variables are set to a value by entering the name of the
variable followed by the desired value. Only entering the name of the variable
will print its current value. Note that they can be clamped within a range by
code.

Examples:
```
> Audio.Debug.LevelsSampleRate
[ Audio.Debug.LevelsSampleRate ] Value 20
> Audio.Debug.LevelsSampleRate 40
[ Audio.Debug.LevelsSampleRate ] Value 40
> Audio.Debug.LevelsSampleRate
[ Audio.Debug.LevelsSampleRate ] Value 40
```
## Agency.AutoComplete
* Type: Boolean
## Agency.InstantSlotUnlock
* Type: Boolean
## Agency.KeepExcessOperatives
* Type: Boolean
## Audio.Compressor
* Type: Boolean
* Not available in release build
## Audio.Debug
* Type: Boolean
* Not available in release build
## Audio.Debug.ExtendedRange
* Type: Boolean
* Not available in release build
## BattleSound.Debug
* Type: Boolean
* Not available in release build
## BattleSound.PlayBackground
* Type: Boolean
* Not available in release build
## BorderLOD.Threaded
* Type: Boolean
* Not available in release build
## CounterIntelligence.TestShieldColors
* Type: Boolean
## Debug.DeleteUnitEachTick
* Type: Boolean
* Not available in release build
## Debug.OldCombat
* Type: Boolean
## Decision.FastRemove
* Type: Boolean
## Decision.NoChecks
* Type: Boolean
## Draw.Borders
* Type: Boolean
* Not available in release build
## Draw.Objects
* Type: Boolean
* Not available in release build
## Draw.Postfx
* Type: Boolean
* Not available in release build
## Draw.Refractions
* Type: Boolean
* Not available in release build
## Draw.Rivers
* Type: Boolean
* Not available in release build
## Draw.ShadowBlur
* Type: Boolean
* Not available in release build
## Draw.Shadows
* Type: Boolean
* Not available in release build
## Draw.Terrain
* Type: Boolean
* Not available in release build
## Draw.Transparent
* Type: Boolean
* Not available in release build
## Draw.Tree
* Type: Boolean
* Not available in release build
## Draw.Water
* Type: Boolean
* Not available in release build
## Focus.AutoComplete
* Type: Boolean
## Focus.IgnorePrerequisites
* Type: Boolean
## Focus.NoChecks
* Type: Boolean
## IntelNetwork.Instant
* Type: Boolean
## Operation.Instant
* Type: Boolean
## PostEffectVolumes.Draw
* Type: Boolean
* Not available in release build
## PostEffectVolumes.Enabled
* Type: Boolean
* Not available in release build
## ShowBorderTypes
* Type: Boolean
* Not available in release build
## ShowTechBonus
* Type: Boolean
* Not available in release build
## Terrain.MipLevels
* Type: Boolean
* Not available in release build
## Tree.MipLevels
* Type: Boolean
* Not available in release build
## Update.Animations
* Type: Boolean
* Not available in release build
## Update.Particles
* Type: Boolean
* Not available in release build
## fa
* Type: Boolean
## resistance_system
* Type: Boolean
## supply_debug.show_debug_lines_rail
* Type: Boolean
* Not available in release build
## supply_debug.show_debug_lines_supply
* Type: Boolean
* Not available in release build
## supply_debug.show_debug_lines_train
* Type: Boolean
* Not available in release build
## supply_debug.show_debug_rivers
* Type: Boolean
* Not available in release build

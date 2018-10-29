NDefines.NGame.START_DATE = "1007.1.1.12"
NDefines.NGame.END_DATE = "1030.1.1.1"

NDefines.NDiplomacy.TENSION_TIME_SCALE_START_DATE = "1007.1.1.12"
NDefines.NTechnology.BASE_TECH_COST = 86
NDefines.NAI.RESEARCH_LAND_DOCTRINE_NEED_GAIN_FACTOR = 0.12 -- Multiplies value based on relative military industry size / country size.
NDefines.NAI.RESEARCH_BONUS_FACTOR = 1.5 				-- To which extent AI should care about bonuses to research
NDefines.NAI.DYNAMIC_STRATEGIES_THREAT_FACTOR = 6.0
NDefines.NAI.BASE_DISTANCE_TO_CARE = 400.0
NDefines.NAI.ATTACK_HEAVILY_DEFENDED_LIMIT = 1.1
NDefines.NAI.SEND_VOLUNTEER_EVAL_BASE_DISTANCE = 100.0
NDefines.NAI.SEND_VOLUNTEER_EVAL_MAJOER_POWER = 1.0
NDefines.NAI.SEND_VOLUNTEER_EVAL_CONTAINMENT_FACTOR = 0.15
NDefines.NAI.DIPLOMACY_FACTION_GLOBAL_TENSION_FACTOR = 0.15
NDefines.NAI.DIPLOMACY_FACTION_NEUTRALITY_PENALTY = 0.2
NDefines.NAI.UPGRADE_DIVISION_RELUCTANCE = 14
NDefines.NAI.FASCISTS_ALLY_FASCISTS = -10
NDefines.NAI.FASCISTS_BEFRIEND_FASCISTS = 0
--NDefines.NAI.MANPOWER_FREE_USAGE_THRESHOLD = 600000			-- If AI has this much manpower he doesn't care about the percentage
NDefines.NAI.MANPOWER_RESERVED_THRESHOLD = 0.1				-- The AI will not deploy more units if he goes below this percentage
NDefines.NAI.NEUTRAL_THREAT_PARANOIA = 1
--NDefines.NAI.DIVISION_CREATE_MIN_XP = 50
--NDefines.NAI.VARIANT_UPGRADE_MIN_XP = 10
NDefines.NGraphics.COUNTRY_FLAG_TEX_MAX_SIZE = 2048
NDefines.NGraphics.COUNTRY_FLAG_SMALL_TEX_MAX_SIZE = 512
NDefines.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_WIDTH = 10
NDefines.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_HEIGHT = 8196
NDefines.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_WIDTH = 41
NDefines.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_HEIGHT = 24000

NDefines.NCountry.SPECIAL_FORCES_CAP_BASE = 0.1					-- Max ammount of special forces battalions is total number of non-special forces battalions multiplied by this and modified by a country modifier
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 32					-- You can have a minimum of this many special forces battalions, regardless of the number of non-special forces battalions you have, this can also be modified by a country modifier
NDefines.NCountry.MAJOR_MIN_FACTORIES = 25 --default 35		-- need at least these many factories to become a major

NDefines.NDiplomacy.MAX_OPINION_VALUE = 100							-- Max opinion value cap.
NDefines.NDiplomacy.MIN_OPINION_VALUE = -300						-- Min opinion value cap.

NDefines.NAI.HOUR_BAD_COMBAT_REEVALUATE = 24 --default 100
NDefines.NAI.PLAN_ACTIVATION_SUPERIORITY_AGGRO = 0.8 --default 1.0		-- How aggressive a country is in activating a plan based on how superiour their force is.

NDefines.NAI.AI_FRONT_MOVEMENT_FACTOR_FOR_READY = 0.1 --default 0.25
NDefines.NAI.PLAN_VALUE_TO_EXECUTE = -0.2 --default -0.5

NDefines.NAI.DEPLOY_MIN_TRAINING_WAR_FACTOR = 0.05	--default 0.25	-- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime
NDefines.NAI.DEPLOY_MIN_EQUIPMENT_WAR_FACTOR = 0.80	--default 90	-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime

NDefines.NAI.MIN_PLAN_VALUE_TO_MICRO_INACTIVE = 0.1 --default 0.2				-- The AI will not consider members of groups which plan is not activated AND evaluates lower than this.

NDefines.NAI.MAX_UNITS_FACTOR_FRONT_ORDER = 3.0	--default 1.5			-- Factor for max number of units to assign to area front orders
NDefines.NAI.DESIRED_UNITS_FACTOR_FRONT_ORDER = 3.0	--default 1.5		-- Factor for desired number of units to assign to area front orders
NDefines.NAI.MIN_UNITS_FACTOR_FRONT_ORDER = 2.0	--default 1.0			-- Factor for min number of units to assign to area front orders

NDefines.NAI.MAX_UNITS_FACTOR_INVASION_ORDER = 0.8	--default 1.0	-- Factor for max number of units to assign to naval invasion orders
NDefines.NAI.DESIRED_UNITS_FACTOR_INVASION_ORDER = 0.8	--default 1.0	-- Factor for desired number of units to assign to naval invasion orders
NDefines.NAI.MIN_UNITS_FACTOR_INVASION_ORDER = 0.8	--default 1.0			-- Factor for min number of units to assign to naval invasion orders
	
NDefines.NAI.MAX_DIST_PORT_RUSH = 40.0	--default 20.0			-- If a unit is in enemy territory with no supply it will consider nearby ports within this distance.
	
NDefines.NAI.MIN_FIELD_STRENGTH_TO_BUILD_UNITS = 0.6	--default 0.7		-- Cancel unit production if below this to get resources out to units in the field
NDefines.NAI.MIN_MANPOWER_TO_BUILD_UNITS = 0.6	--default 0.7				-- Cancel unit production if below this to get resources out to units in the field

NDefines.NAI.VP_LEVEL_IMPORTANCE_HIGH = 50				-- Victory points with values higher than or equal to this are considered to be of high importance.
NDefines.NAI.VP_LEVEL_IMPORTANCE_MEDIUM = 25			-- Victory points with values higher than or equal to this are considered to be of medium importance.
NDefines.NAI.VP_LEVEL_IMPORTANCE_LOW = 5				-- Victory points with values higher than or equal to this are considered to be of low importance.

NDefines.NGraphics.VICTORY_POINT_MAP_ICON_TEXT_CUTOFF = {200, 350, 600}  	-- Vanilla is 100, 250, 500
NDefines.NGraphics.VICTORY_POINTS_DISTANCE_CUTOFF = {300, 500, 1000} 		-- Vanilla is 300, 500, 1500

NDefines.NAI.FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.3
NDefines.NAI.HEAVILY_FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.3
NDefines.NAI.INVASION_DISTANCE_RANDOMNESS = 400

NDefines.NDiplomacy.BASE_STAGE_COUP_DAILY_PP = 0					-- Daily pp cost for staging a coup
NDefines.NDiplomacy.BASE_STAGE_COUP_TOTAL_COST = 9999 				-- Equipment consume factor for stage coup.

NDefines.NMilitary.PLAN_EXECUTE_CAREFUL_MAX_FORT = 4
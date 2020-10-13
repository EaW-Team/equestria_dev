NDefines = {

NGame = {
    START_DATE = "1007.1.1.12",
    END_DATE = "1030.1.1.1",
    HANDS_OFF_START_TAG = "EQS", -- tag for player country for -hands_off runs. use an existing tag that is less likely to affect the game
},

NDiplomacy = {
    TENSION_TIME_SCALE_START_DATE = "1007.1.1.12",
    MAX_OPINION_VALUE = 200,							-- Max opinion value cap.
    MIN_OPINION_VALUE = -200,						-- Min opinion value cap.
    DIPLOMACY_ACCEPT_VOLUNTEERS_BASE = 100,
    VOLUNTEERS_DIVISIONS_REQUIRED = 10,
},

NTechnology = {
    BASE_TECH_COST = 85,
},

NAI = {
    RESEARCH_LAND_DOCTRINE_NEED_GAIN_FACTOR = 0.12, -- Multiplies value based on relative military industry size / country size.
    RESEARCH_BONUS_FACTOR = 1.5,				-- To which extent AI should care about bonuses to research
    DYNAMIC_STRATEGIES_THREAT_FACTOR = 6.0,
    BASE_DISTANCE_TO_CARE = 400.0,
    ATTACK_HEAVILY_DEFENDED_LIMIT = 1.1,
    SEND_VOLUNTEER_EVAL_BASE_DISTANCE = 100.0,
    SEND_VOLUNTEER_EVAL_CONTAINMENT_FACTOR = 0.15,
    DIPLOMACY_FACTION_GLOBAL_TENSION_FACTOR = 0.15,
    DIPLOMACY_FACTION_NEUTRALITY_PENALTY = 0.2,
    UPGRADE_DIVISION_RELUCTANCE = 14,
    FASCISTS_ALLY_FASCISTS = -10,
    FASCISTS_BEFRIEND_FASCISTS = 0,
    --MANPOWER_FREE_USAGE_THRESHOLD = 600000,			-- If AI has this much manpower he doesn't care about the percentage
    MANPOWER_RESERVED_THRESHOLD = 0.1,				-- The AI will not deploy more units if he goes below this percentage
    NEUTRAL_THREAT_PARANOIA = 1,
    --DIVISION_CREATE_MIN_XP = 50,
    --VARIANT_UPGRADE_MIN_XP = 10,
    HOUR_BAD_COMBAT_REEVALUATE = 42, --default 100
    PLAN_ACTIVATION_SUPERIORITY_AGGRO = 1.2, --default 1.0		-- How aggressive a country is in activating a plan based on how superiour their force is.
    AI_FRONT_MOVEMENT_FACTOR_FOR_READY = 0.1, --default 0.25
    PLAN_VALUE_TO_EXECUTE = -0.2, --default -0.5
    DEPLOY_MIN_TRAINING_WAR_FACTOR = 0.05,	--default 0.25	-- Required percentage of training (1.0 = 100%) for AI to deploy unit in wartime
    DEPLOY_MIN_EQUIPMENT_WAR_FACTOR = 0.80,	--default 90	-- Required percentage of equipment (1.0 = 100%) for AI to deploy unit in wartime
    MIN_PLAN_VALUE_TO_MICRO_INACTIVE = 0.1, --default 0.2				-- The AI will not consider members of groups which plan is not activated AND evaluates lower than this.
    MAX_UNITS_FACTOR_FRONT_ORDER = 3.0,	--default 1.5			-- Factor for max number of units to assign to area front orders
    DESIRED_UNITS_FACTOR_FRONT_ORDER = 3.0,	--default 1.5		-- Factor for desired number of units to assign to area front orders
    MIN_UNITS_FACTOR_FRONT_ORDER = 2.0,	--default 1.0			-- Factor for min number of units to assign to area front orders
    MAX_UNITS_FACTOR_INVASION_ORDER = 0.8,	--default 1.0	-- Factor for max number of units to assign to naval invasion orders
    DESIRED_UNITS_FACTOR_INVASION_ORDER = 0.8,	--default 1.0	-- Factor for desired number of units to assign to naval invasion orders
    MIN_UNITS_FACTOR_INVASION_ORDER = 0.8,	--default 1.0			-- Factor for min number of units to assign to naval invasion orders
	MAX_DIST_PORT_RUSH = 40.0,	--default 20.0			-- If a unit is in enemy territory with no supply it will consider nearby ports within this distance.
	MIN_FIELD_STRENGTH_TO_BUILD_UNITS = 0.6,	--default 0.7		-- Cancel unit production if below this to get resources out to units in the field
    MIN_MANPOWER_TO_BUILD_UNITS = 0.6,	--default 0.7				-- Cancel unit production if below this to get resources out to units in the field
    VP_LEVEL_IMPORTANCE_HIGH = 50,				-- Victory points with values higher than or equal to this are considered to be of high importance.
    VP_LEVEL_IMPORTANCE_MEDIUM = 25,			-- Victory points with values higher than or equal to this are considered to be of medium importance.
    VP_LEVEL_IMPORTANCE_LOW = 5,				-- Victory points with values higher than or equal to this are considered to be of low importance.
    FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.3,
    HEAVILY_FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.3,
    INVASION_DISTANCE_RANDOMNESS = 400,
    VARIANT_UPGRADE_MIN_XP = 1000,
},

NGraphics = {
    COUNTRY_FLAG_TEX_MAX_SIZE = 2048,
    COUNTRY_FLAG_SMALL_TEX_MAX_SIZE = 512,
    COUNTRY_FLAG_STRIPE_TEX_MAX_WIDTH = 10,
    COUNTRY_FLAG_STRIPE_TEX_MAX_HEIGHT = 8196,
    COUNTRY_FLAG_LARGE_STRIPE_MAX_WIDTH = 41,
    COUNTRY_FLAG_LARGE_STRIPE_MAX_HEIGHT = 24000,
    VICTORY_POINT_MAP_ICON_TEXT_CUTOFF = {200, 350, 600},  	-- Vanilla is 100, 250, 500
    VICTORY_POINTS_DISTANCE_CUTOFF = {300, 500, 1000}, 		-- Vanilla is 300, 500, 1500
},

NCountry = {
    SPECIAL_FORCES_CAP_BASE = 0.1,					-- Max ammount of special forces battalions is total number of non-special forces battalions multiplied by this and modified by a country modifier
    SPECIAL_FORCES_CAP_MIN = 32,					-- You can have a minimum of this many special forces battalions, regardless of the number of non-special forces battalions you have, this can also be modified by a country modifier
    MAJOR_MIN_FACTORIES = 25, --default 35,		-- need at least these many factories to become a major
    FEMALE_UNIT_LEADER_BASE_CHANCE = { -- modifiers female_random_operative_chance female_random_army_leader_chance female_random_admiral_chance
    -- applies as a factor to female unit leader randomization
    -- the values needs to be zero if you don't actually have random portraits
    1.0, -- navy leaders
    1.0, -- army leaders
    1.0, -- operatives
    },
    COUNTRY_LEADER_FEMALE_CHANCE = 1.0, -- chance for new country leaders to be female. should be set > 0 only if there are portraits/names for that country

},

NMilitary = {
    PLAN_EXECUTE_CAREFUL_MAX_FORT = 4,
},

NResistance = {
    GARRISON_MANPOWER_LOST_BY_ATTACK = 0.01, 	-- Ratio of manpower lost by garrison at each attack on garrison (this number will be reduced by the hardness of garrison template)
    GARRISON_EQUIPMENT_LOST_BY_ATTACK = 0.02, 	-- Ratio of equipment lost by garrison at each attack on garrison (this number will be reduced by the hardness of garrison template)
},

NOperatives = {
    AGENCY_CREATION_FACTORIES = 3,
    AGENCY_UPGRADE_PER_OPERATIVE_SLOT = 4,			-- Number of upgrade needed to unlock an additional operative slot
},

}

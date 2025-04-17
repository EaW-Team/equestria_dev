Code
[[

    static const float EAW_GB_CAM_MIN = 100.0f;
	static const float EAW_GB_CAM_MAX = 350.0f;
	static const float EAW_GB_CAM_MAX_FILLING_CLAMP = 0.8f; // 0 to 1 value for clamping the fill when camera is at max distance

	static const float EAW_BLACK_OUTLINE_CAM_MIN = 100.0f;
	static const float EAW_BLACK_OUTLINE_CAM_MAX = 400.0f;
	static const float EAW_BLACK_BORDER_MAX_CUTOFF = 0.995f;
	static const float EAW_BLACK_BORDER_CUTOFF_WIDTH = 0.025f;
    static const float3 EAW_BLACK_BORDER_COLOR = float3(0.0, 0.0, 0.0);

    static const float EAW_SHADOW_BORDER_CAM_MIN = 100.0f;
	static const float EAW_SHADOW_BORDER_CAM_MAX = 400.0f;
    static const float EAW_MAP_BORDER_SHADOW_STRENGTH = 0.10f;
    static const float EAW_MAP_BORDER_SHADOW_MAX_CUTOFF = EAW_BLACK_BORDER_MAX_CUTOFF;
    static const float EAW_MAP_BORDER_SHADOW_WIDTH_SOLID = EAW_MAP_BORDER_SHADOW_MAX_CUTOFF - 0.0300f;
    static const float EAW_MAP_BORDER_SHADOW_WIDTH_GRADIENT = EAW_MAP_BORDER_SHADOW_WIDTH_SOLID - 0.010f;
    static const float EAW_MAP_BORDER_SHADOW_STRENGTH_SMOOTH = 0.30f;
    static const float EAW_MAP_BORDER_SHADOW_WIDTH_SOLID_SMOOTH =  0.03f;
    static const float EAW_MAP_BORDER_SHADOW_WIDTH_GRADIENT_SMOOTH = 0.050f;
    static const float EAW_MAP_BORDER_SHADOW_WIDTH_SOLID_STATIC = 0.99f;
    static const float EAW_MAP_BORDER_SHADOW_WIDTH_GRADIENT_STATIC = EAW_MAP_BORDER_SHADOW_WIDTH_SOLID_STATIC - 0.05f;
]]
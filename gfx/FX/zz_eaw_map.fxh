ConstantBuffer( 0, 0 )
{
	float4x4	ViewProjectionMatrix;
	float4x4	InvViewProjMatrix;
	float4 		vGBCamDistOverride_GBOutlineCutoff;
	float4 		vVirtualSunPos;
	float4		vVirtualMoonPos;
	float4 		vSecondVirtualSunPos;
	float4		vSecondVirtualMoonPos;
	float3 		vCamPos;
	float 		HdrRange;
	float3 		vCamLookAtDir;
	float 		vGlobalTime;
	float4		vFoWOpacity_FoWTime_SnowMudFade_MaxGameSpeed;
	float4		DayNight_Hour_SunDir;

	float3		AmbientPosX;
	float		ShadowFadeFactor;
	float3		AmbientNegX;
	float		FOWFadeFactor;
	float3		AmbientPosY;
	float		MinMeshAlpha;
	float3		AmbientNegY;
	float		NegFogMultiplier;
	float3		AmbientPosZ;
	float3		AmbientNegZ;
	float		CubemapIntensity;
	float4		SunDiffuseIntensity;
	float4		MoonDiffuseIntensity;
	float		GB_TextureHeight;
	float		SunSpecularIntensity;
};

Code
[[
	float cam_distance(float, float);
	float3 Levels( float3 vInColor, float vMinInput, float vMaxInput );
	float Levels( float vInValue, float vMinValue, float vMaxValue );
	float4 gradient_border_multisample_alpha( in float4 vCh, in sampler2D TexCh, in float2 vUV );
	float gradient_border_distance_to_alpha( float vDist, float vCamDist );

	float eaw_gradient_border_camera_distance() {
		return 1.0f - clamp(cam_distance( EAW_GB_CAM_MIN, EAW_GB_CAM_MAX ), 0, EAW_GB_CAM_MAX_FILLING_CLAMP);
	}

	float eaw_black_outline_camera_distance() {
		return clamp(cam_distance( EAW_BLACK_OUTLINE_CAM_MIN, EAW_BLACK_OUTLINE_CAM_MAX ), 0, 1);
	}

	float eaw_shadow_border_distance() {
		return clamp(cam_distance( EAW_SHADOW_BORDER_CAM_MIN, EAW_SHADOW_BORDER_CAM_MAX ), 0, 1);
	}

	float eaw_gradient_border_process_channel( out float3 vCh, float3 vInit, float vCamDist, float2 uv, float4 vGBDist, float FX, float vOutlineMult, float vOutlineCutoff, float vStrength, float override)
	{
		vCh = vInit;

		const float PulseSpeedMult = 3.5f;
		vStrength *= lerp( lerp( 0.45f, 1.0f, 1.0f - FX ), 1.0f, ( sin( vGlobalTime * PulseSpeedMult ) + 1.0f ) / 2 );

		float Alpha = vGBDist.a;
		//Alpha = 1;

		vOutlineCutoff = EAW_BLACK_BORDER_MAX_CUTOFF;

		// Check how much color and how much outline there is
		float vColorOpacity = Levels( Alpha, 0.0f, vOutlineCutoff );
		float vOutline = 1.0f - Levels( Alpha, vOutlineCutoff, 1.0f );
		float vOldOutline = vOutline;
		vOutline *= floor(vColorOpacity);
		vOutline *= vOutlineMult;

		//vCamDist = 0;


		// Convert "heightmap" to "fill" regarding camera distance (the whole magic in this function)
		vColorOpacity = gradient_border_distance_to_alpha( vColorOpacity, vCamDist );
		//vCh = float3(vColorOpacity, vColorOpacity, vColorOpacity);
		//return 0.0;

		// Now when vOutline > 0 then vColorOpacity = 0, and other way around.
		// Never both values will be > 0.
		vColorOpacity *= floor(vOldOutline);

		float borderShadow = 1.0f - eaw_shadow_border_distance();

		float low_threshold = (EAW_MAP_BORDER_SHADOW_WIDTH_GRADIENT - EAW_MAP_BORDER_SHADOW_WIDTH_GRADIENT_SMOOTH*borderShadow)*floor(1.0 - override) +
		                        EAW_MAP_BORDER_SHADOW_WIDTH_GRADIENT_STATIC*ceil(override);
		float high_threshold = (EAW_MAP_BORDER_SHADOW_WIDTH_SOLID + EAW_MAP_BORDER_SHADOW_WIDTH_SOLID_SMOOTH*borderShadow)*floor(1.0 - override) +
		                        EAW_MAP_BORDER_SHADOW_WIDTH_SOLID_STATIC*ceil(override);

		float vThick = Levels( Alpha, low_threshold, high_threshold);

		float vMaxGradient = 0.3;//max( vColorOpacity, vOutline );
		//vCh = lerp( vCh, vCh*0.5, vThick);
		//return 1;

		vCh = lerp( vCh, vGBDist.rgb, vMaxGradient * vStrength);
		//vCh = lerp( vCh, vGBDist.rgb, 0.7);

		// Compensate the brightness since the 2nd layer is now black (not white) although it's alpha is 0
		//vCh *= 1.15f;
		vCh = min( vCh, float3( 1, 1, 1 ) );

		// Make the outline edge darker
		vCh = lerp( vCh, vCh*lerp(EAW_MAP_BORDER_SHADOW_STRENGTH, EAW_MAP_BORDER_SHADOW_STRENGTH_SMOOTH, borderShadow), vThick );

		float val = vOutline;
		//vCh = float3(val, val, val);
		//return 1.0;

		return 0;
		return max( vMaxGradient, vThick );
	}

	float eaw_apply_black_border(out float3 vCh,
									 float3 vInit,
									 float2 uv,
									 float Alpha,
									 float FX,
									 float en,
									 float vOutlineMult,
									 float vStrength) {

		vCh = vInit;

		const float PulseSpeedMult = 3.5f;
		vStrength *= lerp( lerp( 0.7f, 1.0f, 1.0f - FX ), 1.0f, ( sin( vGlobalTime * PulseSpeedMult ) + 1.0f ) / 2 );

		float vOutlineCutoff = EAW_BLACK_BORDER_MAX_CUTOFF - EAW_BLACK_BORDER_CUTOFF_WIDTH*eaw_black_outline_camera_distance();

		float in_mask = floor(Levels(Alpha, 0.0f, vOutlineCutoff));
		float out_mask = ceil(Levels(Alpha, EAW_BLACK_BORDER_MAX_CUTOFF, 1));
		float gradient = ceil((1.0 - Levels( Alpha, vOutlineCutoff, 1.0f ))*(in_mask - out_mask))*vStrength*eaw_black_outline_camera_distance()*(1.0 - ceil(en));

		vCh = lerp( vCh, EAW_BLACK_BORDER_COLOR, gradient);

		// Debug, to see the mask
		//float val = gradient;
		//vCh = float3(val, val, val);

		return gradient;
	}

	void eaw_gradient_border_apply( inout float3 vColor, float3 vNormal, float2 vUV,
		in sampler2D TexCh1, in sampler2D TexCh2,
		float vOutlineMult, float2 vOutlineCutoff, float2 vCamDistOverride, inout float vBloomAlpha, float water)
	{

	#ifndef GRADIENT_BORDERS
		vBloomAlpha = 1.0f;
		return;
	#endif

		//if (water > 0) {
		//	vBloomAlpha = 1.0f;
		//	return;
		//}

		// Check the distance of camera (value 0-1)
		float vGBCamDist = eaw_gradient_border_camera_distance();
		//vColor =  float3(0, 0, vOutlineCutoff.y);

		// Handle camera distance overriding (unique for each channel)
		float vGBCamDistCh1 = saturate( ( vGBCamDist * int( 1.0f - vCamDistOverride.x ) ) + vCamDistOverride.x );
		float vGBCamDistCh2 = saturate( ( vGBCamDist * int( 1.0f - vCamDistOverride.y ) ) + vCamDistOverride.y );
		//vColor = float3(vCamDistOverride.x, vCamDistOverride.x, vCamDistOverride.x);
		//return;

		// Split UV to correct offset in height, as 1st channel is the top half part of the texture, and 2nd channel is bottom half
		float HalfPix = 0.5f / GB_TextureHeight;
		vUV.y *= 0.5f - HalfPix;
		float2 vUV2 = float2( vUV.x, vUV.y + 0.5f );

		// Calculate color and transparency of both channels
		float3 vGradMix;
		float4 FX1 = tex2D(TexCh2, vUV);
		float4 FX2 = tex2D(TexCh2, vUV2);
		float4 text_color1 = gradient_border_multisample_alpha(tex2D(TexCh1, vUV),  TexCh1, vUV);
		float4 text_color2 = gradient_border_multisample_alpha(tex2D(TexCh1, vUV2), TexCh1, vUV2);

		float vAlpha1 = eaw_gradient_border_process_channel( vGradMix, vColor, vGBCamDistCh1, vUV, text_color1, FX1.b, vOutlineMult, vOutlineCutoff.x, GB_STRENGTH_CH1, water);
		// Now mix, the resultat with background
		float TranspA = 1.0f - FX1.g;
		vColor = vGradMix;
		//vColor = lerp( vColor, vGradMix, ( GB_OPACITY_NEAR + ( 1.0f - vGBCamDist ) * ( GB_OPACITY_FAR - GB_OPACITY_NEAR ) ) * TranspA );

		float vAlpha2 = eaw_gradient_border_process_channel( vGradMix, vColor, vGBCamDistCh2, vUV2, text_color2, FX2.b, vOutlineMult, vOutlineCutoff.y, (1.0 - vAlpha1 * GB_STRENGTH_CH1 * GB_FIRST_LAYER_PRIORITY) * GB_STRENGTH_CH2, water);
		float TranspB = 1.0f - FX2.g;
		//vColor = vGradMix;
		//vColor = lerp( vColor, vGradMix, ( GB_OPACITY_NEAR + ( 1.0f - vGBCamDist ) * ( GB_OPACITY_FAR - GB_OPACITY_NEAR ) ) * TranspB );

		float vAlpha3 = eaw_apply_black_border(vGradMix,
									vColor,
									vUV,
									text_color1.a,
									FX1.b,
									FX1.g,
									vOutlineMult,
									1.0);
		vColor = lerp(vGradMix, vColor, water);

		float val = FX1.g;
		//vColor = float3(val, val, val);
		//vColor = text_color2.rgb;

		//vColor = vGradMix;
		//return;
	//vColor = GetOverlay( vColor, ToLinear(vGradMix), 0.80);

		// Return some alpha, so the postprocess will ignore gradient borders
		// when applying season coloring overlay
		// (we don't want to affect the colors especially when camera is zoomed out, and
		//  everything is 100% filled)
		vBloomAlpha = 1.0f - max(max( vAlpha1, vAlpha2), vAlpha3);
		//vBloomAlpha = 0;
	}

]]
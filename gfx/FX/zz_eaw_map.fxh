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

	static const float EAW_GB_CAM_MIN = 100.0f;
	static const float EAW_GB_CAM_MAX = 350.0f;
	static const float EAW_GB_CAM_MAX_FILLING_CLAMP = 0.8f; // 0 to 1 value for clamping the fill when camera is at max distance
	float eaw_gradient_border_camera_distance() {
		return 1.0f - clamp( cam_distance( EAW_GB_CAM_MIN, EAW_GB_CAM_MAX ), 0, EAW_GB_CAM_MAX_FILLING_CLAMP );
	}

	float eaw_gradient_border_process_channel( out float3 vCh, float3 vInit, float vCamDist, float2 uv, in sampler2D gbTex, in sampler2D gbTex2, float vOutlineMult, float vOutlineCutoff, float vStrength )
	{
		vCh = vInit;

		const float PulseSpeedMult = 3.5f;
		float FX = tex2D( gbTex2, uv ).b;
		vStrength *= lerp( lerp( 0.45f, 1.0f, 1.0f - FX ), 1.0f, ( sin( vGlobalTime * PulseSpeedMult ) + 1.0f ) / 2 );

		float vFullWidth = (2.5f + 4*smoothstep(0.0f, 1.0f, 1f - vCamDist))/ 255.0f;//lerp( 5.25f, 0.01f, FX ) / 255.f;
		float vGradientWidth = 10f / 255.0f;//lerp( 0.5f, 0.1f, FX ) / 255.f;

		// Grab multisampled border color
		float4 vGBDist = gradient_border_multisample_alpha( tex2D( gbTex, uv ), gbTex, uv );

		float Alpha = vGBDist.a;
		//Alpha = 1;

		// Check how much color and how much outline there is
		float vColorOpacity = Levels( Alpha, 0.0f, vOutlineCutoff );
		float vOutline = 1.0f - Levels( Alpha, vOutlineCutoff, 1.0f );
		float vOldOutline = vOutline;
		vOutline *= floor(vColorOpacity);
		vOutline *= vOutlineMult;

		//vCh = float3(vCamDistOverride.y, vCamDistOverride.y, vCamDistOverride.y);
		//return 0.0;

		// Convert "heightmap" to "fill" regarding camera distance (the whole magic in this function)
		vColorOpacity = gradient_border_distance_to_alpha( vColorOpacity, vCamDist );

		// Now when vOutline > 0 then vColorOpacity = 0, and other way around.
		// Never both values will be > 0.
		vColorOpacity *= floor(vOldOutline);



		float vThick = smoothstep( 0.f, 1.f, Levels( Alpha, vOutlineCutoff - vFullWidth, vOutlineCutoff - vFullWidth + vGradientWidth ) ) ;
		vThick = ceil(Levels( Alpha, vOutlineCutoff - vFullWidth, vOutlineCutoff - vFullWidth + vGradientWidth ));

		vThick *= floor(vOldOutline);

		float vMaxGradient = max( vColorOpacity, vOutline );
		//vCh = lerp( vCh, vCh*0.5, vThick);
		//return 1;

		vCh = lerp( vCh, vGBDist.rgb, vMaxGradient * vStrength);

		// Compensate the brightness since the 2nd layer is now black (not white) although it's alpha is 0
		vCh *= 1.15f;
		vCh = min( vCh, float3( 1, 1, 1 ) );

		// Make the outline edge darker
		//vCh = lerp( vCh, vCh * .5, vThick );

		return max( vMaxGradient, vThick );
	}

	float eaw_apply_black_border(out float3 vCh,
									 float3 vInit,
									 float vCamDist,
									 float2 uv,
									 float Alpha,
									 float FX,
									 float vOutlineMult,
									 float vOutlineCutoff,
									 float vStrength) {

		vCh = vInit;

		const float PulseSpeedMult = 3.5f;
		vStrength *= lerp( lerp( 0.7f, 1.0f, 1.0f - FX ), 1.0f, ( sin( vGlobalTime * PulseSpeedMult ) + 1.0f ) / 2 );

		//Alpha = 1;

		vOutlineCutoff = 0.968;

		// Check how much color and how much outline there is
		float vColorOpacity = Levels( Alpha, 0.0f, vOutlineCutoff );
		float vOutline = 1.0f - Levels( Alpha, vOutlineCutoff, 1.0f );
		float vOldOutline = vOutline;
		vOutline *= ceil(floor(vColorOpacity));
		vOutline *= vOutlineMult;

		vColorOpacity = vOutline*vStrength;

		vCh = lerp( vCh, float3(0, 0, 0), vColorOpacity);
		//vCh = float3(vColorOpacity, vColorOpacity, vColorOpacity);

		return vColorOpacity;
	}

	void eaw_gradient_border_apply( inout float3 vColor, float3 vNormal, float2 vUV,
		in sampler2D TexCh1, in sampler2D TexCh2,
		float vOutlineMult, float2 vOutlineCutoff, float2 vCamDistOverride, inout float vBloomAlpha )
	{

	#ifndef GRADIENT_BORDERS
		vBloomAlpha = 1.0f;
		return;
	#endif


		// Check the distance of camera (value 0-1)
		float vGBCamDist = eaw_gradient_border_camera_distance();
		//vColor =  float3(0, 0, vOutlineCutoff.y);

		// Handle camera distance overriding (unique for each channel)
		float vGBCamDistCh1 = saturate( ( vGBCamDist * int( 1.0f - vCamDistOverride.x ) ) + vCamDistOverride.x );
		float vGBCamDistCh2 = saturate( ( vGBCamDist * int( 1.0f - vCamDistOverride.y ) ) + vCamDistOverride.y );
		//vColor = float3(vCamDistOverride.y, vCamDistOverride.y, vCamDistOverride.y);
		//return;

		// Split UV to correct offset in height, as 1st channel is the top half part of the texture, and 2nd channel is bottom half
		float HalfPix = 0.5f / GB_TextureHeight;
		vUV.y *= 0.5f - HalfPix;
		float2 vUV2 = float2( vUV.x, vUV.y + 0.5f );

		// Calculate color and transparency of both channels
		float3 vGradMix;

		float vAlpha1 = eaw_gradient_border_process_channel( vGradMix, vColor, vGBCamDistCh1, vUV, TexCh1, TexCh2, vOutlineMult, vOutlineCutoff.x, GB_STRENGTH_CH1 );
		// Now mix, the resultat with background
		float TranspA = 1.0f - tex2D( TexCh2, vUV ).g;
		vColor = lerp( vColor, vGradMix, ( GB_OPACITY_NEAR + ( 1.0f - vGBCamDist ) * ( GB_OPACITY_FAR - GB_OPACITY_NEAR ) ) * TranspA );

		float vAlpha2 = eaw_gradient_border_process_channel( vGradMix, vColor, vGBCamDistCh2, vUV2, TexCh1, TexCh2, vOutlineMult, vOutlineCutoff.y, (1.0 - vAlpha1 * GB_STRENGTH_CH1 * GB_FIRST_LAYER_PRIORITY) * GB_STRENGTH_CH2 );
		float TranspB = 1.0f - tex2D( TexCh2, vUV2 ).g;
		vColor = vGradMix;
		vColor = lerp( vColor, vGradMix, ( GB_OPACITY_NEAR + ( 1.0f - vGBCamDist ) * ( GB_OPACITY_FAR - GB_OPACITY_NEAR ) ) * TranspB );

		float FX = tex2D(TexCh2, vUV).b;
		float Alpha = gradient_border_multisample_alpha( tex2D( TexCh1, vUV ), TexCh1, vUV).a;

		float vAlpha3 = eaw_apply_black_border(vGradMix,
									vColor,
									vGBCamDist,
									vUV,
									Alpha,
									FX,
									vOutlineMult,
									vOutlineCutoff.x,
									1.0);
		vColor = vGradMix;

		//vColor = vGradMix;
		//return;
	//vColor = GetOverlay( vColor, ToLinear(vGradMix), 0.80);

		// Return some alpha, so the postprocess will ignore gradient borders
		// when applying season coloring overlay
		// (we don't want to affect the colors especially when camera is zoomed out, and
		//  everything is 100% filled)
		vBloomAlpha = 1.0f - max(max( vAlpha1, vAlpha2), vAlpha3);
	}

]]
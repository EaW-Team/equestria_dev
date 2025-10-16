Includes = {
	"constants.fxh"
	"standardfuncsgfx.fxh"
}
PixelShader = 
{
	Code
	[[
	
	//Untility function to check if day/night overrides need to be applied
	int dayNightOverrideCheck(in sampler2D gbChannel) {
		
		//Sample the hidden province
		float HalfPix = 0.5f / GB_TextureHeight;
		float3 colorTest = tex2D( gbChannel, float2(0.10327f,1.0f*(0.5f - HalfPix)));
		
		//Day override
		if ( 0.0004f < colorTest.x ) {
			return 2;
		}
		
		//Night override
		if ( 0.0f < colorTest.x ) {
			return 1;
		}
		
		//No override
		return 0;
	}
	
	//Overloaded functions from standardfuncsgfx.fxh
	float DayNightFactor( float3 vGlobeNormal, float vMin, float vMax, int dayNightStatus ) //EaW overload
	{
		if (dayNightStatus == 1) {
			return saturate( 1.0f );
		}
		else if (dayNightStatus == 2) {
			return saturate( 0.0f );
		}
		else {
			float vDot = dot( vGlobeNormal, DayNight_Hour_SunDir.yzw );
			return saturate( ( vDot - vMin ) / ( vMax - vMin ) ) * vFoWOpacity_FoWTime_SnowMudFade_MaxGameSpeed.w;
		}
	}
	
	float DayNightFactor( float3 vGlobeNormal, int dayNightStatus ) //EaW overload
	{
		return DayNightFactor( vGlobeNormal, FEATHER_MIN, FEATHER_MAX, dayNightStatus );
	}
	
	float3 DayNightWithBlend( float3 vDayColor, float3 vGlobeNormal, float vBlend, int dayNightStatus ) //EaW overload
	{
		#ifdef NO_NIGHT
		return vDayColor;
		#endif

		//return vec3( DayNightFactor( vGlobeNormal ) );

	    // lerp between day and night
		return lerp( vDayColor, NightifyColor(vDayColor, vBlend), DayNightFactor( vGlobeNormal, dayNightStatus ) * NIGHT_OPACITY );
	}
	
	float3 DayNight( float3 vDayColor, float3 vGlobeNormal, int dayNightStatus ) //EaW overload
	{
		return DayNightWithBlend(vDayColor, vGlobeNormal, 1.0f, dayNightStatus);
	}
	
	float3 DayNightCityMask( float3 vDayColor, float3 vGlobeNormal, float vCityLightMask, float vFogFactor, int dayNightStatus ) //EaW overload
	{
		#ifdef NO_NIGHT
		return vDayColor;
		#endif

		float vNightFactor = DayNightFactor( vGlobeNormal, dayNightStatus );

	    // lerp between day and night
		float3 Result = lerp( vDayColor, NightifyColor(vDayColor , 0.0f), vNightFactor * NIGHT_OPACITY );

		Result += vCityLightMask * float3(2.0f, 2.0f, 0.3f) * vNightFactor * (1.0f - vFogFactor * vFogFactor);

		return Result;
	}
	
	float3 CalculateSunDirection( float3 vWorldPos, float3 SunPos, float3 SecondSunPos, float3 MoonPos, float3 SecondMoonPos, int dayNightStatus )// EaW overload
	{
		float vSelected = DayNightFactor( CalcGlobeNormal( vWorldPos.xz ), 0.0f, 0.0001f, dayNightStatus );
		float3 vSourcePos = lerp( SunPos, MoonPos, vSelected );
		float3 vSecondSourcePos = lerp( SecondSunPos, SecondMoonPos, vSelected );

		if ( vWorldPos.x - vSourcePos.x > MAP_SIZE_X * 0.5 )
		{
			vSourcePos.x += MAP_SIZE_X;
		}
		else if ( vWorldPos.x - vSourcePos.x < -MAP_SIZE_X * 0.5 )
		{
			vSourcePos.x -= MAP_SIZE_X;
		}

		if ( vWorldPos.x - vSecondSourcePos.x > MAP_SIZE_X * 0.5 )
		{
			vSecondSourcePos.x += MAP_SIZE_X;
		}
		else if ( vWorldPos.x - vSecondSourcePos.x < -MAP_SIZE_X * 0.5 )
		{
			vSecondSourcePos.x -= MAP_SIZE_X;
		}

		float lerpFactor = abs( vWorldPos.x - vSourcePos.x ) / (MAP_SIZE_X * 0.5);
		lerpFactor = smoothstep(0.5, 1.0, lerpFactor);
		vSourcePos = lerp( vSourcePos, vSecondSourcePos, lerpFactor );

		return normalize( vWorldPos - vSourcePos );
	}
	
	float3 CalculateSunDirection( float3 vWorldPos, int dayNightStatus ) // EaW overload
	{
		return CalculateSunDirection( vWorldPos, vVirtualSunPos.xyz, vSecondVirtualSunPos.xyz, vVirtualMoonPos.xyz, vSecondVirtualMoonPos.xyz, dayNightStatus );
	}
	
	float3 CalculateSunDirectionWater( float3 vWorldPos, int dayNightStatus ) // EaW overload
	{
		return CalculateSunDirection( vWorldPos, vVirtualSunPos.xwz, vSecondVirtualSunPos.xwz, vVirtualMoonPos.xwz, vSecondVirtualMoonPos.xwz, dayNightStatus );
	}
	
	void CalculateSunLight(LightingProperties aProperties, float aShadowTerm, float3 vLightSourceDirection, out float3 aDiffuseLightOut, out float3 aSpecularLightOut, int dayNightStatus )// EaW overload
	{
		float vDayFactor = 1.0f - DayNightFactor( CalcGlobeNormal( aProperties._WorldSpacePos.xz ), dayNightStatus );
		float vNightFactor = DayNightFactor( CalcGlobeNormal( aProperties._WorldSpacePos.xz ), MOON_FEATHER_MIN, MOON_FEATHER_MAX, dayNightStatus );

		aShadowTerm = aShadowTerm * saturate( vDayFactor + vNightFactor );

		float3 sunIntensity =
			SunDiffuseIntensity.rgb * SunDiffuseIntensity.a * aShadowTerm * vDayFactor
			+ MoonDiffuseIntensity.rgb * MoonDiffuseIntensity.a * aShadowTerm * vNightFactor;
		//sunIntensity += 0.6f * (1.0f - (vDayFactor  * aShadowTerm + vNightFactor));


	#ifdef PDX_IMPROVED_BLINN_PHONG
		ImprovedBlinnPhong(sunIntensity, -vLightSourceDirection, aProperties, aDiffuseLightOut, aSpecularLightOut);
	#else
		aDiffuseLightOut = CalculateLight(aProperties._Normal, vLightSourceDirection, sunIntensity);
		aSpecularLightOut = CalculatePBRSpecularPower(aProperties._WorldSpacePos, aProperties._Normal, aProperties._SpecularColor, aProperties._Glossiness, sunIntensity, vLightSourceDirection);
	#endif
		aSpecularLightOut *= SunSpecularIntensity;
	}
	
	void CalculateSunLight(LightingProperties aProperties, float aShadowTerm, out float3 aDiffuseLightOut, out float3 aSpecularLightOut, int dayNightStatus ) //EaW overload
	{
		float3 vLightSourceDirection = CalculateSunDirection( aProperties._WorldSpacePos, dayNightStatus );
		CalculateSunLight(aProperties, aShadowTerm, vLightSourceDirection, aDiffuseLightOut, aSpecularLightOut, dayNightStatus );
	}
	
	float3 ComposeLight(LightingProperties aProperties, float3 aDiffuseLight, float3 aSpecularLight, int dayNightStatus ) //EaW overload
	{
		float vDayNight = DayNightFactor( CalcGlobeNormal( aProperties._WorldSpacePos.xz ), dayNightStatus );

		float3 vAmbientColor = AmbientLight(aProperties._Normal, vDayNight);
		float3 diffuse = ((vAmbientColor + aDiffuseLight) * aProperties._Diffuse) * HdrRange;
		float3 specular = aSpecularLight;

		return diffuse + specular;
	}
	
	float3 ComposeLightSnow(LightingProperties aProperties, float3 aDiffuseLight, float3 aSpecularLight, float vSnowFactor, int dayNightStatus ) //EaW overload
	{
		float vDayNight = DayNightFactor( CalcGlobeNormal( aProperties._WorldSpacePos.xz ), dayNightStatus );
		float3 vAmbientColor = AmbientLight(aProperties._Normal, vDayNight);
	#ifdef LOW_END_GFX
		return (((vAmbientColor + aDiffuseLight) * aProperties._Diffuse) * HdrRange) + aSpecularLight;
	#else
		float3 SnowAmbient = CalcSnowAmbient(aDiffuseLight, vSnowFactor);
		return (((SnowAmbient + vAmbientColor + aDiffuseLight) * aProperties._Diffuse) * HdrRange) + aSpecularLight;
	#endif
	}
	
	float3 ComposeLightMesh(LightingProperties aProperties, float3 aDiffuseLight, float3 aSpecularLight, float vSnowFactor, int dayNightStatus ) // EaW overload
	{
		float vDayNight = DayNightFactor( CalcGlobeNormal( aProperties._WorldSpacePos.xz ), dayNightStatus );

		float3 DayAmbientColors[6];
		DayAmbientColors[0] = AmbientPosX;
		DayAmbientColors[1] = AmbientNegX;
		DayAmbientColors[2] = AmbientPosY;
		DayAmbientColors[3] = AmbientNegY;
		DayAmbientColors[4] = AmbientPosZ;
		DayAmbientColors[5] = AmbientNegZ;

		float3 NightAmbientColors[6];
		NightAmbientColors[0] = NightAmbientPosX;
		NightAmbientColors[1] = NightAmbientNegX;
		NightAmbientColors[2] = NightAmbientPosY;
		NightAmbientColors[3] = NightAmbientNegY;
		NightAmbientColors[4] = NightAmbientPosZ;
		NightAmbientColors[5] = NightAmbientNegZ;

		float3 vAmbientColor = AmbientLight(aProperties._Normal, vDayNight, DayAmbientColors, NightAmbientColors);
		float3 SnowAmbient = CalcSnowAmbient(aDiffuseLight, vSnowFactor);
		float3 diffuse = ((SnowAmbient + vAmbientColor + aDiffuseLight) * aProperties._Diffuse) * HdrRange;
		float3 specular = aSpecularLight;

		return diffuse + specular;
	}
	
	]]
}
Includes = {
	"constants.fxh"
	"standardfuncsgfx.fxh"
	"shadow.fxh"
	"tiled_pointlights.fxh"
	"fow.fxh"
	"zzz_eaw_functions.fxh"
}

PixelShader =
{
	Samplers =
	{
		RailTexture =
		{
			Index = 0
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		Diffuse =
		{
			Index = 1
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Clamp"
		}
		
		NormalMap =
		{
			Index = 2
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Clamp"
		}
		RiverData =
		{
			Index = 3
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Clamp"
			AddressV = "Clamp"
		}
		LeanTexture1 =
		{
			Index = 4
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		LeanTexture2 =
		{
			Index = 5
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		ProvinceSecondaryColorMap =
		{
			Index = 6
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		HeightNormal =
		{
			Index = 7
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		SnowMudTexture =
		{
			Index = 8
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		CityLightsAndSnowNoise =
		{
			Index = 9
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		LightIndexMap =
		{
			Index = 10
			MagFilter = "Point"
			MinFilter = "Point"
			MipFilter = "Point"
			AddressU = "Clamp"
			AddressV = "Clamp"
		}
		LightDataMap =
		{
			Index = 11
			MagFilter = "Point"
			MinFilter = "Point"
			MipFilter = "Point"
			AddressU = "Clamp"
			AddressV = "Clamp"
		}
		GradientBorderChannel1 =
		{
			Index = 12
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Clamp"
			AddressV = "Clamp"
		}
		GradientBorderChannel2 =
		{
			Index = 13
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Clamp"
			AddressV = "Clamp"
		}
		ReflectionCubeMap =
		{
			Index = 14
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Clamp"
			AddressV = "Clamp"
			Type = "Cube"
		}
		ShadowMap =
		{
			Index = 15
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "Linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
			Type = "Shadow"
		}
	}
}


VertexStruct VS_INPUT
{
	float4 vPosition   : POSITION;
	float2 vUV : TEXCOORD0;
};

VertexStruct VS_OUTPUT
{
	float4 vPosition		: PDX_POSITION;
	float2 vUV				: TEXCOORD0;
	float4 vScreenCoord		: TEXCOORD1;
	float4 vPos_Height	    : TEXCOORD2;
};


ConstantBuffer( 1, 32 )
{
	float4x4 ShadowMapTextureMatrix;
	float vTimeGlobal;
	float vRailwayAlpha;
};


VertexShader =
{
	MainCode VertexShader
	[[
		VS_OUTPUT main( const VS_INPUT v )
		{
			VS_OUTPUT Out;
		
			Out.vPos_Height.xyz = v.vPosition.xyz;
			Out.vPos_Height.w = v.vPosition.y;
			Out.vPosition = mul( ViewProjectionMatrix, v.vPosition );
			
			Out.vUV = v.vUV;
			
			// scale railway width
			// disabled for now. doesn't look good anyway
			// Out.vUV.y = lerp( Out.vUV.y < 0.5 ? -4 : 5, Out.vUV.y, vRailwayAlpha );
			
			// Output the screen-space texture coordinates
			Out.vScreenCoord.x = ( Out.vPosition.x * 0.5 + Out.vPosition.w * 0.5 );
			Out.vScreenCoord.y = ( Out.vPosition.w * 0.5 - Out.vPosition.y * 0.5 );
		#ifdef PDX_OPENGL
			Out.vScreenCoord.y = -Out.vScreenCoord.y;
		#endif			
			Out.vScreenCoord.z = Out.vPosition.w;
			Out.vScreenCoord.w = Out.vPosition.w;

			return Out;
		}
		
	]]
}

PixelShader =
{
	MainCode PixelShader
	[[
		float3 ApplySnowMesh( float3 vColor, float3 vPos, inout float3 vNormal, float4 vFoWColor, out float vSnowAlpha, in float alpha )
		{
			float vIsSnow = GetSnow( vFoWColor, alpha ) * 0.25f;
			float vSnowFade = saturate( saturate( vNormal.y - saturate( 1.0f - vIsSnow ) )*vIsSnow*5.5f*saturate( ( vNormal.y - 0.5f ) * 1000.0f ) );
						
			float vOpacity = cam_distance( SNOW_CAM_MIN, SNOW_CAM_MAX );
			vOpacity = SNOW_OPACITY_MIN + vOpacity * ( SNOW_OPACITY_MAX - SNOW_OPACITY_MIN );
			
			vColor = lerp( vColor, SNOW_COLOR, vSnowFade * vOpacity );
			vSnowAlpha = saturate( vIsSnow * 1.5f ) * vOpacity;
						
			return vColor;
		}

		float4 main( VS_OUTPUT Input ) : PDX_COLOR
		{
			if ( Input.vUV.y < 0.0 || Input.vUV.y >= 1.0 ) discard;
			
			float4 Color = tex2D( RailTexture, Input.vUV );
			float3 vPos = Input.vPos_Height.xyz;
			
			float2 map_uv = float2( ( ( vPos.x+0.5f ) / MAP_SIZE_X ), ( ( vPos.z+0.5f-MAP_SIZE_Y ) / -MAP_SIZE_Y ));

			float3 vNormal = float3(0,1,0);
			float vSnowAlpha = 0;
			#ifdef PDX_SNOW
				float4 vFoWColor = GetMudSnowColor( vPos, SnowMudTexture );
				Color.rgb = ApplySnowMesh( Color.rgb, vPos, vNormal, vFoWColor, vSnowAlpha, tex2D( ProvinceSecondaryColorMap, map_uv ).a );	
			#endif

			#ifdef PDX_GRADIENT_BORDERS
				// Gradient Borders
				float vBloomAlpha = 0.0f;
				gradient_border_apply( Color.rgb, vNormal, map_uv, GradientBorderChannel1, GradientBorderChannel2, 1.0f, vGBCamDistOverride_GBOutlineCutoff.zw, vGBCamDistOverride_GBOutlineCutoff.xy, vBloomAlpha );

				// Secondary color mask
				//secondary_color_mask( Color.rgb, vNormal, map_uv, ProvinceSecondaryColorMap, vBloomAlpha );	
			#endif

			Color.a *= vRailwayAlpha;
			
			
			float3 FOWColor = ApplyFOW( Color.rgb, ShadowMap, Input.vScreenCoord );
			Color.rgb = FOWColor;
			
			return Color;
		}
	]]
}


BlendState BlendState
{
	BlendEnable = yes
	AlphaTest = no
	SourceBlend = "src_alpha"
	DestBlend = "inv_src_alpha"
	WriteMask = "RED|GREEN|BLUE"
}


DepthStencilState DepthStencilState
{
	DepthEnable = no
	StencilEnable = no
}

Effect railroad
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShader"
	Defines = { "PDX_SNOW" "PDX_GRADIENT_BORDERS" }
}

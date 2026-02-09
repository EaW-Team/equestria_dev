# ##########
# EaW Team #
# ##########
# Description
# This shader is used in the underground SGUI for HYE
# Its main purpose is to animate the node used in the underground map
# It features : - Parametrable delay before the animation (Same time base as the links)
# 			    - One dynamic transitional animation
# ##########
# Input : delay  - The animation delay, 7bits unsigned (Range [0, 118])
# Input format :
#                Fields |  delay |
#                  Bits |  7 | 0 |
# Up       : Up state, as other button. No animation, and first frame displayed
# Disabled : Delay the animation, and then dsipaly successively the frames until it reach the last
# Over : Apply a light qudaratic animated mask
# Down : Apply a dark linear animated mask
# ##########

Includes = {
	"buttonstate.fxh"
}

PixelShader =
{
	Samplers =
	{
		MapTexture =
		{
			Index = 0
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "None"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
	}
}


VertexStruct VS_OUTPUT
{
	float4  vPosition : PDX_POSITION;
	float2  vTexCoord : TEXCOORD0;
};


VertexShader =
{
	MainCode VertexShader
	[[
		VS_OUTPUT main(const VS_INPUT v )
		{
		    VS_OUTPUT Out;
			Out.vTexCoord = v.vTexCoord;
			Out.vPosition  = mul( WorldViewProjectionMatrix, float4( v.vPosition, 1 ) );
			
		    return Out;
		}
	]]
}

PixelShader =
{
	MainCode PixelShaderUp
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			// Dispaly the first frame
			float4 OutColor = tex2D( MapTexture, v.vTexCoord );
			return OutColor;
		}
	]]

	MainCode PixelShaderDisable
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			// Play the animation with a delay
			float time_offset = (Offset*8) / 100.0;
			float2 frame_offset = float2(min(max(floor((Time - AnimationTime - time_offset)*14), 0)/8.0, 7.0/8.0), 0.0);
			float vTime = saturate( (Time - AnimationTime)*16 );
		    float4 OutColor = tex2D( MapTexture, v.vTexCoord + frame_offset);
			return OutColor;
		}
	]]

	MainCode PixelShaderDown
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float vTime = saturate( (Time - AnimationTime)*16 );
		    float4 OutColor = tex2D( MapTexture, v.vTexCoord);
			OutColor.rgb -= float3(0.4, 0.4, 0.4) * vTime;
			return OutColor;
		}
	]]

	MainCode PixelShaderOver
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
		    float4 OutColor = tex2D( MapTexture, v.vTexCoord );
			float vTime = 0.9 - saturate( (Time - AnimationTime) * 4 );
			vTime *= vTime;
			vTime = 0.9*0.9 - vTime;
		    float4 MixColor = float4( 0.15, 0.15, 0.15, 0 ) * vTime;
		    OutColor.rgb += ( 0.5 + OutColor.rgb ) * MixColor.rgb;
			return OutColor;
		}
	]]
}


BlendState BlendState
{
	BlendEnable = yes
	SourceBlend = "SRC_ALPHA"
	DestBlend = "INV_SRC_ALPHA"
}


Effect Up
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderUp"
}

Effect Down
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderDown"
}

Effect Disable
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderDisable"
}

Effect Over
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderOver"
}


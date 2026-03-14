Includes = {
	"buttonstate.fxh"
	"sprite_animation.fxh"
}

PixelShader =
{
	Samplers =
	{
		MapTexture =
		{
			Index = 0
			MagFilter = "Point"
			MinFilter = "Point"
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
			Out.vPosition = mul(WorldViewProjectionMatrix, float4(v.vPosition.xyz, 1));
			Out.vTexCoord = v.vTexCoord;
			return Out;
		}
	]]
}

PixelShader =
{
	MainCode PixelShaderShow
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float vTime = Time - AnimationTime;
			float opacity = vTime / 6;

			if (vTime > 6) {
				return float4(0, 0, 0, 1);
			}
			return float4(1, 1, 1, opacity);
		}
	]]

	MainCode PixelShaderHide
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float vTime = Time - AnimationTime;
			float opacity = 1 - vTime / 6;

			if (opacity >= 0){
				return float4(0, 0, 0, opacity);
			}
			return float4(0, 0, 0, 0);
		}
	]]
}

BlendState BlendState
{
	BlendEnable = yes
	SourceBlend = "src_alpha"
	DestBlend = "inv_src_alpha"
}

Effect Up
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderShow"
}

Effect Disable
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderHide"
}

# Unused
Effect Down
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderShow"
}

# Unused
Effect Over
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderHide"
}
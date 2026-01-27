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
	MainCode PixelShader
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float vTime = (Time - AnimationTime);
			float vEnd = (3.141592f / 2.f);
			if(v.vTexCoord.x <= sin(vTime) || vTime > vEnd){
				float4 OutColor = tex2D( MapTexture, v.vTexCoord );
				return OutColor;
			}
			else {
				return float4(0.f, 0.f, 0.f, 0.f);
			}
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
	PixelShader = "PixelShader"
}

Effect Down
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShader"
}

Effect Disable
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShader"
}

Effect Over
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShader"
}
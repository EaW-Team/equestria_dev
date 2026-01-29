### Wipe text reveal by Scars
# Recommended for non-monospaced fonts
# How to activate animation:
#	- Give the element (that was assigned the gfx) a _click_enabled trigger
#	- Alternate between having the trigger evaluate TRUE or FALSE (e.g. country flag that constantly flips) to trigger the animation

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
			// Put the frame information as the number of lines
			// For example, 19 lines will be `frame = 19`

			float numberOfLines = Offset.x + 1;
			float linesPerSecond = 1.5;

			float vTime = (Time - AnimationTime) * linesPerSecond;
			float yRoundedTime = ceil(vTime)/numberOfLines;
			float xRoundedTime = vTime - floor(v.vTexCoord.y*numberOfLines);
			
			if(v.vTexCoord.x <= xRoundedTime && v.vTexCoord.y <= yRoundedTime){
				return float4(0.0, 0.0, 0.0, 0.0);
			}
			else {
				return tex2D( MapTexture, v.vTexCoord );
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
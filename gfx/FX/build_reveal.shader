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
			float imageSegments = Offset.x + 1;

			float vTime = (Time - AnimationTime)*0.5;
			float rangeLower = floor(v.vTexCoord.x*imageSegments)/imageSegments;
			vTime -= rangeLower;

			float yOffset = 0.2f;
			float speedFactor = 4.5f;

			v.vTexCoord.y += yOffset;
			if(vTime*speedFactor <= 1.570796f && sin(vTime*speedFactor) * yOffset < yOffset){
				v.vTexCoord.y -= sin(vTime*speedFactor) * yOffset;
			}
			else{
				v.vTexCoord.y -= yOffset;
			}		
			
			float4 OutColor = tex2D(MapTexture,v.vTexCoord);

			if(vTime < 0.2f){
				OutColor.a *= vTime*5;
			}
			
			return OutColor;
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
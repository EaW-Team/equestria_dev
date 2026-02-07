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
	MainCode PixelShaderUp
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float pi = 3.14159265;
			float vTime = (Time - AnimationTime);
			float vTimeSmooth = 0.0;
			if(vTime < 1.0)
				vTimeSmooth = sin(vTime * pi / 2);
			else
				vTimeSmooth = 1.0;

			float2 vDiff = 0.5 - v.vTexCoord;
			float vAngle = atan2(vDiff.y, vDiff.x) - pi/2;
			if (vAngle < 0.0)
				vAngle += 2 * pi;
			
			float vLerp = saturate( ( vAngle - vTimeSmooth * pi * 2.0 ) * 50.0 );
			float4 vOne = tex2D( MapTexture, v.vTexCoord );
			float4 vTwo = (0.0, 0.0, 0.0, 0.0);
			return lerp( vOne, vTwo, vLerp );
		}	
	]]
	MainCode PixelShaderDisable
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float pi = 3.14159265;
			float vTime = (Time - AnimationTime);
			float vTimeSmooth = 0.0;
			if(vTime < 1.0)
				vTimeSmooth = sin(vTime * pi / 2);
			else
				vTimeSmooth = 1.0;

			float2 vDiff = 0.5 - v.vTexCoord;
			float vAngle = atan2(vDiff.y, vDiff.x) - pi/2;
			if (vAngle < 0.0)
				vAngle += 2 * pi;
			
			float vLerp = saturate( ( vAngle - vTimeSmooth * pi * 2.0 ) * 50.0 );
			float4 vOne = (0.0, 0.0, 0.0, 0.0);
			float4 vTwo = tex2D( MapTexture, v.vTexCoord );
			return lerp( vOne, vTwo, vLerp );
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
	PixelShader = "PixelShaderUp"
}

Effect Disable
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderDisable"
}

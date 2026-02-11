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
			float vTime = (Time - AnimationTime);
			float pi = 3.14159265;

			float speedFactor = round(Offset.x) + 1;
			float vTimeScaled = 0.5 * vTime * speedFactor;

			float2 vDiff = 0.5 - v.vTexCoord;

			float vAngle = atan2(vDiff.y, vDiff.x) - pi/2;
			if (vAngle < 0.0)
				vAngle += 2*pi;

			// length of arc: (pi/4) rad = 45 degrees
			float vArcRad = clamp(vTime * speedFactor, 0.0, 1.0) * pi / 4;

			// first arc
			float vSpinA = frac(vTimeScaled) * pi + sin(3 * vTimeScaled);
			float vDistA = abs(vAngle - vSpinA);
			vDistA = min(vDistA, 2*pi - vDistA);
			float vLerpA = saturate((vArcRad - vDistA) * 50.0);

			// opposite arc, 180 degrees offset + correction
			float vSpinB = vSpinA + pi;
			vSpinB = fmod(vSpinB, 2*pi);
			float vDistB = abs(vAngle - vSpinB);
			vDistB = min(vDistB, 2*pi - vDistB);
			float vLerpB = saturate((vArcRad - vDistB) * 50.0);

			// combine
			float vLerp = vLerpA + vLerpB;

			float4 vOne = tex2D(MapTexture, v.vTexCoord);
			float4 vTwo = float4(0.0, 0.0, 0.0, 0.0);

			float4 Out = lerp(vTwo, vOne, vLerp);

			return Out;
		}	
	]]
	MainCode PixelShaderDisable
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			return float4(0.0, 0.0, 0.0, 0.0);
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

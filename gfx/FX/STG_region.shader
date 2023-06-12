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
	float4  vPosition_in : POSITION;
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
            int fillingType = (int)(Offset*2) & 0x3;
            int fillingVal  = ((int)(Offset*2) >> 2) & 0xFF;
            float4 colorSelect   = float4(0, 1.0, 0.0, 1.0);
            float4 colorHomeBase = float4(1.0, 0, 1.0, 1.0);
			float4 colorEmpty = float4(0, 0, 1.0, 1.0);
			float4 colorFull = float4(1.0, 0, 0, 1.0);

			float2 fillCoord = v.vTexCoord;
            fillCoord.x += 0.5;
			float4 fillColor = tex2D( MapTexture, fillCoord );
            if (fillColor.w != 0.0) {
                fillColor = float4(0, 1.0, 1.0, 1.0);
                if (fillingType == 1) {
                    fillColor = colorSelect;
                } else if (fillingType == 2) {
                    fillColor = colorHomeBase;
                } else {
					fillColor = lerp(colorEmpty, colorFull, fillingVal/255.0);
				}
            } else {
                fillColor = float4(1.0, 1.0, 1.0, 0.0);
            }

            float4 maskColor = tex2D( MapTexture, v.vTexCoord );

            float alpha_out   = maskColor.w + fillColor.w*(1.0 - maskColor.w);
            float3 mixedColor = (maskColor.xyz*maskColor.w + fillColor.xyz*fillColor.w*(1.0 - maskColor.w))/alpha_out;

            return float4(mixedColor, alpha_out);
		}
	]]

	MainCode PixelShaderDisable
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
		    float4 OutColor = tex2D( MapTexture, v.vTexCoord);
			return OutColor;
		}
	]]

	MainCode PixelShaderDown
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			int fillingType = (int)(Offset*2) & 0x3;
            int fillingVal  = ((int)(Offset*2) >> 2) & 0xFF;
            float4 colorSelect   = float4(0, 1.0, 0.0, 1.0);
            float4 colorHomeBase = float4(1.0, 0, 1.0, 1.0);
			float4 colorEmpty = float4(0, 0, 1.0, 1.0);
			float4 colorFull = float4(1.0, 0, 0, 1.0);

			float2 fillCoord = v.vTexCoord;
            fillCoord.x += 0.5;
			float4 fillColor = tex2D( MapTexture, fillCoord );
            if (fillColor.w != 0.0) {
                fillColor = float4(0, 1.0, 1.0, 1.0);
                if (fillingType == 1) {
                    fillColor = colorSelect;
                } else if (fillingType == 2) {
                    fillColor = colorHomeBase;
                } else {
					fillColor = lerp(colorEmpty, colorFull, fillingVal/255.0);
				}
            } else {
                fillColor = float4(1.0, 1.0, 1.0, 0.0);
            }

            float4 maskColor = tex2D( MapTexture, v.vTexCoord );

            float alpha_out   = maskColor.w + fillColor.w*(1.0 - maskColor.w);
            float3 mixedColor = (maskColor.xyz*maskColor.w + fillColor.xyz*fillColor.w*(1.0 - maskColor.w))/alpha_out;

		    float4 OutColor = float4(mixedColor, alpha_out);

			float vTime = saturate( (Time - AnimationTime)*16 );
			OutColor.rgb -= float3(0.4, 0.4, 0.4) * vTime;
			return OutColor;
		}
	]]

	MainCode PixelShaderOver
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{

			int fillingType = (int)(Offset*2) & 0x3;
            int fillingVal  = ((int)(Offset*2) >> 2) & 0xFF;
            float4 colorSelect   = float4(0, 1.0, 0.0, 1.0);
            float4 colorHomeBase = float4(1.0, 0, 1.0, 1.0);
			float4 colorEmpty = float4(0, 0, 1.0, 1.0);
			float4 colorFull = float4(1.0, 0, 0, 1.0);
			
			float2 fillCoord = v.vTexCoord;
            fillCoord.x += 0.5;
			float4 fillColor = tex2D( MapTexture, fillCoord );
            if (fillColor.w != 0.0) {
                fillColor = float4(0, 1.0, 1.0, 1.0);
                if (fillingType == 1) {
                    fillColor = colorSelect;
                } else if (fillingType == 2) {
                    fillColor = colorHomeBase;
                } else {
					fillColor = lerp(colorEmpty, colorFull, fillingVal/255.0);
				}
            } else {
                fillColor = float4(1.0, 1.0, 1.0, 0.0);
            }

            float4 maskColor = tex2D( MapTexture, v.vTexCoord );

            float alpha_out   = maskColor.w + fillColor.w*(1.0 - maskColor.w);
            float3 mixedColor = (maskColor.xyz*maskColor.w + fillColor.xyz*fillColor.w*(1.0 - maskColor.w))/alpha_out;

		    float4 OutColor = float4(mixedColor, alpha_out);
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


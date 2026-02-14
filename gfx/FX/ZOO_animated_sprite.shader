# ##########
# EaW Team #
# ##########
# Scars' adaptation of crni's `animated_sprite.shader` specifically tailored for ZOO's train animation
# Includes hardcoded variable values and looping horizontal slide

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
			Out.vTexCoord = v.vTexCoord;
			Out.vPosition  = mul( WorldViewProjectionMatrix, float4( v.vPosition, 1 ) );

		    return Out;
		}
	]]
}

PixelShader =
{
	MainCode PixelShader
	[[

        float part_dec(float x) {
            return x - floor(x);
        }
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
            int nb_frames = 14;
            // Get the inputs parameters
            int offsetInt = int(round(Offset.x*nb_frames));
            int start_frame   = 1;
            int end_frame     = 14;
            int frame_per_sec = 180;
            int looping       = 1;

            // Compute the effective fps
            float fps = float(frame_per_sec + 1)/256.0;
            fps = fps*fps * 50;

			// Display the first frame
            float delta_time = (Time - AnimationTime)*fps/(end_frame - start_frame);
            float current_frame_offset = floor(part_dec(delta_time)*(end_frame - start_frame));
            if ((looping == 0) && (delta_time >= 1.0) ) {
                current_frame_offset = end_frame - start_frame - 1;
            }

            v.vTexCoord.x += float(start_frame + current_frame_offset)/nb_frames;
            v.vTexCoord.x -= (Time - AnimationTime)*0.009;

            return tex2D(MapTexture, v.vTexCoord);
		}
	]]

	MainCode PixelShaderDown
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			return float4(0, 0, 0, 1);
		}
	]]

	MainCode PixelShaderOver
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
		    return float4(0.5, 0.5, 0.5, 1);
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
	PixelShader = "PixelShaderDown"
}

Effect Over
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderOver"
}
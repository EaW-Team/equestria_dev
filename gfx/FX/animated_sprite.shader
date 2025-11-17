# ##########
# EaW Team #
# ##########
# Description
# This shader implements a generic code controllable animation
# Its main purpose is to allow more liberties and diminish code bloatting when doing custom animations
# It features : - Start / end frame selection
#               - Animation looping
#               - Parametrable framerate
# When changing the parameters, the continuity is not guaranted
# The texture file used need to have a padding frame at the end that contain the number of frames in the color
#     -> For a strip of 4 frames, append a 5th that containe the color (4, 4, 4, 4) in RGBA. Declare the GFX as having 5 frame
# Support 64 frames maximum, that should be 3 pixels wide minimum
# ##########
# Input : start_frame   - The animation start frame, a 6bits unsigned integer (Range [0, 63])
#         end_frame     - The animation end frame, a 6bits unsigned integer (Range [0, 63])
#         frame_per_sec - The animation speed, a 8bits unsigned integer (Range [0, 255])
#                           effective fps in frame/s being fps = ((frame_per_sec+1)/256)² * 20
#         looping       - Boolean that indicate if the animation should loop, a 1bit field
# Input format :
#                Fields | looping | frame_per_sec | end_frame | start_frame |
#                  Bits |   20    |   19  |   12  |  11  |  6 |   5  |   0  |
# Up       : Do the animation from the start. Alternate with enable / disable to restart the animation in case of non looping
# Disabled : Do the animation from the start. Alternate with enable / disable to restart the animation in case of non looping
# Over : Not used, sprite need to be declared as alwaystransparent
# Down : Not used, sprite need to be declared as alwaystransparent
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

		// These additional extensions are here for OpenGL compatibility
		#ifdef PDX_OPENGL
			#extension GL_ARB_shader_texture_lod : enable
			#extension GL_EXT_gpu_shader4 : enable
		#endif

        float part_dec(float x) {
            return x - floor(x);
        }
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
            // The number of frames is in the last frame
            float4 frame_size = tex2D( MapTexture, float2((Offset.x - NextOffset.x)/2, 0));
            int nb_frames = int(round(frame_size.x * 256) + 1);
            // Get the inputs parameters
            int offsetInt = int(round(Offset.x*nb_frames));
            int start_frame   = (offsetInt >> 0)  & 0x3F;
            int end_frame     = ((offsetInt >> 6) & 0x3F) + 1;
            int frame_per_sec = (offsetInt >> 12) & 0xFF;
            int looping       = (offsetInt >> 20) & 0x1;


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
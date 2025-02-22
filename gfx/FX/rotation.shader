# ##########
# EaW Team #
# ##########
# Description
# This shader implements a way to rotate texture using a variable
# It features : - Pivot point selection
#               - Dynamic rotation
# Limitations : - The Pivot Point is static and cannotbe change through variable
#               - The image size is limited to 999. (Though there are way to bypass that limitation, ask the EaW team if needed. Or check the maths that come next)
# ##########
# GFX definition :
# progressbartype = {
# 	name = "GFX_exemple_rotation"
# 	color = { 0.5 1 0.5 } # Pivot point position
# 	colortwo = { 0.080 0.080 0.0 } # Size of the texture in pixel divided by 1000
# 	textureFile1 = "gfx/debug_rotation.dds" # Only the first texture is used
# 	textureFile2 = "gfx/debug_rotation.dds"
# 	size = { x = 80 y = 80 } # Set the value to the actual size of the texture
# 	steps = 360 # The step 0 correspond to 0°, the max step is 360.
# 	effectFile = "gfx/FX/rotation.lua"
# }
# Input : angle - the angle is pass to the shader through the frame variable in the scripted GUI.
# All the computation are done in the Vertex Shader. The main thing to do is set up correctly the Pivot Point in the GFX definition.
# Pivot Point coordinates, with the origin set at the center of the texture :
#	((color[0] - 0.5)*scaling*texture_size_x, (color[1] - 0.5)*scaling*texture_size_y)
# color[0] - The first field in color
# color[1] - The second field in color
# scaling  - Scaling factor, allowing to place the pivot point out of the texture boundaries if needed. Equals to 1 + 2.f*color[2].
# The texture_size variable are set using the colorTwo as explained in the GFX definition.
#
# Using the scaling, it is then possible to position the Pivot Point outside the texture boundaries.
# ##########

Includes = {
}

PixelShader =
{
	Samplers =
	{
		TextureOne =
		{
			Index = 0
			MagFilter = "linear"
			MinFilter = "linear"
			MipFilter = "linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		TextureTwo =
		{
			Index = 1
			MagFilter = "linear"
			MinFilter = "linear"
			MipFilter = "linear"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
	}
}


VertexStruct VS_INPUT
{
    float4 vPosition  : POSITION;
    float2 vTexCoord  : TEXCOORD0;
};

VertexStruct VS_OUTPUT
{
    float4  vPosition : PDX_POSITION;
    float2  vTexCoord0 : TEXCOORD0;
};


ConstantBuffer( 0, 0 )
{
	float4x4 WorldViewProjectionMatrix;
	float4 vFirstColor;
	float4 vSecondColor;
	float CurrentState;
};


VertexShader =
{
	MainCode VertexShader
	[[

		// These additional extensions are here for OpenGL compatibility
		#ifdef PDX_OPENGL
			#extension GL_EXT_gpu_shader4 : enable
		#endif

		VS_OUTPUT main(const VS_INPUT v )
		{
			VS_OUTPUT Out;
			// Get the position from the first color, scaling using the blue color
			// Second color is the size in pixel of the image
			float scaling_factor  = 1 + 2.f*vFirstColor.z;
			float2 size_image     = float2(round(vSecondColor.x*1000),
									       round(vSecondColor.y*1000));
			float4 rotation_pivot = float4((vFirstColor.x - .5f)*size_image.x*scaling_factor + .5f*size_image.x,
										   (vFirstColor.y - .5f)*size_image.y*scaling_factor + .5f*size_image.y,
										   0.f,
										   0.f);

			// Apply the rotation
			const float pi = 3.141592;
			float rad = 2*pi*CurrentState;
			float4x4 rot_matrix = float4x4(cos(rad), -sin(rad), 0, 0,
										   sin(rad),  cos(rad), 0, 0,
										   0,         0,        1, 0,
										   0,         0,        0, 1);

			float4 rot_position = mul(rot_matrix, v.vPosition - rotation_pivot);

		   	Out.vPosition  = mul(WorldViewProjectionMatrix, rot_position + rotation_pivot);
			Out.vTexCoord0 = float2(v.vTexCoord.x, -v.vTexCoord.y);

			return Out;
		}

	]]
}

PixelShader =
{
	MainCode PixelColor
	[[

		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			if( v.vTexCoord0.x <= CurrentState / 2.f )
				return vFirstColor;
			else
				return vSecondColor;
		}

	]]

	MainCode PixelTexture
	[[

		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float rot = CurrentState * 3.14159265f;
			return tex2D(TextureOne, v.vTexCoord0);
		}

	]]
}


BlendState BlendState
{
	BlendEnable = yes
	SourceBlend = "SRC_ALPHA"
	DestBlend = "INV_SRC_ALPHA"
}


Effect Color
{
	VertexShader = "VertexShader"
	PixelShader = "PixelColor"
}

Effect Texture
{
	VertexShader = "VertexShader"
	PixelShader = "PixelTexture"
}

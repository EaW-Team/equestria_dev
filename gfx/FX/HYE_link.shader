# ##########
# EaW Team #
# ##########
# Description
# This shader is used in the underground SGUI for HYE
# Its main purpose is to generate the links between the node for the underground map
# It features : - Parametrable length
# 			    - Dynamic rotation angle
# 			    - One dynamic transitional animation
# ##########
# Input : angle  - The angle of rotation, 8bits unsigned (Range [0, 360[ degrees)
# 		  length - Length of the link, 7bits unsigned (Range [0, 118])
# Input format :
#                Fields | angle  | length |
#                  Bits | 15 | 8 |  7 | 0 |
# Up       : Basic state, no animation or filling
# Disabled : Play a filling animation when switching from Up to Disabled
# Over : Unused, use alwaystransparent = yes
# Down : Unused, use alwaystransparent = yes
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

# Vectex structure modified to pass the pixel coordinate
# It is neccessary to avoid the sampler between the VertexShader and the PixelShader
VertexStruct VS_OUTPUT
{
	float4  vPosition : PDX_POSITION;
	float2  vTexCoord : TEXCOORD0;
	float4  vPosition_in : POSITION;
};


VertexShader =
{
	# The Vertex shader take care of the rotation
	MainCode VertexShader
	[[
		VS_OUTPUT main(const VS_INPUT v )
		{
		    VS_OUTPUT Out;
			Out.vTexCoord = v.vTexCoord;
			Out.vPosition_in = float4(v.vPosition, 0); // The magic to avoid the sampler : doing pixel manipulation after the vertex shader
			float size_img[] = {128.0, 8.0};
			float angle = (float)(((int)(Offset * 3.0) >> 7) & 0xFF)/256.0 * 2*3.14159265;

			float3 tmp_position = v.vPosition;
			tmp_position.x -= size_img[0]/2;
			tmp_position.y -= size_img[1]/2;
			float3x3 rot_matrice = float3x3(cos(angle), -sin(angle), 0.0,
											sin(angle), cos(angle), 0.0,
											0.0, 0.0, 0.0);
			tmp_position = mul(rot_matrice, tmp_position);
			tmp_position.x += size_img[0]/2;
			tmp_position.y += size_img[1]/2;
			Out.vPosition  = mul( WorldViewProjectionMatrix, float4( tmp_position.xyz, 1 ) );
			
		    return Out;
		}
	]]
}

# The pixels shader compute the size of the link and its animation
PixelShader =
{
	# When the link is enabled, no animation is applied
	MainCode PixelShaderUp
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float bound_size[] = {5.0, 3.0, 5.0};
			float size_link = (float)((int)(Offset * 3.0) & 0x7F);
			float max_size_link = 3.0*39.0;
			float size_img = 128.0;
			float bound_size_link = (size_img - (bound_size[0] + size_link + bound_size[2])) / 2;
			float2 tmp;

			// Translation to center the link
			float2 pos_trans = float2(v.vPosition_in.x - bound_size_link,
									  v.vPosition_in.y);
			if (pos_trans.x < bound_size[0]) {
				// Left bound
				tmp = float2((pos_trans.x) / 3 / size_img, pos_trans.y / 8.0);
			} else if (pos_trans.x < bound_size[0] + size_link) {
				// Middle section
				tmp = float2((pos_trans.x) / 3 / size_img, pos_trans.y / 8.0);
			} else {
				// Right bound
				tmp = float2((pos_trans.x + max_size_link - size_link ) / 3 / size_img, pos_trans.y / 8.0);
			}
			
			float4 OutColor = tex2D( MapTexture, tmp);
			// Masking if out of link bounds
			if ((v.vPosition_in.x <= bound_size_link) ||
				(v.vPosition_in.x > size_link + bound_size[0] + bound_size[2] + bound_size_link)) {
				OutColor = float4(0, 0, 0, 0);
			}
			return OutColor;
		}
	]]

	# When the link is disabled, it will fill from left end to the right with an animation
	MainCode PixelShaderDisable
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float bound_size[] = {5.0, 3.0, 5.0};
			float size_link = (float)((int)(Offset * 3.0) & 0x7F);
			float max_size_link = 3.0*39.0;
			float size_img = 128.0;
			float bound_size_link = (size_img - (bound_size[0] + size_link + bound_size[2])) / 2;
			float2 tmp;

			int middle_section_anim_duration = 5;
			int animated_filling[2] = {2, 2};
			int static_component[2] = {bound_size[0] - animated_filling[0],
									   bound_size[1] - animated_filling[1]};

			// Linear filling rate => Double the size, double the time to fill the link
			int filling = (int)floor((Time - AnimationTime)*100);
			int anim_bound = min(static_component[0] - 1 + animated_filling[0] + size_link + animated_filling[1] + middle_section_anim_duration - 1, filling);
			//anim_bound = 2 + 2 + size_link + 5; // Debugging line, to test fixed bound value

			// Translating to center the link
			float2 pos_trans = float2(v.vPosition_in.x - bound_size_link,
									  v.vPosition_in.y);
			if (pos_trans.x < bound_size[0]) {
				// Left bound
				tmp = float2((pos_trans.x) / 3 / size_img, pos_trans.y / 8.0);
			} else if (pos_trans.x < bound_size[0] + size_link) {
				// Middle section
				tmp = float2((pos_trans.x) / 3 / size_img, pos_trans.y / 8.0);
			} else {
				// Right bound
				tmp = float2((pos_trans.x + max_size_link - size_link ) / 3 / size_img, pos_trans.y / 8.0);
			}

			// Animation
			// anim_bound is the progress of filling
			// stable_bound is when there is no more transitory pixels state to the left of this value
			int pos_x = (int)pos_trans.x;
			int stable_bound = anim_bound - middle_section_anim_duration;
			if (pos_x <= stable_bound) {
				tmp.x += 2.0/3.0;
			} else if (pos_x <= anim_bound) {
				if (pos_x < bound_size[0]) {
					// Left bound
					tmp.x = (128.0 + pos_x + max(anim_bound - static_component[0], 0)*13.0 + 0.5) / 3.0 / size_img;
				} else if (pos_x < size_link + bound_size[0]) {
					// Middle section
					tmp.x = (128.0 + 5.0 + (anim_bound - pos_x)*13.0 + 0.5) / 3.0 / size_img;
				} else {
					// Right bound
					tmp.x = (128.0 + 9.0 + pos_x - (size_link + bound_size[0] + 1) + (anim_bound - (size_link + bound_size[0]))*13.0 + 0.5) / 3.0 / size_img;
				}
			}
			
			float4 OutColor = tex2D( MapTexture, tmp);
			// Masking if out of link bounds
			if ((v.vPosition_in.x <= bound_size_link) ||
				(v.vPosition_in.x > size_link + bound_size[0] + bound_size[2] + bound_size_link)) {
				OutColor = float4(0, 0, 0, 0);
			}
			return OutColor;
		}
	]]

	# Unused
	MainCode PixelShaderDown
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
		    float4 OutColor = tex2D( MapTexture, v.vTexCoord );
			return OutColor;
		}
	]]

	# Unused
	MainCode PixelShaderOver
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
		    float4 OutColor = tex2D( MapTexture, v.vTexCoord );
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

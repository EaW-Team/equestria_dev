# Radar graph (5-axis) by Scars
# Description
# This shader implements a programmable radar graph chart with 5 axis
# Input format :
#      Fields | Output Axis of Sector 2  | Output Axis of Sector 1  | Input Axis of Sector 2  | Input Axis of Sector 1 |   Sector    |
#        Bits |     22      |     18     |     17      |     13     |     12      |     8     |     7      |     3     |  2  |   0   |
# `textureFile` is a square with the desired area with the filled color

# Instead of one single sprite for the entire radar graph, uses five different elements representing each sector between two axes, and creates an amimation which smoothly interpolates the initial and final states
# Limited to 26 (0-25) discrete levels for each axis due to bit limitation with feeding the data
# use the `calculate_radar_graph_5axis_anim_frame` scripted effect by feeding in a temp array 0-1 decimal for each axis_init^{i} and axis_final^{i}, i=0,1,..,4
# use the output `sector_frame^{k}`, k=1,2,...,5 to feed frame data into every element. Gridbox use recommended.
# animation uses a fliping country flag in an `<element>_click_enabled` trigger to re-trigger the animation after every change of value

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
			MagFilter = "Linear"
			MinFilter = "Linear"
			MipFilter = "None"
			AddressU = "Clamp"
			AddressV = "Clamp"
			MipMapLodBias = -0.8
		}
		MaskingTexture =
		{
			Index = 5
			MagFilter = "Point"
			MinFilter = "Point"
			MipFilter = "None"
			AddressU = "Clamp"
			AddressV = "Clamp"
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
		    Out.vPosition  = mul( WorldViewProjectionMatrix, float4( v.vPosition.xyz, 1 ) );
		    Out.vTexCoord = v.vTexCoord;
			// Out.vTexCoord += Offset;
		
		    return Out;
		}
	]]
}

PixelShader =
{
	MainCode PixelShaderRadarGraphAnim
	[[
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
		    float4 FilledColor = tex2D( MapTexture, v.vTexCoord );
		    float4 EmptyColor = float4( 0.0, 0.0, 0.0, 0.0 );

			float x = 2 * v.vTexCoord.x - 1;
			float y = 2 * v.vTexCoord.y - 1;
			y *= -1;

			float pi = 3.141592654;

			#ifdef PDX_OPENGL
				float angles[5] = float[5](
					2*pi*0/5,
					2*pi*1/5,
					2*pi*2/5,
					2*pi*3/5,
					2*pi*4/5
				);
			#else
				float angles[5] = {
					2*pi*0/5,
					2*pi*1/5,
					2*pi*2/5,
					2*pi*3/5,
					2*pi*4/5
				};
			#endif

			float vTimeClamped = sin(clamp(2*(Time-AnimationTime),0,pi/2));
			int data = int(Offset.x) + 1;

			#ifdef PDX_OPENGL
				float thisSector = mod(data, 8.0);
			#else
				int thisSector = (data >> 0) & 0x7;
			#endif

			#ifdef PDX_OPENGL
				float scale_init[2] = float[2](
					float(mod(float(data) / 8.0, 32.0)) / 25.0,
					float(mod(float(data) / 256.0, 32.0)) / 25.0
				);
			#else
				float scale_init[2] = {
					float((data >> 3) & 0x1F) / 25.0,
					float((data >> 8) & 0x1F) / 25.0
				};
			#endif

			#ifdef PDX_OPENGL
				float scale_final[2] = float[2](
					float(mod(float(data) / 8192.0, 32.0)) / 25.0,
					float(mod(float(data) / 262144.0, 32.0)) / 25.0
				);
			#else
				float scale_final[2] = {
					float((data >> 13) & 0x1F) / 25.0,
					float((data >> 18) & 0x1F) / 25.0
				};
			#endif

			float2 origin = float2(0.0, 0.0);

			#ifdef PDX_OPENGL
				float2 coords_flat[5] = float2[5](
					float2(sin(angles[0]),cos(angles[0])),
					float2(sin(angles[1]),cos(angles[1])),
					float2(sin(angles[2]),cos(angles[2])),
					float2(sin(angles[3]),cos(angles[3])),
					float2(sin(angles[4]),cos(angles[4]))
				);
			#else
				float2 coords_flat[5] = {
					float2(sin(angles[0]),cos(angles[0])),
					float2(sin(angles[1]),cos(angles[1])),
					float2(sin(angles[2]),cos(angles[2])),
					float2(sin(angles[3]),cos(angles[3])),
					float2(sin(angles[4]),cos(angles[4]))
				};
			#endif

			#ifdef PDX_OPENGL
				float2 thisSectorCoords[3] = float2[3](
					origin,
					lerp(scale_init[0],scale_final[0],vTimeClamped)*coords_flat[int(thisSector-1)],
					lerp(scale_init[1],scale_final[1],vTimeClamped)*coords_flat[int(mod(thisSector,5.0))]
				);
			#else
				float2 thisSectorCoords[3] = {
					origin,
					lerp(scale_init[0],scale_final[0],vTimeClamped)*coords_flat[thisSector-1],
					lerp(scale_init[1],scale_final[1],vTimeClamped)*coords_flat[thisSector%5]
				};
			#endif

			// Loops through every boundary line to check if a pixel is inside the polygon
			// uses bool insidePoly which acts as a counter for how many boundary lines are there to the right of a certain y-level
			// 0 intersections to the right: not inside (false)
			// 1 intersections to the right: is inside  (true)
			// 2 intersections to the right: not inside (false)
			bool insidePoly = false;
			for (int i = 0; i < 3; i++) {
				float2 point_a = thisSectorCoords[i];

				#ifdef PDX_OPENGL
					float2 point_b = thisSectorCoords[int(mod(i+1,3.0))];
				#else
					float2 point_b = thisSectorCoords[(i+1)%3];
				#endif

				// either point a or point b is above the current y level and the other is below, meaning this y-level must cross the line between those two points somewhere
				bool hasCrossing = (point_a.y > y) != (point_b.y > y);

				// find the x-coordinate where the y-line crosses the line between our two points
				float x_intersection = (point_b.x - point_a.x) * (y - point_a.y) / (point_b.y - point_a.y) + point_a.x;

				// skips check if there is no intersection with a boundary at this y-level
				// if the current x value is less than the intersection (current pixel is to the left of a boundary line), flip the boolean
				insidePoly = insidePoly != (hasCrossing && x < x_intersection);
			}

			return lerp(EmptyColor, FilledColor, int(insidePoly));
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
	PixelShader = "PixelShaderRadarGraphAnim"
}

Effect Down
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderRadarGraphAnim"
}

Effect Disable
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderRadarGraphAnim"
}

Effect Over
{
	VertexShader = "VertexShader"
	PixelShader = "PixelShaderRadarGraphAnim"
}


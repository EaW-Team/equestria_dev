
PixelShader = 
{
	Code
	[[
	
	//Untility function to check if day/night overrides need to be applied
	int dayNightOverrideCheck(in sampler2D gbChannel) {
		float HalfPix = 0.5f / GB_TextureHeight;
		float3 colorTest = tex2D( gbChannel, float2(0.20386f,0.27197f*(0.5f - HalfPix)));
		if ((0.036865f < colorTest.x && colorTest.x < 0.036966f) && (0.034423f < colorTest.y && colorTest.y < 0.034424f) && (0.097656f < colorTest.z && colorTest.z < 0.097657f)) {
			return 1;
		}
		return 0;
	}
	
	]]

}
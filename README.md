
# Hand-E

A robotic arm controlled via a Python script running on a microcontroller. Uses OpenCV & Mediapipe. Based on Tony Stark's Dum-E!


## History

The project was inspired by Tony Stark's Dum-E, an assistive robotic arm. Originally, the plan was to use OpenCV and Mediapipe in Python with the [**TVS**](https://github.com/aryan-cs/hand-e/tree/master/tvs-scdp#two-vector-system-for-single-camera-depth-perception) to relay information to an external microcontroller like an Arduino or RaspberryPi which controls servos. However, I quickly ran into issues with depth perception & the nature of the distance-dependent actuation. 

In light of this, I'm currently working on engineering a solution that requires only one camera. I've created a port-based script which sends information gathered by OpenCV on Python to Unity which recreates the nodes & connections of the hand to make a digital hand capable of interacting with the virtual world.


## Authors

- [@aryan-cs](https://www.github.com/aryan-cs)


## Contributing

Contributions are always welcome! Please fork the repository and create a pull request to contribute. Feel free to add yourself as an author in your contribution.


## Possible Contributions

For beginners, I'd recommend trying to work with the TVS-SCDP script and implementing a feature that accounts for the distance between the hand & camera to **determine the distance between the thumb & index fingers** (or, for that matter, any two arbitrarily chosen nodes). This can (mathematically) be done using some basic trigonometry. See below.
![Mathematic Approach](https://lh3.googleusercontent.com/pw/ABLVV87N23eN-vubOYyOMtdn-5643SNrh2KA6PLtccfV_Di9rlhsAPXCXCwS8vKNgfIn4-tmAbNNbTqjrp4CNII9PVKiNsbCnKHRew3QEbbesimsxKbvZXTZ81m78wEgVH3adXZZcBII4lgTsG1upX5R7WGIlmg_Z2tEnHblhdO1vJkA9bNe_CcPepIHM8M1bP8nydVHMSBA7XyK5xgGOBWBB9GLD1JLGRpYYL52uHlFEuoerVXuzuANZWQBq3_ECDinCHc9CkLKxn6oa_ndFQkicTc5RaAHzRz0xuHM1wzjJwR48g3WK6zJBjUDIq9H4hK5puVz2P67ruvuZ39J-9pLuKvTpGlUoKkRkocDfbrj5GDd9FnkxFFUqmoOlQU4v-jyPTA4aNzG2gAN23OmrbNSt9wJvCHE07b2T092WOYEBUUv5pXBWEKNxWxasB-ujxD8Zb_LYFgomBXMR0paV1awFl_T5qWqvOecaIZ-JXxh5TdwVBC2KaX746xP8HyHNV4Pu_lVnm51ZWB3r1kLLD_hgTHENNwSbCFsW4jMf__4y7C9HWOICChw9Yn0jdi66dnNYpzfJ_KCObWpcbSsI3nu865-VuNBWcUo4olUZcjfqDfxwGDgZS6N9tKJsIqibkok7QwIj9CRCbQvw9EdLdCl1Eof1Pb5CFhQOeknQqop0ZXrYjTU3zMMJRAGe8SvuozJewuOrbZk5RtS_SvTK8YWWTmNI-8_tkGuMA7zjSo_R4U5gt_jnsWFvwBu84-Jnj1Ej_VyImS3j7ifkVlf8qlgj7psy6idEgB2-Grk3CqrmKOqJ_crKdClbzzjAUup12cdpKff7nRrWPNpp-PWGs73vYKSyF-GWkTN0xIFJGKYT6uIi-Ifw_AwuNxsf31qCq9kggrQdsKMJrhjmyhzVbUYjJU68H5Fg_ICgTmIsf1pGLuTeFJKDC9e7DrdUbkH8FnU2fHS1OtOyAW_3tlV4R4uDhgB08cMVlqSCY3WwPEtPp--bX1HDdKW-CxJ_1EVpXDRz8l8MLhC9BOWhoFQTI-H_3JtO9j2bn4FPkmAe-PvTSVF1fxBIOWGhtSeBuhIvgxfropA2qbxrx4VrCpxKOewXjlycMODhE08VgMXRTjHR2FVOl5woKGyVbOD4uvRg2JC84yu0W35NaHqoI1XYvbmkhuY5teLekfKtYStzKEJTV-L1kwhmVGwOOUmGt7At-k-hfNQ2QhZBNlG97Se89J94m8zen2tBDmBn79wqc6Y8JEB=w400-h400-no?authuser=0&quot)

Where C represents the camera, A represents the index finger, and b represents the thumb.

Other possible contributions include...
- Adding documentation
- Finding a way to implement the TVS in `tvs.py`
- Optimizing code for efficiency
- Implementing a second camera for depth perception
- Anything meaningful you believe the project could benefit from!

# Tempo-change-pitch-converter
A simple tool that tells you what the new musical key is after speeding up/slowing down audio

In Ableton and many other modern DAWs, you can speed up or slow down audio. Ableton also let's you choose from different modes of doing this. Specifically the 'Repitch' mode, does this in a way like a vinyl player would. If you speed up the audio, its pitch gets higher, and if you slow down the audio, the pitch gets lower. It does this without regard for musical keys, which can sometimes be difficult if you want to use this sped up/slowed down audio in combination with other instruments that are tuned to the standard 440Hz. 

What this tool does is tell you what the new key is of your audio, plus or minus the amount of cents after you've slowed it up or down. 

For example: if your original audio is in D (minor or major don't matter in this case) at 90 BPM, and you've sped it up to 110 BPM, the tool will tell you that the new key of your audio is F + 47,41 cent. So to make it be exactly in the key of F, you will need to pitch down your sped up/slowed down audio 47 cents. Ableton's 'repitch' mode usually results in very few artifacts, because it is a more "natural" way of pitching audio (again think of how a vinyl player works). With this added tool, you then only have to correct for cents, never full semitones, which again usually gives very few artifacts. 
To do this in Ableton without any external plugins you would speed up/slow down to your desired tempo in Repitch mode, then consolidate the audio clip, choose any of the warp modes other than Repitch and pitch up or down by the required amount of cents to be exactly on key. 

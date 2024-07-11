---
title: Biophysical Society 2017 Takeaways
math: true
date: 2017-02-20
---

Last week I had a fun time in NOLA (New Orleans) at the Biophysical Society Annual Meeting! It was my first big conference and it was absolutely fabulous to see so much new and exciting work done from all kinds of different fields/approaches.  It kinda got me even more excited about biophysics - it felt like there were so many things that biophysical theory can be applicable to, from cancer to small peptide design, all the way to material engineering! 

![BPS 2017](/blog/figures-visuals/biophysics-everywhere.jpg)

With so many topics out there, I thought I'd highlight some of the really cool/exciting directions that biophysicists seem to be going in:

1. __Phase transitions.__ Turns out membraneless organelles and phase separation via biomolecules are more and more prevalent than anybody ever thought. Only now are we even starting to see connections to disease states, and maybe soon we'll start seeing even more biomedical relevance! Thanks to work by Ashutosh Chilkoti at Duke , we can even engineer phase transitioning peptides! For more information about membraneless organelles, Tanja Mittag at St. Jude has done a lot of ground breaking work showing biomedical and disease implications. 
2. __Membrane proteins.__ Everyone's working on it. Everyone's excited about it, and thanks to how far we've come with modern techniques, we're finally approaching the point where we can try and obtain large amounts of membrane proteins for all kinds of studies. Who knows, with the combination of modern tools and machine learning (*cough* Bil Clemons *cough*), we may get to the point someday where expressing membrane proteins is as easy as soluble ones! In particular, Ion Channels are getting even more attention than before, and there were a few great talks on G-Protein Coupled Receptors from the MacCammon lab!
4. On a more fundamental physics stage - there was some significant discussion on __the role of dispersion energies and their role in getting more accurate force fields__ and more atomic molecular simulations. As a reminder: non-bonded atom energies are split into electrostatics and van Der Waals (vdw) interactions. The vdw term is often represented by the Lennard-Jones potential: 

$$V(r) = 4\varepsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^{6} \right]$$


where:
- $V(r)$ is the potential energy as a function of the distance $r$ between the particles.
- $\varepsilon$ is the depth of the potential well.
- $\sigma$ is the finite distance at which the inter-particle potential is zero.
- $r$ is the distance between the particles.

The σ6 represents the attractive forces between atoms, also known as the dispersion term. And by tweaking that many people have managed to reparameterize force fields to better capture bulk solvent properties (like Osmotic Potential), but also a force field better able to capture both folded and Intrinsically disordered proteins. Personally, I sometimes am unable to distinguish if this is done out of convenience (because it’s a single uncomplicated parameter) or if there is also some physical insight behind why the dispersion terms need fixing. Either way, I'm excited to see where future work goes!

5. There are tons, tons of software packages out there to analyze MD Simulations (outside of MDTraj), and the best part is that many of them are available for free and in Python for the scientific community to use. I haven't had a chance to play with them all yet, but they all bring something new to the proverbial tool belt of a computational biophysicist:
    1. [MDAnalysis](https://www.mdanalysis.org/)
    2. [ProDy](http://www.bahargroup.org/prody/)
    3. There are far too many to discuss, but many people have generated cool new ways to look at networks of communication within protein dynamics, and understand allosteric communication and its effects (I'm particularly excited about these, seeing as they are incredibly relevant and supplementary to my own work!)



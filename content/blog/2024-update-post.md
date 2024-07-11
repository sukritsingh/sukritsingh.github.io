---
title: 2024 Update Post
date: 2024-07-11
---


Now that it's 2024 I realized I should probably sit down and write out some life updates
and what is going on! This will just be a set of updates on what I've been up to professionally
in the last few years:

## TLDR: Stay tuned for more papers and work, but I think I'll be going on the faculty
job search in the fall. Let me know if you know anybody hiring, and feel free to 
check out my [research](https://sites.google.com/site/sukritsingh92/about#h.xydjej2td3t4)!

## Papers
I've contributed to quite a few works over the last couple of years (check out my Google Scholar
if you're interested), but the big highlight is that I've been lucky enough to publish my 
first co-corresponding author paper! This was work driven by superstar graduate student Ivy Zhang
who helped drive and develop code to do Free Energy Calculations on mutations, as well as
parsing how we can assess sampling within this mutations.

- [Identifying and overcoming the sampling challenges in relative binding free energy calculations of a model protein:protein complex., J. Chem. Theory Comput., July 2023](https://doi.org/10.1021/acs.jctc.3c00333)

The other highlight was that I was the lead computational author in a study where we identified 
and mechanistically parsed drug-resistant mutations in the leukemia target Menin. This work was
particularly exciting to me as it served as a proof of concept for many of the tools and ideas I 
am excited about further developing:

- [MEN1 mutations mediate clinical resistance to Menin inhibition. Nature, 2023](https://doi.org/10.1038/s41586-023-05755-9)


## Awards

Thanks to the massive help and support of my co-mentors John and Markus, I was able to secure
independent funding for the first time in the form of a couple of fellowships!
- The [2024 National Cancer Institute (NCI) Pathway to Independence Award for Outstanding Early Stage Postdoctoral Researchers:](https://grants.nih.gov/grants/guide/rfa-files/RFA-CA-22-035.html) this 
transition to independence award gives me some independent funding to complete my postdoctoral training 
and will award me a larger sum of money upon starting my own independent grant funding! The wild part
of this application process was that each institution was only allowed to nominate _one_ person.
In other words I had to first win an internal competition followed by the full competition.

- The [2022 Damon Runyon Quantitative Biology Fellowship:](https://www.damonrunyon.org/news/entries/6716/)
This 2022 award was the a huge support for me obtaining independent funding in the future (including
the K99 award above!) It focuses on awarding quantitative biologists and computational-oriented folks
like me a chance at getting hybrid training in wet-lab an dry-lab biology.

- I was also lucky enough not only to present my work at the NCI Junior Investigators meeting
in 2023, I was also awarded Best Talk! This one was particularly fun for me as it was my 
first time presenting to a room full of folks who come from very diverse cancer-oriented backgrounds.

## Miscellaneous ones listed here

- I'm still involved in the social media of [Folding@home](https://x.com/foldingathome), albeit
less so nowadays due to other priorities
- I've now become one of the maintainers for [MDTraj](https://github.com/mdtraj/mdtraj), a repository
for analyzing large molecular dynamics simulation datasets at scale.

- Lastly, I spent a bit of time thinking about how to better embed trajectories into HTML, and with the
help of [Hugo MacDermott-Opeskin](https://github.com/hmacdope) I was lucky enough to be able to
achieve this goal! [Minimal_molview](https://github.com/hmacdope/minimal_molview/tree/main) is a library that allows one to embed interactive protein visualizations into webpages by generating the 
protein in an HTML format. A sample is below:

<iframe src="/molview/quick-flip-morph.html" style="width: 100%; height: 500px; border: none;"></iframe>
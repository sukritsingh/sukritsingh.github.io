---
title: Signaling in action
date: 2018-10-20
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Image with Captions and Markdown</title>
    <style>
        .image-container {
            text-align: center;
            margin-bottom: 1px;
        }
        .caption {
            font-size: 14px;
            color: #000; /* Black text */
            background-color: #fff; /* White background */
            border: 0px solid #000; /* Black border */
            padding: 5px;
            display: inline-block;
            margin-top: 1px;
        }
    </style>
</head>

## TL;DR: 
Our paper in eLife modeling G protein activation is out! 
Check it out [here](https://elifesciences.org/articles/38465)

A brief summary of our paper was also published as an [eLife digest](https://elifesciences.org/digests/38465/calling-all-neighbors)! 

## Introduction and Significance

To communicate and respond to our environment (i.e. via vision, smell, or taste), our cells rely on signaling cascades made up of groups of proteins that activate and deactivate one another, much like a circuit. 

Many cascades in our body involve heterotrimeric G proteins, which have three components  named G-alpha (Gα), G-beta (Gβ), and G-gamma (Gγ). Gα is a critical member of this trio, acting as a switch that turns on upon receiving a signal from a membrane protein receptor. This switch-like behavior of Gα is critical for life; both overactive and under-active Gα proteins have been linked to cancer, heart disease, and other disorders. However, no current therapies target Gα, despite the fact that roughly 40% of drugs on the market target other components of G-protein signaling cascades. 

<body>
    <div class="image-container">
        <img src="/blog/figures-visuals/2018-gpcr-fig1.png" alt="Original image" width="500">
        <div class="caption"><strong>Structural view of G protein signaling.</strong> a heterotrimeric G protein inside the cell (bottom) bound to the well known G protein coupled receptor (GPCR, orange). 
</div>
    </div>
</body>

Understanding the structural changes governing the switch-like behavior of Gα would shed light into how signals are transmitted within our cells. When Gα is off, it is bound to the small molecule Guanosine diphosphate (GDP). To turn on, Gα must release GDP to bind Guanosine triphosphate (GTP). However, the details of GDP release from Gα, the critical step of Gα activation, remain unclear. This is the focus of our paper - what atomic motions and molecular changes drive GDP release during the process of Gα activation?


<body>
    <div class="image-container">
        <img src="/blog/figures-visuals/2018-gpcr-fig2.png" alt="Original image" width="500">
        <div class="caption"><strong>Structure of Gα labelled.</strong> GDP (lime green) binds between the two domains.  
</div>
    </div>
</body>


## Combining powerful computational methods let us observe GDP release using unbiased simulations:
Simulations act as a “computational microscope,” capturing how Gα moves and changes shape. However, they can be computationally intensive, and so capturing a process that takes milliseconds like GDP unbinding can be difficult. In fact, GDP release is such a slow process that modeling it has never been done before! 

By combining a myriad of computational approaches, we were able to model GDP release. We used a variant of "adaptive seeding", where we ran biased simulations using a methodology named "Metadynamics" that pushed GDP out of it's binding pocket. These Metadynamics simulations, while observing GDP unbinding, are biased simulations, and so we cannot extract mechanistic information easily from these simulations. What we CAN do is seed unbiased simulations from these biased simulations (like in our workflow below). 

This effort was made possible through the generous donations of citizen scientists through the Folding@home distributed computing platform, who volunteered to run simulations on their personal computers. Their collective contributions generated data on Gα that would have taken approximately 150 years to collect on a typical desktop computer. 

<body>
    <div class="image-container">
        <img src="/blog/figures-visuals/2018-gpcr-fig3.png" alt="Original image" width="500">
        <div class="caption"><strong>Workflow of modeling GDP release using "adaptive seeding".</strong> Starting from the top left, we use Metadynamics to run biased simulations where we push GDP out of the bound state. We then take these simulations and pick states along them (dots on arrows) to seed unbiased MD simulations, which we then stitched together into a Markov state model.  
</div>
    </div>
</body>

## Our model of GDP release unified decades of literature research:
By focusing analysis to secondary structure elements and residues that are shared across all Gα homologs, this model likely captures a universal ‘skeleton’ of changes involved in Gαq activation, expanding upon a previously proposed universal mechanism for Gαq activation. The consistency of this model with a wide variety of structural and biochemical data suggests that it is a promising foundation for future efforts to understand the determinants of GPCR-Gαq interaction specificity, how mutations cause aberrant signaling and disease, and how small molecule inhibitors modulate Gαq activation. 


<body>
    <div class="image-container">
        <img src="/blog/figures-visuals/2018-gpcr-fig4.png" alt="Original image" width="500">
        <div class="caption"><strong>Changes in the allosteric network of Gαq drive GDP release.</strong> Structure of the the ras-like domain of Gαq while bound to GDP (blue) and after its rate-limiting step of GDP release (orange). Major structural changes are marked using labelled arrows, and communication from the GPCR-binding region to GDP binding site is marked using dashed arrows.   
</div>
    </div>
</body>


---
title: "My thesis project online"
description: "This page embeds my thesis in HTML using an iframe."
---

<head>
    <meta charset="UTF-8">
    <title>Embedded Page Example</title>
    <style>
        .iframe-container {
            display: flex;
            justify-content: left; /* Centers the iframe */
            margin-bottom: 20px;
        }
        iframe {
            width: 145%; /* Adjust the width as needed */
            height: 600px;
            border: none;
            margin-left: -20%;
        }
    </style>
</head>

<iframe src="/thesis/index.html" width="200%" align="center" height="600px" frameborder="0"></iframe>
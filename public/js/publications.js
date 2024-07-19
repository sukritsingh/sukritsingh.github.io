// Function to load and parse BibTeX file
function loadBibtexFile(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            callback(xhr.responseText);
        }
    };
    xhr.send(null);
}

// Function to render BibTeX entries
function renderBibtexEntries(bibtexText) {
    var bibtexParser = new BibtexParser();
    bibtexParser.setInput(bibtexText);
    bibtexParser.bibtex();

    var entries = bibtexParser.getEntries();
    var output = '';

    for (var entryKey in entries) {
        var entry = entries[entryKey];
        output += '<div class="publication">';
        output += '<div class="publication-title">' + entry.TITLE + '</div>';
        output += '<div class="publication-authors">' + entry.AUTHOR + '</div>';
        output += '<div class="publication-journal">' + (entry.JOURNAL || '') + '</div>';
        output += '<div class="publication-year">' + entry.YEAR + '</div>';
        output += '</div>';
    }

    document.getElementById('publications').innerHTML = output;
}

// Load and render the BibTeX file
loadBibtexFile('/research/my-papers.bib', renderBibtexEntries);

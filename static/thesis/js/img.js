
Array.prototype.forEach.call(document.querySelector("img"), function (elem) {
    elem.addEventListener("click", function () {
        elem.classList.toggle("enlarged");
    });
});
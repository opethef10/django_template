document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("pre").forEach(function (pre) {
        pre.classList.add("position-relative");
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn btn-sm btn-outline-light copy-code-btn";
        btn.setAttribute("aria-label", "Copy to clipboard");
        btn.innerHTML = '<i class="fa-regular fa-copy"></i>';
        pre.appendChild(btn);

        btn.addEventListener("click", async function () {
            const code = pre.querySelector("code") || pre;
            try {
                await navigator.clipboard.writeText(code.innerText);
                btn.innerHTML = '<i class="fa-solid fa-check"></i>';
                setTimeout(function () {
                    btn.innerHTML = '<i class="fa-regular fa-copy"></i>';
                }, 2000);
            } catch (e) {
                btn.innerHTML = '<i class="fa-solid fa-xmark"></i>';
            }
        });
    });
});

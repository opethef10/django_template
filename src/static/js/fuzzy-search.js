let fuseResults = null;
let currentResults = [];
let currentHighlight = -1;
let currentSubIndex = -1;

// Load data once
async function loadSearchData() {
  let results = [];
  try {
    const res = await fetch("/api/search/");
    if (res.ok) {
      const data = await res.json();
      results = data.results || [];
    }
  } catch (e) {
    // fetch failed or JSON parse error - use empty results
  }

  const fuseOptions = {
    keys: ["search_tokens"],
    threshold: 0.4,
    ignoreDiacritics: true,
    includeScore: true,
    shouldSort: true,
    useExtendedSearch: true,
    minMatchCharLength: 2
  };

  fuseResults = new Fuse(results, fuseOptions);
}

function transliterate(text) {
  const map = { ç:"c",Ç:"C",ğ:"g",Ğ:"G",ı:"i",İ:"I",ö:"o",Ö:"O",ş:"s",Ş:"S",ü:"u",Ü:"U" };
  return text.replace(/[çÇğĞıİöÖşŞüÜ]/g, ch => map[ch] || ch);
}

function renderResults(query, container) {
  let results = [];

  if (!query) {
    results = fuseResults._docs.map(d => ({ item: d }));
  } else {
    // Prefix + multi-word AND search
    const words = transliterate(query.trim().toLowerCase()).split(/\s+/).filter(Boolean);
    if (words.length) {
      const extendedQuery = words.map(w => ({ search_tokens: `^${w}` }));
      results = fuseResults.search({ $and: extendedQuery });
    }
  }

  currentResults = results;
  currentHighlight = results.length ? 0 : -1;
  currentSubIndex = -1;

  container.innerHTML = `
    <ul class="list-group">
      ${results.map((r, idx) => {
        const subLinks = (r.item.sub_links || [])
          .map((sub, subIdx) => `<a href="${sub.url}" class="badge fw-normal text-primary border ms-1 search-sub-link" data-index="${idx}" data-sub-index="${subIdx}">${sub.label}</a>`)
          .join("");
        return `
          <li class="list-group-item d-flex justify-content-between align-items-center ${idx === 0 ? "search-highlight" : ""}" data-index="${idx}" data-url="${r.item.url}">
            <div>
              <a href="${r.item.url}" class="text-decoration-none search-main-link ${idx === 0 ? "search-active" : ""}" data-index="${idx}">${r.item.search_text}</a>
              <div class="text-muted small">${r.item.category}</div>
            </div>
            <div class="d-flex flex-wrap justify-content-end">
              ${subLinks}
            </div>
          </li>
        `;
      }).join("")}
    </ul>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  loadSearchData();

  const searchBox = document.getElementById("navbar-search-input");
  const resultsDiv = document.getElementById("navbar-search-results");
  const resultsList = document.getElementById("navbar-search-results-list");

  let dismissed = false;

  function openResults() {
    dismissed = false;
    showResults();
  }

  function closeResults() {
    resultsDiv.style.display = "none";
    dismissed = true;
  }

  function positionResults() {
    resultsDiv.style.top = (searchBox.getBoundingClientRect().bottom + 4) + "px";
  }

  function showResults() {
    if (dismissed) return;
    renderResults(searchBox.value.trim(), resultsList);
    resultsDiv.style.display = "block";
    positionResults();
  }

  function isResultsOpen() {
    return resultsDiv.style.display === "block";
  }

  function getRadio() {
    return Array.from(resultsList.querySelectorAll("li[data-index]"));
  }

  function setHighlight(index) {
    const rows = getRadio();
    if (!rows.length) {
      currentHighlight = -1;
      currentSubIndex = -1;
      return;
    }
    if (index < 0) {
      index = rows.length - 1;
    } else if (index >= rows.length) {
      index = 0;
    }
    // Highlighting a (possibly) new row: clear any active sub-link.
    if (index !== currentHighlight) {
      currentSubIndex = -1;
    }
    rows.forEach((row, i) => {
      row.classList.toggle("search-highlight", i === index);
    });
    currentHighlight = index;
    const row = rows[index];
    if (row) {
      // Scroll within the fixed dropdown container only, never the page.
      const container = row.closest("#navbar-search-results");
      if (container && container.scrollHeight > container.clientHeight) {
        const cRect = container.getBoundingClientRect();
        const rRect = row.getBoundingClientRect();
        const rowTop = rRect.top - cRect.top + container.scrollTop;
        const rowBottom = rowTop + rRect.height;
        if (rowTop < container.scrollTop) {
          container.scrollTop = rowTop;
        } else if (rowBottom > container.scrollTop + container.clientHeight) {
          container.scrollTop = rowBottom - container.clientHeight;
        }
      }
    }
    paintActive();
  }

  function getSubsOf(index) {
    return Array.from(resultsList.querySelectorAll(`.search-sub-link[data-index="${index}"]`));
  }

  // Visually mark the highlighted row's main link and the currently active
  // sub-link (if any).
  function paintActive() {
    resultsList.querySelectorAll(".search-sub-link.search-sub-active")
      .forEach(el => el.classList.remove("search-sub-active"));
    resultsList.querySelectorAll(".search-main-link.search-active")
      .forEach(el => el.classList.remove("search-active"));

    if (currentHighlight === -1) return;

    // The main link is styled as active only while no sub-link is targeted.
    if (currentSubIndex === -1) {
      const main = resultsList.querySelector(`.search-main-link[data-index="${currentHighlight}"]`);
      if (main) main.classList.add("search-active");
      return;
    }

    const sub = getSubsOf(currentHighlight)[currentSubIndex];
    if (sub) sub.classList.add("search-sub-active");
  }

  // Tab cycles through the highlighted row's sub-links, then advances to the
  // next row. Focus stays in the search box so the user can keep typing.
  function tabForward() {
    const rows = getRadio();
    if (!rows.length) return;
    if (currentHighlight === -1) {
      setHighlight(0);
      return;
    }
    const subs = getSubsOf(currentHighlight);
    if (subs.length) {
      setSubActive(currentSubIndex + 1);
    } else {
      // No sub-links here: move the highlight forward instead.
      moveHighlight(1);
    }
  }

  // Tab cycles backwards (Shift+Tab): sub-links of the highlighted row in
  // reverse, then back to the previous row.
  function tabBackward() {
    const rows = getRadio();
    if (!rows.length) return;
    if (currentHighlight === -1) {
      setHighlight(rows.length - 1);
      return;
    }
    if (currentSubIndex === -1) {
      // At the main link: move to the previous row, landing on its last
      // sub-link (or its main link if that row has none).
      const prev = currentHighlight - 1 < 0 ? rows.length - 1 : currentHighlight - 1;
      setHighlight(prev);
      const subs = getSubsOf(prev);
      if (subs.length) {
        currentSubIndex = subs.length - 1;
        paintActive();
      }
      return;
    }
    // On a sub-link: move back toward the main link within this row.
    setSubActive(currentSubIndex - 1);
  }

  function setSubActive(index) {
    const subs = getSubsOf(currentHighlight);
    if (!subs.length) {
      // This row has no sub-links: just advance the row highlight.
      moveHighlight(1);
      return;
    }
    if (index >= subs.length) {
      // Past the last sub-link of this row: move to the next row.
      currentSubIndex = -1;
      paintActive();
      moveHighlight(1);
      return;
    }
    currentSubIndex = index;
    paintActive();
  }

  function moveHighlight(delta) {
    const rows = getRadio();
    if (!rows.length) {
      currentHighlight = -1;
      return;
    }
    // Derive the current position from the DOM so we never desync after re-renders.
    let cur = rows.findIndex(r => r.classList.contains("search-highlight"));
    let next;
    if (delta > 0) {
      next = cur === -1 ? 0 : cur + 1;
      if (next >= rows.length) next = 0;
    } else {
      next = cur === -1 ? rows.length - 1 : cur - 1;
      if (next < 0) next = rows.length - 1;
    }
    setHighlight(next);
  }

  function navigateTo(index, subIndex) {
    const item = currentResults[index];
    if (!item || !item.item) return;
    if (subIndex !== undefined && subIndex >= 0 && (item.item.sub_links || [])[subIndex]) {
      window.location.href = item.item.sub_links[subIndex].url;
      return;
    }
    if (item.item.url) {
      window.location.href = item.item.url;
    }
  }

  // Handle Down/Up keys while the dropdown is open. Focus always stays in the
  // search box so the user can keep typing; the highlight just moves.
  function handleArrowKeys(e) {
    if (e.key !== "ArrowDown" && e.key !== "ArrowUp") return false;
    if (!isResultsOpen()) return false;
    e.preventDefault();
    const delta = e.key === "ArrowDown" ? 1 : -1;
    moveHighlight(delta);
    return true;
  }

  // Typing re-opens a dismissed dropdown.
  searchBox.addEventListener("input", openResults);
  // Focusing the box re-opens the dropdown (e.g. after blur or Escape).
  searchBox.addEventListener("focus", openResults);
  // Losing focus closes the dropdown, unless the focus moves into the results
  // (e.g. a mouse click / tab targeting a result link or sub-link).
  searchBox.addEventListener("blur", e => {
    const next = e.relatedTarget;
    if (next && resultsDiv.contains(next)) return;
    closeResults();
  });
  window.addEventListener("scroll", positionResults, true);
  window.addEventListener("resize", positionResults);

  // Close button inside the dropdown
  resultsDiv.addEventListener("click", e => {
    if (e.target.closest(".search-close-btn")) {
      resultsDiv.style.display = "none";
      searchBox.blur();
    }
  });

  // Hide when clicking outside
  document.addEventListener("click", e => {
    if (!searchBox.closest(".position-relative").contains(e.target)) {
      resultsDiv.style.display = "none";
    }
  });

  // Keyboard navigation for the search box. Focus stays in the search box so
  // the user can keep typing after using the arrows or tab.
  searchBox.addEventListener("keydown", e => {
    if (handleArrowKeys(e)) return;
    if (!isResultsOpen()) return;
    if (e.key === "Enter") {
      e.preventDefault();
      if (currentHighlight >= 0 && currentHighlight < currentResults.length) {
        navigateTo(currentHighlight, currentSubIndex);
      } else if (currentResults.length > 0) {
        navigateTo(0, currentSubIndex);
      }
      return;
    }
    if (e.key === "Tab") {
      e.preventDefault();
      if (e.shiftKey) {
        tabBackward();
      } else {
        tabForward();
      }
    }
  });

  // Ctrl+K focuses the search box
  document.addEventListener("keydown", e => {
    if (e.ctrlKey && e.key.toLowerCase() === "k") {
      e.preventDefault();
      searchBox.focus();
      searchBox.select();
      return;
    }
    // Close the dropdown from anywhere (focus may have left the search box).
    if (e.key === "Escape") {
      closeResults();
      e.preventDefault();
      e.stopPropagation();
    }
  });
});
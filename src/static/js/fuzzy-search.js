const resultsDiv = document.getElementById("search-results");

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

function renderResults(query) {
  let results = [];

  if (!query) {
    // Empty input → show all results
    results = fuseResults._docs.map(d => ({ item: d }));
  } else {
    // Prefix + multi-word AND search
    const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
    if (words.length) {
      const extendedQuery = words.map(w => ({ search_tokens: `^${w}` }));
      results = fuseResults.search({ $and: extendedQuery });
    }
  }

  resultsDiv.innerHTML = `
    <ul class="list-group">
      ${results.map(r => {
        const subLinks = (r.item.sub_links || [])
          .map(sub => `<a href="${sub.url}" class="badge fw-normal text-primary border ms-1">${sub.label}</a>`)
          .join("");
        return `
          <li class="list-group-item d-flex justify-content-between align-items-center">
            <div>
              <a href="${r.item.url}" class="text-decoration-none">${r.item.search_text}</a>
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

  const searchBox = document.getElementById("search-box");
  const resultsDiv = document.getElementById("search-results");
  const searchModalEl = document.getElementById("searchModal");
  const searchModal = new bootstrap.Modal(searchModalEl);

    // Focus input after modal is fully shown
searchModalEl.addEventListener("shown.bs.modal", () => {
  searchBox.focus();
    renderResults("");
});

    searchModalEl.addEventListener("hidden.bs.modal", () => {
  searchBox.blur();
});

// Ctrl+K shortcut
document.addEventListener("keydown", e => {
  if (e.ctrlKey && e.key.toLowerCase() === "k") {
    e.preventDefault();
    searchModal.show();
  }
});

// Navbar trigger
document.getElementById("navbarSearchTrigger").addEventListener("click", () => {
  searchModal.show();
});

searchBox.addEventListener("input", e => {
  renderResults(e.target.value);
});

  // Prefix + multi-word AND search
    // searchBox.addEventListener("input", e => {
  // const q = e.target.value.trim().toLowerCase();
  // if (!q) {
  //   resultsDiv.innerHTML = "";
  //   return;
  // }

//   // Prefix + multi-word AND search
//   // function prefixSearch(fuse, query) {
//   //   const words = query.trim().toLowerCase().split(/\s+/);
//   //   if (!words.length) return [];
//   //   const extendedQuery = words.map(w => ({ search_tokens: `^${w}` }));
//   //   return fuse.search({ $and: extendedQuery });
//   // }
//     function prefixSearch(fuse, query) {
//       const words = query.split(/\s+/).filter(Boolean);
//       if (!words.length) return [];
//       const extendedQuery = words.map(w => ({ search_tokens: `^${w}` }));
//       return fuse.search({ $and: extendedQuery });
//     }

//   // Collect all results
//   // let results = prefixSearch(fuseResults, q);

//         let results = [];

//   if (!q) {
//     // Empty input → show all results
//     results = fuseResults._docs.map(d => ({ item: d }));
//   } else {
//     // Prefix + multi-word AND search

//     results = prefixSearch(fuseResults, q);
//   }
//   // Limit total displayed results
//   // results = results.slice(0, 15);

//   // Render all results in a single block
//   resultsDiv.innerHTML = `
//     <ul class="list-group">
//       ${results.map(r => `
//         <li class="list-group-item">
//           <a href="${
//             r.item.url
//           }">
//             ${r.item.search_text}
//           </a>
//           <div class="text-muted small">${r.item.category}</div>
//         </li>
//       `).join("")}
//     </ul>
//   `;
// });

});


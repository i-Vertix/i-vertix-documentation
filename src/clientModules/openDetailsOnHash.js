/**
 * Opens a collapsed <details> when the URL hash points to an element inside it
 * (e.g. a heading in the <summary> or in the body), so links from the table of contents
 * or within the page land on visible content.
 */

function openDetailsForHash(hash) {
    if (!hash || hash.length < 2) return;
    let target;
    try {
        target = document.getElementById(decodeURIComponent(hash.slice(1)));
    } catch (e) {
        return;
    }
    if (!target) return;

    // open every enclosing <details>, outermost first
    const closed = [];
    for (let el = target.closest('details'); el; el = el.parentElement?.closest('details')) {
        if (!el.open || el.getAttribute('data-collapsed') === 'true') closed.unshift(el);
    }
    for (const details of closed) {
        // Docusaurus' Details component toggles via a click on its <summary> (keeps its animation state in sync)
        const summary = details.querySelector(':scope > summary');
        if (summary) summary.click();
        else details.open = true;
    }
    if (closed.length > 0) {
        // wait for the expand animation to start, then make sure the target is in view
        setTimeout(() => target.scrollIntoView(), 50);
    }
}

export function onRouteDidUpdate({location}) {
    // let the page render first
    setTimeout(() => openDetailsForHash(location.hash), 0);
}

if (typeof window !== 'undefined') {
    window.addEventListener('hashchange', () => openDetailsForHash(window.location.hash));
}

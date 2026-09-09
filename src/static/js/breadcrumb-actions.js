// Breadcrumb action bar: copy link, share, copy as markdown.
(function () {
    'use strict';

    var currentUrl = window.location.href;

    function toastFeedback(message, type) {
        var existing = document.querySelector('.crumb-toast');
        if (existing) existing.remove();
        var toast = document.createElement('div');
        type = type || 'success';
        toast.className = 'crumb-toast ';
        if (type === 'error') {
            toast.classList.add('text-bg-danger');
        } else {
            toast.classList.add('text-bg-success');
        }
        toast.textContent = message;
        document.body.appendChild(toast);
        setTimeout(function () {
            toast.classList.add('show');
        }, 10);
        setTimeout(function () {
            toast.classList.remove('show');
            setTimeout(function () { toast.remove(); }, 300);
        }, 2000);
    }

    function copyText(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            return navigator.clipboard.writeText(text);
        }
        var textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        try {
            document.execCommand('copy');
        } finally {
            textarea.remove();
        }
        return Promise.resolve();
    }

    function copyPageLink() {
        copyText(currentUrl).then(function () {
            toastFeedback('Link copied to clipboard');
        }).catch(function () {
            toastFeedback('Copy failed', 'error');
        });
    }

    function shareNative() {
        if (!navigator.share) {
            toastFeedback('Native sharing is not supported in this browser', 'error');
            return;
        }
        navigator.share({ url: currentUrl }).catch(function () {
            // user cancelled or failed; ignore
        });
    }

    function mdUrl() {
        var url = currentUrl.split(/[?#]/)[0];
        if (url.endsWith('/')) {
            url = url.slice(0, -1);
        }
        return url + '.md';
    }

    function copyAsMarkdown() {
        fetch(mdUrl(), { headers: { 'Accept': 'text/markdown,text/plain,*/*' } })
            .then(function (response) {
                if (!response.ok) throw new Error('Not available');
                return response.text();
            })
            .then(function (text) {
                return copyText(text).then(function () {
                    toastFeedback('Markdown copied to clipboard');
                });
            })
            .catch(function () {
                toastFeedback('This page is not available in Markdown format', 'error');
            });
    }

    window.copyPageLink = copyPageLink;
    window.shareNative = shareNative;
    window.copyAsMarkdown = copyAsMarkdown;
    window.toastFeedback = toastFeedback;
})();

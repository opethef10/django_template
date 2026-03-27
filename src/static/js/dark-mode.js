const theme = localStorage.getItem('bsTheme') || 'dark';
document.documentElement.setAttribute('data-bs-theme', theme);
document.addEventListener('DOMContentLoaded', () => {
    const htmlElement = document.documentElement;
    const icon = document.getElementById('themeToggle');

    function updateIcon(theme) {
        if (theme === 'dark') {
            icon.classList.replace('fa-moon', 'fa-sun');
        } else {
            icon.classList.replace('fa-sun', 'fa-moon');
        }
    }

    updateIcon(htmlElement.getAttribute('data-bs-theme'));

    icon.addEventListener('click', () => {
        const newTheme =
            htmlElement.getAttribute('data-bs-theme') === 'dark'
                ? 'light'
                : 'dark';

        htmlElement.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('bsTheme', newTheme);
        updateIcon(newTheme);
    });
});

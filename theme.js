(() => {
  const root = document.documentElement;
  const button = document.querySelector('[data-theme-toggle]');
  if (!button) return;

  let stored;
  try { stored = localStorage.getItem('portfolio-theme'); } catch { /* Storage may be unavailable. */ }
  const systemDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initial = stored === 'light' || stored === 'dark' ? stored : systemDark ? 'dark' : 'light';
  button.hidden = false;

  function setTheme(theme) {
    root.dataset.theme = theme;
    const isDark = theme === 'dark';
    button.setAttribute('aria-pressed', String(isDark));
    button.setAttribute('aria-label', isDark ? '切换至浅色模式' : '切换至深色模式');
    button.textContent = isDark ? '☀ 浅色' : '◐ 深色';
  }

  setTheme(initial);
  button.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    try { localStorage.setItem('portfolio-theme', next); } catch { /* The control still works for this visit. */ }
  });
})();
